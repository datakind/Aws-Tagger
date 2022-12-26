from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class CloudfrontTagger(object):
    def __init__(self, dryrun, verbose, servicetype, accesskey, secretaccesskey, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.servicetype = servicetype
        self.cloudfront = _client('cloudfront', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        self.sts = _client('sts', accesskey=self.accesskey, secretaccesskey=self.secretaccesskey, role=role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "cloudfront"
        if self.servicetype == 'CloudFrontStreamingDistribution':
            resource_arn = "streamingdistribution/"+resource_arn

        if self.servicetype == 'CloudFrontDistribution':
            resource_arn = "distribution/"+resource_arn
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)

        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        if self.verbose:
            print("tagging %s with %s" % (file_system_id, _format_dict(tags)))
        if not self.dryrun:
            try:
                self._cloudfront_tag_resource(Resource=file_system_id, Tags={'Items': aws_tags})
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['NoSuchResource']:
                    print("CloudFront Resource not found: %s" % file_system_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _cloudfront_tag_resource(self, **kwargs):
        return self.cloudfront.tag_resource(**kwargs)