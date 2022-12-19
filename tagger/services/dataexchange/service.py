from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception
import botocore
from retrying import retry

class dataexchangeTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.ami = _client('ec2', role=role, region=region)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._ami_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _ami_create_tags(self, **kwargs):
        return self.ami.create_tags(**kwargs)