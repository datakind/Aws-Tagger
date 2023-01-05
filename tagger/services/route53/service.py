from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class Route53Tagger(object):
    def __init__(self, dryrun, verbose, servicetype, accesskey, secretaccesskey, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.region = region
        self.servicetype = servicetype
        self.route53 = _client('route53', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        self.route53domains = _client('route53domains', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        aws_tags = _dict_to_aws_tags(tags)
        if self.servicetype == 'Route53HealthCheck':
            aws_tags = _dict_to_aws_tags(tags)
            print(aws_tags)
            if self.verbose:
                print("tagging %s with %s" % (", ".join(resource_arn), _format_dict(tags)))
            if not self.dryrun:
                try:
                    self._route53_create_tags(ResourceType="healthcheck",ResourceId=resource_arn, AddTags=aws_tags)
                except botocore.exceptions.ClientError as exception:
                    if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                        print("Resource not found: %s" % resource_arn)
                    else:
                        raise exception

        elif self.servicetype == 'Route53HostedZone':
            aws_tags = _dict_to_aws_tags(tags)
            print(aws_tags)
            if self.verbose:
                print("tagging %s with %s" % (", ".join(resource_arn), _format_dict(tags)))
            if not self.dryrun:
                try:
                    self._route53_create_tags(ResourceType="hostedzone",ResourceId=resource_arn, AddTags=aws_tags)
                except botocore.exceptions.ClientError as exception:
                    if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                        print("Resource not found: %s" % resource_arn)
                    else:
                        raise exception

        elif self.servicetype == 'Route53Domain':
            if self.verbose:
                print("tagging %s with %s" % (", ".join(resource_arn), _format_dict(tags)))
            if not self.dryrun:
                try:
                    self._route53domains_create_tags(DomainName=resource_arn, TagsToUpdate=aws_tags)
                except botocore.exceptions.ClientError as exception:
                    if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                        print("Resource not found: %s" % resource_arn)
                    else:
                        raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _route53_create_tags(self, **kwargs):
        return self.route53.change_tags_for_resource(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _route53domains_create_tags(self, **kwargs):
        return self.route53domains.update_tags_for_domain(**kwargs)