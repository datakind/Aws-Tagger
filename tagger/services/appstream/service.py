from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class appstreamTagger(object):
    def __init__(self, dryrun, verbose, servicetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.servicetype = servicetype
        self.appstream = _client('appstream', role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', role=role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "appstream"
        if self.servicetype == 'AppstreamFleet':
            resource_arn = "fleet/"+resource_arn

        if self.servicetype == 'AppstreamImageBulder':
            resource_arn = "appstreamimagebulder/"+resource_arn

        if self.servicetype == 'AppstreamImageStack':
            resource_arn = "appstreamimagestack/"+resource_arn
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        print(file_system_id)
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        if self.verbose:
            print("tagging %s with %s" % (", ".join(file_system_id), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._appstream_create_tags(ResourceArn=file_system_id, Tags=tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("Resource not found: %s" % file_system_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _appstream_create_tags(self, **kwargs):
        return self.appstream.tag_resource(**kwargs)