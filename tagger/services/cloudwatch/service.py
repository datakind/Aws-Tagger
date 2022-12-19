from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception
import botocore
from retrying import retry

class CloudWatchLogsTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.logs= _client('logs', role=role, region=region)

    def tag(self, resource_arn, tags):
        if self.verbose:
            print("tagging %s with %s" % (resource_arn, _format_dict(tags)))
        log_group = None
        parts = resource_arn.split(':')
        if len(parts) > 0:
            log_group = parts[-1]

        if not log_group:
            print("Invalid ARN format for CloudWatch Logs: %s" % resource_arn)
            return

        if not self.dryrun:
            try:
                self._logs_tag_log_group(logGroupName=log_group, tags=tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['ResourceNotFoundException']:
                    print("CWL Resource not found: %s" % resource_arn)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _logs_tag_log_group(self, **kwargs):
        return self.logs.tag_log_group(**kwargs)