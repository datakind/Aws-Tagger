from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class ESTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.es = _client('es', role=role, region=region)

    def tag(self, resource_arn, tags):
        aws_tags = _dict_to_aws_tags(tags)
        if self.verbose:
            print("tagging %s with %s" % (resource_arn, _format_dict(tags)))
        if not self.dryrun:
            try:
                self._es_add_tags(ARN=resource_arn, TagList=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['ValidationException']:
                    print("ES Resource not found: %s" % resource_arn)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _es_add_tags(self, **kwargs):
        return self.es.add_tags(**kwargs)