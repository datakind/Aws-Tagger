import os
import boto3
import botocore
from retrying import retry
import tagger.services as tagservices
import socket
import csv
from . import sconfig

#tagservices.appstream.service.AppstreamTagger


def resource_finder(resource_name,role,region):
    # check Instance profiles
    resource_checker = boto3.resource('iam')
    # print(dir(resource_checker))
    try:
        resource_checker.InstanceProfile(resource_name).arn
        return 'instanceprofile'
    except Exception as m:
    # check efs
        resource_checker = sconfig._client("efs",role,region)
        try:
            resource_checker.describe_file_systems(FileSystemId=resource_name)
            return "elasticfilesystem"
        except Exception as m:
    # check elasticbenstalk
            resource_checker = sconfig._client("elasticbeanstalk",role,region)
            try:
                instance_profile = resource_checker.describe_applications(ApplicationNames=[resource_name])
                if len(instance_profile["Applications"]) != 0:
                    return "elasticbenstalkapp"
                else:
                    purposebreak = 1+"purposebreak"
            except Exception as m:
        # check Lambda
                    resource_checker = sconfig._client("lambda",role,region)
                    try:
                        resource_checker.get_function(FunctionName=resource_name)
                        return "lambda"
                    except Exception as m:
        # check redshift cluster group
                        resource_checker = sconfig._client("redshift",role,region)
                        try:
                            resource_checker.describe_cluster_parameter_groups(ParameterGroupName=resource_name)
                            return "redshiftclusergroup"
                        except Exception as m:
        # check route53 hosted zone
                            resource_checker = sconfig._client("route53",role,region)
                            try:
                                resource_checker.get_hosted_zone(Id=resource_name)
                                return "route53hostedzone"
                            except Exception as m:
        # check Sagemaker Notebook Instance
                                resource_checker = sconfig._client("sagemaker",role,region)
                                try:
                                    resource_checker.describe_notebook_instance(NotebookInstanceName=resource_name)
                                    return "sagemakernotebookinstance"
                                except Exception as m:
                                    return "No Resource Found"
    # check KMS Key
                # try:
                #     resource_checker = sconfig._client("kms",role,region)
                #     resource_checker.describe_key(KeyId=resource_name)
                #     return "KMSKey"
                # except Exception as m:
                #     print(m)
                #     return "No Resource Found"
    




def resource_finder_by_arn_builder(resourecheck):
    # Finding ManagedPolicies
    print(resourecheck)
    try:
        region = None
        accountclient = sconfig._client('sts', role=None, region=region)
        account_id = accountclient.get_caller_identity()["Account"]
        service = "iam"

        client = sconfig._client('iam',role=None, region=None)
        ManagedPoliciesresourecheck = "policy/"+resourecheck
        ManagedPoliciesresourecheck = sconfig._name_to_arn(resource_name=ManagedPoliciesresourecheck,region=region,service=service,account_id=account_id)
        client.get_policy(PolicyArn=resourecheck)
        return "managedpolicy"
    except Exception as m:
    # Finding Saml Provider
        try:
            SamlProviderresourecheck = "saml-provider/"+resourecheck
            SamlProviderresourecheck = sconfig._name_to_arn(resource_name=SamlProviderresourecheck,region=region,service=service,account_id=account_id)
            client.get_saml_provider(SAMLProviderArn=SamlProviderresourecheck)
            return "samlprovider"
        except Exception as m:
            # Finding resource group
            try:
                service = "resource-groups"
                client = sconfig._client('resource-groups',role=None, region=None)

                my_session = boto3.session.Session()
                region = my_session.region_name
                resourcegroupresourecheck = "group/"+resourecheck
                resourcegroupresourecheck = sconfig._name_to_arn(resource_name=resourcegroupresourecheck,region=region,service=service,account_id=account_id)
                client.get_group(Group=resourcegroupresourecheck)
                return "resourcegroup"
            except Exception as m:
                # Finding SNS Topic
                try:
                    service = "sns"
                    client = sconfig._client('sns',role=None, region=None)

                    my_session = boto3.session.Session()
                    region = my_session.region_name
                    resourcegroupresourecheck = sconfig._name_to_arn(resource_name=resourecheck,region=region,service=service,account_id=account_id)
                    client.get_topic_attributes(TopicArn=resourcegroupresourecheck)
                    return "snstopic"
                except Exception as m:
                    # Finding Secret Manager Secret
                    try:
                        service = "secretsmanager"
                        client = sconfig._client('secretsmanager',role=None, region=None)

                        my_session = boto3.session.Session()
                        region = my_session.region_name
                        secretmanagersecretresourecheck = "secret:"+resourecheck
                        secretmanagersecretresourecheck = sconfig._name_to_arn(resource_name=secretmanagersecretresourecheck,region=region,service=service,account_id=account_id)
                        print(secretmanagersecretresourecheck)
                        client.describe_secret(SecretId=secretmanagersecretresourecheck)
                        return "secretsmanagersecret"
                    except Exception as m:
                        # Finding Cloudformation stack
                        try:
                            service = "cloudformation"
                            client = sconfig._client('cloudformation',role=None, region=None)

                            my_session = boto3.session.Session()
                            region = my_session.region_name
                            cfstackresourecheck = "stack/"+resourecheck
                            cfstackresourecheck = sconfig._name_to_arn(resource_name=cfstackresourecheck,region=region,service=service,account_id=account_id)
                            print(cfstackresourecheck)
                            client.describe_stacks(StackName=cfstackresourecheck)
                            return "cloudformationstack"
                        except Exception as m:
                            print(m)
    
    
class SingleResourceTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None, tag_volumes=False):
        # print(resourcetype)
        self.taggers = {}
        self.taggers['ec2'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, resourcetype, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['ami'] = tagservices.ec2.service.AMITagger(dryrun, verbose, resourcetype, role=role, region=region)
        self.taggers['dopt'] = tagservices.ec2.service.DHCPOTagger(dryrun, verbose, resourcetype, role=role, region=region)
        self.taggers['igw'] = tagservices.ec2.service.InternetGatewayTagger(dryrun, verbose, resourcetype, role=role, region=region)
        self.taggers['acl'] = tagservices.ec2.service.NetworkAclTagger(dryrun, verbose, resourcetype, role=role, region=region,)
        self.taggers['igw'] = tagservices.ec2.service.InternetGatewayTagger(dryrun, verbose, resourcetype, role=role, region=region)
        self.taggers['eni'] = tagservices.ec2.service.NetworkInterfaceTagger(dryrun, verbose, resourcetype, role=role, region=region)
        self.taggers['rtb'] = tagservices.ec2.service.RouteTableTagger(dryrun, verbose, resourcetype, role=role, region=region)
        self.taggers['sg'] = tagservices.ec2.service.SecurityGroupTagger(dryrun, verbose, resourcetype, role=role, region=region)
        self.taggers['subnet'] = tagservices.ec2.service.SubnetTagger(dryrun, verbose, resourcetype, role=role, region=region)
        self.taggers['organization'] = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, role=role, region=region)
        self.taggers['vpc'] = tagservices.ec2.service.VPCTagger(dryrun, verbose, resourcetype, role=role, region=region)
        self.taggers['elasticfilesystem'] = tagservices.efs.service.EFSTagger(dryrun, verbose, role=role, region=region)
        self.taggers['rds'] = tagservices.rds.service.RDSTagger(dryrun, verbose, role=role, region=region)
        self.taggers['elasticloadbalancing'] = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, role=role, region=region)
        self.taggers['elasticbenstalkapp'] = tagservices.elasticbeanstalk.service.EBSATagger(dryrun, verbose, role=role, region=region)
        self.taggers['resourcegroup'] = tagservices.resourcegroups.service.ResourceGroupTagger(dryrun, verbose, role=role, region=region)
        self.taggers['snstopic'] = tagservices.sns.service.SNSTopicTagger(dryrun, verbose, role=role, region=region)
        self.taggers['cloudformationstack'] = tagservices.cloudformation.service.CloudformationStackTagger(dryrun, verbose, role=role, region=region)
        self.taggers['secretsmanagersecret'] = tagservices.secretsmanager.service.SecretManagerSecretTagger(dryrun, verbose, role=role, region=region)
        self.taggers['sagemakernotebookinstance'] = tagservices.sagemaker.service.SagemakerNotebookInstanceTagger(dryrun, verbose, role=role, region=region)
        self.taggers['elasticache'] = tagservices.elasticcache.service.ElasticacheTagger(dryrun, verbose, role=role, region=region)
        self.taggers['instanceprofile'] = tagservices.iam.service.InstanceProfileTagger(dryrun, verbose, role=role, region=region)
        self.taggers['route53hostedzone'] = tagservices.route53.service.Route53HostedZoneTagger(dryrun, verbose, role=role, region=region)
        self.taggers['managedpolicy'] = tagservices.iam.service.ManagedPolicyTagger(dryrun, verbose, role=role, region=region)
        self.taggers['samlprovider'] = tagservices.iam.service.SamlProviderTagger(dryrun, verbose, role=role, region=region)
        self.taggers['s3'] = tagservices.s3.service.S3Tagger(dryrun, verbose, role=role, region=region)
        self.taggers['es'] = tagservices.es.service.ESTagger(dryrun, verbose, role=role, region=region)
        self.taggers['kinesis'] = tagservices.kinesis.service.KinesisTagger(dryrun, verbose, role=role, region=region)
        self.taggers['cloudfront'] = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, role=role, region=region)
        self.taggers['logs'] = tagservices.cloudwatch.service.CloudWatchLogsTagger(dryrun, verbose, role=role, region=region)
        self.taggers['dynamodb'] = tagservices.dynamodb.service.DynamoDBTagger(dryrun, verbose, role=role, region=region)
        self.taggers['lambda'] = tagservices.awslambda.service.LambdaTagger(dryrun, verbose, role=role, region=region)
        self.taggers['redshiftclusergroup'] = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, role=role, region=region)
    

    def tag(self, resource_id, tags, role=None, region=None):
        if resource_id == "":
            return

        if len(tags) == 0:
            return

        tagger = None
        resource_arn = resource_id
        if resource_id.startswith('arn:'):
            product, resource_id = self._parse_arn(resource_id)
            if product:
                tagger = self.taggers.get(product)
        # else:
        #     tagger = self.taggers['s3']


        if resource_id.startswith('i-'):
            tagger = self.taggers['ec2']
            resource_arn = resource_id
        elif resource_id.startswith('vol-'):
            tagger = self.taggers['ec2']
            resource_arn = resource_id
        elif resource_id.startswith('snap-'):
            tagger = self.taggers['ec2']
            resource_arn = resource_id

        if resource_id.startswith('ami-'):
            tagger = self.taggers['ami']
            resource_arn = resource_id
        
        if resource_id.startswith('dopt-'):
            tagger = self.taggers['dopt']
            resource_arn = resource_id

        if resource_id.startswith('igw-'):
            tagger = self.taggers['igw']
            resource_arn = resource_id
        
        if resource_id.startswith('acl-'):
            tagger = self.taggers['acl']
            resource_arn = resource_id

        if resource_id.startswith('eni-'):
            tagger = self.taggers['eni']
            resource_arn = resource_id

        if resource_id.startswith('rtb-'):
            tagger = self.taggers['rtb']
            resource_arn = resource_id

        if resource_id.startswith('sg-'):
            tagger = self.taggers['sg']
            resource_arn = resource_id
        
        if resource_id.startswith('subnet-'):
            tagger = self.taggers['subnet']
            resource_arn = resource_id

        if resource_id.startswith('vpc-'):
            tagger = self.taggers['vpc']
            resource_arn = resource_id

        if resource_id.startswith('vpc-'):
            tagger = self.taggers['vpc']
            resource_arn = resource_id

        if resource_id.startswith('o-') and "/" in resource_id:
            tagger = self.taggers['organization']
            resource_arn = resource_id

        if tagger == None:
            resourecheck = resource_finder(resource_id,role=role, region=region)
            if not resourecheck == "No Resource Found":
                print(resourecheck)
                tagger = self.taggers[resourecheck]
                resource_arn = resource_id
            else:
                print("checking by arn builder")
                resourecheck = resource_finder_by_arn_builder(resource_id)
                if resourecheck != "No Resource Found":
                    print(resourecheck)
                    tagger = self.taggers[resourecheck]
                    resource_arn = resource_id

        if tagger:
            tagger.tag(resource_arn, tags)
        else:
            print("Tagging is not support for this resource %s" % resource_id)

    def _parse_arn(self, resource_arn):
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

class MultipleResourceTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None, tag_volumes=False):
        # print(resourcetype)
        # print(verbose)
        self.tagger = SingleResourceTagger(dryrun, verbose, role=role, region=region, resourcetype=resourcetype, tag_volumes=tag_volumes)

    def tag(self, resource_ids, tags):
        for resource_id in resource_ids:
            self.tagger.tag(resource_id, tags)

class CSVResourceTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None, tag_volumes=False):
        self.dryrun = dryrun
        self.verbose = verbose
        self.tag_volumes = tag_volumes
        self.role = role
        self.region = region
        self.regional_tagger = {}
        self.resource_id_column = 'Id'
        self.region_column = 'Region'

    def tag(self, filename):
        with open(filename, 'rU') as csv_file:
            reader = csv.reader(csv_file)
            header_row = True
            tag_index = None

            for row in reader:
                if header_row:
                    header_row = False
                    tag_index = self._parse_header(row)
                else:
                    self._tag_resource(tag_index, row)

    def _parse_header(self, header_row):
        tag_index = {}
        for index, name in enumerate(header_row):
            tag_index[name] = index

        return tag_index

    def _tag_resource(self, tag_index, row):
        resource_id = row[tag_index[self.resource_id_column]]
        tags = {}
        for (key, index) in tag_index.items():
            value = row[index]
            if key != self.resource_id_column and key != self.region_column and value != "":
                tags[key] = value

        tagger = self._lookup_tagger(tag_index, row)
        tagger.tag(resource_id, tags)

    def _lookup_tagger(self, tag_index, row):
        region = self.region
        region_index = tag_index.get(self.region_column)

        if region_index is not None:
            region = row[region_index]
        if region == '':
            region = None

        tagger = self.regional_tagger.get(region)
        if tagger is None:
            tagger = SingleResourceTagger(self.dryrun, self.verbose, role=self.role, region=region, tag_volumes=self.tag_volumes)
            self.regional_tagger[region] = tagger

        return tagger