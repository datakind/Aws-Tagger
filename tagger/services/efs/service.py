from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _arn_to_name
import botocore
from retrying import retry

class EFSTagger(object):
    def __init__(self, dryrun, verbose, accesskey, secretaccesskey, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.efs = _client('efs', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    def tag(self, resource_arn, tags):
        file_system_id = _arn_to_name(resource_arn)
        aws_tags = _dict_to_aws_tags(tags)

        if self.verbose:
            print("tagging %s with %s" % (file_system_id, _format_dict(tags)))
        if not self.dryrun:
            try:
                self._efs_create_tags(FileSystemId=file_system_id, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['FileSystemNotFound']:
                    print("EFS Resource not found: %s" % resource_arn)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _efs_create_tags(self, **kwargs):
        return self.efs.create_tags(**kwargs)