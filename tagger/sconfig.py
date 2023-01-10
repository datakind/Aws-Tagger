import boto3
import os
import socket
import botocore

def _is_retryable_exception(exception):
    return not isinstance(exception, botocore.exceptions.ClientError) or \
        (exception.response["Error"]["Code"] in ['LimitExceededException', 'RequestLimitExceeded', 'Throttling', 'ParamValidationError'])

def _format_dict(tags):
    output = []
    for (key, value) in tags.items():
        output.append("%s:%s" % (key, value))

    return ", ".join(output)

def _dict_to_aws_tags(tags):
    return [{'Key': key, 'Value': value} for (key, value) in tags.items() if not key.startswith('aws:')]

def _aws_tags_to_dict(aws_tags):
    return {x['Key']: x['Value'] for x in aws_tags if not x['Key'].startswith('aws:')}
    
def _arn_to_name(resource_arn):
    parts = resource_arn.split(':')
    name = parts[-1]
    parts = name.split('/', 1)
    if len(parts) == 2:
        name = parts[-1]
    return name

# https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
def _name_to_arn(resource_name,service,region,account_id):
    if not region == None:
        arnstring = "arn:aws:"+service+":"+region+":"+account_id+":"+resource_name
        return arnstring
    else:
        if service != "braket":
            arnstring = "arn:aws:"+service+"::"+account_id+":"+resource_name
        else:
            arnstring = "arn:aws:"+service+":::"+resource_name
        return arnstring

