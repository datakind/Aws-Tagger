from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _arn_to_name
import botocore
from retrying import retry

class LBTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.elb = _client('elb', role=role, region=region)
        self.alb = _client('elbv2', role=role, region=region)

    def tag(self, resource_arn, tags):
        aws_tags = _dict_to_aws_tags(tags)

        if self.verbose:
            print("tagging %s with %s" % (resource_arn, _format_dict(tags)))
        if not self.dryrun:
            try:
                if ':loadbalancer/app/' in resource_arn:
                    self._alb_add_tags(ResourceArns=[resource_arn], Tags=aws_tags)
                else:
                    elb_name = _arn_to_name(resource_arn)
                    self._elb_add_tags(LoadBalancerNames=[elb_name], Tags=aws_tags)
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