from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class RedshiftclusterGroupTagger(object):
    def __init__(self, dryrun, verbose, servicetype, accesskey, secretaccesskey, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.servicetype = servicetype
        self.redshiftcg = _client('redshift', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', accesskey=self.accesskey, secretaccesskey=self.secretaccesskey, role=role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "redshift"
        if self.servicetype == 'RedshiftCluster':
            resource_arn = "cluster:"+resource_arn
        if self.servicetype == 'RedshiftClusterSubnetGroup':
            resource_arn = "subnetgroup:"+resource_arn
        if self.servicetype == 'RedshiftHSMClientCertificate':
            resource_arn = "hsmclientcertificate:"+resource_arn
        if self.servicetype == "RedshiftParameterGroup":
            resource_arn = "parametergroup:"+resource_arn
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        aws_tags = _dict_to_aws_tags(tags)

        if self.verbose:
            print("tagging %s with %s" % (file_system_id, _format_dict(tags)))
        if not self.dryrun:
            try:
                self._redshiftcg_tag_resource(ResourceName=file_system_id, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['ResourceNotFoundException']:
                    print("Redshift Cluster Parameter Group Resource not found: %s" % resource_arn)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _redshiftcg_tag_resource(self, **kwargs):
        return self.redshiftcg.create_tags(**kwargs)