def _fetch_temporary_credentials(role):
    sts = boto3.client('sts', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

    response = sts.assume_role(RoleArn=role, RoleSessionName='aws-tagger.%s' % socket.gethostname())
    access_key_id = response.get('Credentials', {}).get('AccessKeyId', None)
    secret_access_key = response.get('Credentials', {}).get('SecretAccessKey', None)
    session_token = response.get('Credentials', {}).get('SessionToken', None)
    return access_key_id, secret_access_key, session_token
    
def _client(name, role, region, accesskey, secretaccesskey):
    kwargs = {}

    if region:
        kwargs['region_name'] = region
    elif os.environ.get('AWS_REGION'):
        kwargs['region_name'] = os.environ['AWS_REGION']

    if role:
        access_key_id, secret_access_key, session_token = _fetch_temporary_credentials(role)
        kwargs['aws_access_key_id'] = access_key_id
        kwargs['aws_secret_access_key'] = secret_access_key
        kwargs['aws_session_token'] = session_token
    if accesskey and secretaccesskey:
        kwargs['aws_access_key_id'] = accesskey
        kwargs['aws_secret_access_key'] = secretaccesskey
        print("boto print: "+region)
        if 'AWS_REGION' not in os.environ and region is None:
            # print("setting base region")
            kwargs['region_name'] = "us-east-1"
    elif os.environ.get('AWS_ACCESS_KEY_ID') and os.environ.get('AWS_SECRET_ACCESS_KEY'):
      kwargs['aws_access_key_id'] = os.environ.get('AWS_ACCESS_KEY_ID')
      kwargs['aws_secret_access_key'] = os.environ.get('AWS_SECRET_ACCESS_KEY')
      
    print(kwargs)
    return boto3.client(name, **kwargs)

def _parse_arn( resource_arn):
        product = None
        resource_id = None
        parts = resource_arn.split(':')
        if len(parts) > 5:
            product = parts[2]
            resource_id = parts[5]
            resource_parts = resource_id.split('/')
            if len(resource_parts) > 1:
                resource_id = resource_parts[-1]

        return product, resource_id

def resourcesearch(taggers,resource_id, role=None, region=None):
        print(f'Searching for resource with identifier: {resource_id}')
        tagger = None
        resource_arn = resource_id
        if resource_id.startswith('arn:'):
            print("Parsing ARN for Resource Type")
            product, resource_id = _parse_arn(resource_id)
            print(f'Product: ${product}, resource_id: ${resource_id}')
            if product:
                tagger = taggers.get(product)
        # else:
        #     tagger = self.taggers['s3']


        if resource_id.startswith('i-'):
            tagger = taggers['ec2']
            resource_arn = resource_id
        elif resource_id.startswith('vol-'):
            tagger = taggers['ec2']
            resource_arn = resource_id
        elif resource_id.startswith('snap-'):
            tagger = taggers['ec2']
            resource_arn = resource_id

        if resource_id.startswith('ami-'):
            tagger = taggers['ami']
            resource_arn = resource_id
        
        if resource_id.startswith('dopt-'):
            tagger = taggers['dopt']
            resource_arn = resource_id

        if resource_id.startswith('igw-'):
            tagger = taggers['igw']
            resource_arn = resource_id
        
        if resource_id.startswith('acl-'):
            tagger = taggers['acl']
            resource_arn = resource_id

        if resource_id.startswith('eni-'):
            tagger = taggers['eni']
            resource_arn = resource_id

        if resource_id.startswith('rtb-'):
            tagger = taggers['rtb']
            resource_arn = resource_id

        if resource_id.startswith('sg-'):
            tagger = taggers['sg']
            resource_arn = resource_id
        
        if resource_id.startswith('subnet-'):
            tagger = taggers['subnet']
            resource_arn = resource_id

        if resource_id.startswith('vpc-'):
            tagger = taggers['vpc']
            resource_arn = resource_id

        if resource_id.startswith('vpc-'):
            tagger = taggers['vpc']
            resource_arn = resource_id

        if resource_id.startswith('o-') and "/" in resource_id:
            tagger = taggers['organization']
            resource_arn = resource_id

        if tagger == None:
            resourecheck = resource_finder(resource_id,role=role, region=region)
            if not resourecheck == "No Resource Found":
                print(resourecheck)
                tagger = taggers[resourecheck]
                resource_arn = resource_id
            else:
                print("checking by arn builder")
                resourecheck = resource_finder_by_arn_builder(resource_id)
                if resourecheck != "No Resource Found":
                    print(resourecheck)
                    tagger = taggers[resourecheck]
                    resource_arn = resource_id
        return resource_arn, tagger


def resource_finder_by_arn_builder(resourecheck):
    # Finding ManagedPolicies
    print(resourecheck)
    try:
        region = None
        accountclient = _client('sts', role=None, region=region)
        account_id = accountclient.get_caller_identity()["Account"]
        service = "iam"

        client = _client('iam',role=None, region=None)
        ManagedPoliciesresourecheck = "policy/"+resourecheck
        ManagedPoliciesresourecheck = _name_to_arn(resource_name=ManagedPoliciesresourecheck,region=region,service=service,account_id=account_id)
        client.get_policy(PolicyArn=resourecheck)
        return "managedpolicy"
    except Exception as m:
    # Finding Saml Provider
        try:
            SamlProviderresourecheck = "saml-provider/"+resourecheck
            SamlProviderresourecheck = _name_to_arn(resource_name=SamlProviderresourecheck,region=region,service=service,account_id=account_id)
            client.get_saml_provider(SAMLProviderArn=SamlProviderresourecheck)
            return "samlprovider"
        except Exception as m:
            # Finding resource group
            try:
                service = "resource-groups"
                client = _client('resource-groups',role=None, region=None)

                my_session = boto3.session.Session()
                region = my_session.region_name
                resourcegroupresourecheck = "group/"+resourecheck
                resourcegroupresourecheck = _name_to_arn(resource_name=resourcegroupresourecheck,region=region,service=service,account_id=account_id)
                client.get_group(Group=resourcegroupresourecheck)
                return "resourcegroup"
            except Exception as m:
                # Finding SNS Topic
                try:
                    service = "sns"
                    client = _client('sns',role=None, region=None)

                    my_session = boto3.session.Session()
                    region = my_session.region_name
                    resourcegroupresourecheck = _name_to_arn(resource_name=resourecheck,region=region,service=service,account_id=account_id)
                    client.get_topic_attributes(TopicArn=resourcegroupresourecheck)
                    return "snstopic"
                except Exception as m:
                    # Finding Secret Manager Secret
                    try:
                        service = "secretsmanager"
                        client = _client('secretsmanager',role=None, region=None)

                        my_session = boto3.session.Session()
                        region = my_session.region_name
                        secretmanagersecretresourecheck = "secret:"+resourecheck
                        secretmanagersecretresourecheck = _name_to_arn(resource_name=secretmanagersecretresourecheck,region=region,service=service,account_id=account_id)
                        print(secretmanagersecretresourecheck)
                        client.describe_secret(SecretId=secretmanagersecretresourecheck)
                        return "SecretsManagerSecret"
                    except Exception as m:
                        # Finding Cloudformation stack
                        try:
                            service = "cloudformation"
                            client = _client('cloudformation',role=None, region=None)

                            my_session = boto3.session.Session()
                            region = my_session.region_name
                            cfstackresourecheck = "stack/"+resourecheck
                            cfstackresourecheck = _name_to_arn(resource_name=cfstackresourecheck,region=region,service=service,account_id=account_id)
                            print(cfstackresourecheck)
                            client.describe_stacks(StackName=cfstackresourecheck)
                            return "cloudformationstack"
                        except Exception as m:
                            print(m)

def resource_finder(resource_name,role,region):
    # check Instance profiles
    resource_checker = boto3.resource('iam')
    # print(dir(resource_checker))
    try:
        resource_checker.InstanceProfile(resource_name).arn
        return 'instanceprofile'
    except Exception as m:
    # check efs
        resource_checker = _client("efs",role,region)
        try:
            resource_checker.describe_file_systems(FileSystemId=resource_name)
            return "elasticfilesystem"
        except Exception as m:
    # check elasticbenstalk
            resource_checker = _client("elasticbeanstalk",role,region)
            try:
                instance_profile = resource_checker.describe_applications(ApplicationNames=[resource_name])
                if len(instance_profile["Applications"]) != 0:
                    return "elasticbenstalkapp"
                else:
                    purposebreak = 1+"purposebreak"
            except Exception as m:
        # check Lambda
                    resource_checker = _client("lambda",role,region)
                    try:
                        resource_checker.get_function(FunctionName=resource_name)
                        return "lambda"
                    except Exception as m:
        # check redshift cluster group
                        resource_checker = _client("redshift",role,region)
                        try:
                            resource_checker.describe_cluster_parameter_groups(ParameterGroupName=resource_name)
                            return "redshiftclusergroup"
                        except Exception as m:
        # check route53 hosted zone
                            resource_checker = _client("route53",role,region)
                            try:
                                resource_checker.get_hosted_zone(Id=resource_name)
                                return "route53hostedzone"
                            except Exception as m:
        # check Sagemaker Notebook Instance
                                resource_checker = _client("sagemaker",role,region)
                                try:
                                    resource_checker.describe_notebook_instance(NotebookInstanceName=resource_name)
                                    return "SageMakerNotebookInstance"
                                except Exception as m:
                                    return "No Resource Found"
    # check KMS Key
                # try:
                #     resource_checker = _client("kms",role,region)
                #     resource_checker.describe_key(KeyId=resource_name)
                #     return "KMSKey"
                # except Exception as m:
                #     print(m)
                #     return "No Resource Found"