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
        arnstring = "arn:aws:"+service+"::"+account_id+":"+resource_name
        return arnstring

def _fetch_temporary_credentials(role):
    sts = boto3.client('sts', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

    response = sts.assume_role(RoleArn=role, RoleSessionName='aws-tagger.%s' % socket.gethostname())
    access_key_id = response.get('Credentials', {}).get('AccessKeyId', None)
    secret_access_key = response.get('Credentials', {}).get('SecretAccessKey', None)
    session_token = response.get('Credentials', {}).get('SessionToken', None)
    return access_key_id, secret_access_key, session_token
    
def _client(name, role, region):
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

    return boto3.client(name, **kwargs)