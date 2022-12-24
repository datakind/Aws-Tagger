from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class DynamoDBTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.role = role
        self.region = region
        self.dynamodb = _client('dynamodb', role=role, region=region)

    def tag(self, resource_arn, tags):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', role=self.role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = 'dynamodb'
        resource_arn = f'table/{resource_arn}'
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        aws_tags = _dict_to_aws_tags(tags)
        
        if self.verbose:
            print("tagging %s with %s" % (", ".join(file_system_id), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._dynamodb_create_tags(ResourceArn=file_system_id, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("Resource not found: %s" % file_system_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _dynamodb_create_tags(self, **kwargs):
        return self.dynamodb.tag_resource(**kwargs)