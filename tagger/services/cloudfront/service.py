from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception
import botocore
from retrying import retry

class CloudfrontTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.cloudfront = _client('cloudfront', role=role, region=region)

    def tag(self, resource_arn, tags):
        aws_tags = _dict_to_aws_tags(tags)
        if self.verbose:
            print("tagging %s with %s" % (resource_arn, _format_dict(tags)))
        if not self.dryrun:
            try:
                self._cloudfront_tag_resource(Resource=resource_arn, Tags={'Items': aws_tags})
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['NoSuchResource']:
                    print("CloudFront Resource not found: %s" % resource_arn)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _cloudfront_tag_resource(self, **kwargs):
        return self.cloudfront.tag_resource(**kwargs)