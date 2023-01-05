from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3


class braketTagger(object):
    def __init__(self, dryrun, verbose, accesskey, secretaccesskey, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.region = region
        self.braket = _client('braket', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):

        self.sts = _client('sts', accesskey=self.accesskey, secretaccesskey=self.secretaccesskey, role=role, region=self.region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "braket"
        resource_arn = "device/quantum-simulator/amazon/"+resource_arn

        file_system_id = _name_to_arn(resource_name=file_system_id,region=region,service=service,account_id=account_id)
    
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)

        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_arn), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._braket_create_tags(Resources=resource_arn, Tags=tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("Resource not found: %s" % resource_arn)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _braket_create_tags(self, **kwargs):
        return self.braket.tag_resource(**kwargs)