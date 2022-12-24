from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class CloudWatchTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.cloudwatch= _client('cloudwatch', role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', role=role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "cloudwatch"
        resource_arn = "alarm:"+resource_arn
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)

        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        if self.verbose:
            print("tagging %s with %s" % (", ".join(file_system_id), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._cloudwatch_tag_log_group(ResourceARN=file_system_id, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['ResourceNotFoundException']:
                    print("CWL Resource not found: %s" % resource_arn)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _cloudwatch_tag_log_group(self, **kwargs):
        return self.cloudwatch.tag_resource(**kwargs)