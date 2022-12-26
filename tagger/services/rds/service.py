from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class RDSTagger(object):
    def __init__(self, dryrun, verbose, servicetype, accesskey, secretaccesskey, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.servicetype = servicetype
        self.rds = _client('rds', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', accesskey=self.accesskey, secretaccesskey=self.secretaccesskey, role=role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "rds"
        if self.servicetype == 'RDSDBCluster':
            resource_arn = "cluster:"+resource_arn

        if self.servicetype == 'RDSDBClusterParameterGroup':
            resource_arn = "cluster-pg:"+resource_arn

        if self.servicetype == 'RDSDBInstance':
            resource_arn = "db:"+resource_arn

        if self.servicetype == 'RDSDBClusterSnapshot':
            resource_arn = "cluster-snapshot:"+resource_arn

        if self.servicetype == 'RDSDBParameterGroup':
            resource_arn = "pg:"+resource_arn

        if self.servicetype == 'RDSDBSecurityGroup':
            resource_arn = "secgrp:"+resource_arn

        if self.servicetype == 'RDSDBSnapshot':
            resource_arn = "snapshot:"+resource_arn

        if self.servicetype == 'RDSDBSubnetGroup':
            resource_arn = "subgrp:"+resource_arn

        if self.servicetype == 'RDSEventSubscription':
            resource_arn = "es:"+resource_arn

        if self.servicetype == 'RDSOptionGroup':
            resource_arn = "og:"+resource_arn

        if self.servicetype == 'RDSReservedDBInstance':
            resource_arn = "ri:"+resource_arn

        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        if self.verbose:
            print("tagging %s with %s" % (", ".join(file_system_id), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._rds_create_tags(ResourceArn=file_system_id, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("Resource not found: %s" % file_system_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _rds_create_tags(self, **kwargs):
        return self.rds.add_tags_to_resource(**kwargs)