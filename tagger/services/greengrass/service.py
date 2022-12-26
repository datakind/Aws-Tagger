from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class greengrassTagger(object):
    def __init__(self, dryrun, verbose, servicetype, accesskey, secretaccesskey, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.servicetype = servicetype
        self.greengrass = _client('greengrass', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', accesskey=self.accesskey, secretaccesskey=self.secretaccesskey, role=role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "greengrass"
        if self.servicetype == 'GreengrassConnectorDefinition':
            resource_arn = "/greengrass/definition/connectors/"+resource_arn

        if self.servicetype == 'GreengrassCoreDefinition':
            resource_arn = "/greengrass/definition/cores/"+resource_arn

        if self.servicetype == 'GreengrassDeviceDefinition':
            resource_arn = "/greengrass/definition/devices/"+resource_arn

        if self.servicetype == 'GreengrassFunctionDefinition':
            resource_arn = "/greengrass/definition/functions/"+resource_arn

        if self.servicetype == 'GreengrassGroup':
            resource_arn = "/greengrass/groups/"+resource_arn

        if self.servicetype == 'GreengrassLoggerDefinition':
            resource_arn = "/greengrass/definition/loggers/"+resource_arn

        if self.servicetype == 'GreengrassResourceDefinition':
            resource_arn = "/greengrass/definition/resources/"+resource_arn

        if self.servicetype == 'GreengrassSubscriptionDefinition':
            resource_arn = "/greengrass/definition/subscriptions/"+resource_arn

        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        if self.verbose:
            print("tagging %s with %s" % (", ".join(file_system_id), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._greengrass_create_tags(ResourceArn=file_system_id, tags=tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("Resource not found: %s" % file_system_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _greengrass_create_tags(self, **kwargs):
        return self.greengrass.tag_resource(**kwargs)