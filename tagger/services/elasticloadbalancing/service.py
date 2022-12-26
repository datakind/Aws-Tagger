from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class LBTagger(object):
    def __init__(self, dryrun, verbose, servicetype, accesskey, secretaccesskey, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.servicetype = servicetype
        self.elb = _client('elb', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.alb = _client('elbv2', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', accesskey=self.accesskey, secretaccesskey=self.secretaccesskey, role=role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "elasticloadbalancing"
        if self.servicetype == 'ElasticLoadBalancingLoadBalancer':
            resource_arn = "loadbalancer/"+resource_arn

        if self.servicetype == 'ElasticLoadBalancingV2LoadBalancer':
            resource_arn = "loadbalancer/app/"+resource_arn

        if self.servicetype == 'ElasticLoadBalancingV2TargetGroup':
            resource_arn = "targetgroup/"+resource_arn

        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)

        if self.verbose:
            print("tagging %s with %s" % (resource_arn, _format_dict(tags)))
        if not self.dryrun:
            try:
                if self.servicetype == "ElasticLoadBalancingV2LoadBalancer" or \
                    self.servicetype == "ElasticLoadBalancingV2TargetGroup":
                    self._alb_add_tags(ResourceArns=[file_system_id], Tags=aws_tags)
                else:
                    self._elb_add_tags(LoadBalancerNames=[file_system_id], Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['LoadBalancerNotFound']:
                    print("LB Resource not found: %s" % resource_arn)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _elb_add_tags(self, **kwargs):
        return self.elb.add_tags(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _alb_add_tags(self, **kwargs):
        return self.alb.add_tags(**kwargs)