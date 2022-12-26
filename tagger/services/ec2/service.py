from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class EC2Tagger(object):
    def __init__(self, dryrun, verbose, servicetype, accesskey, secretaccesskey, role=None, region=None, tag_volumes=False):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey

        self.ec2 = _client('ec2', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.servicetype = servicetype
        if self.servicetype == 'ec2':
            self.volume_cache = {}
            if tag_volumes:
                self.add_volume_cache()

    def add_volume_cache(self):
        #TODO implement paging for describe instances
        reservations = self._ec2_describe_instances(MaxResults=1000)

        for reservation in reservations["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance['InstanceId']
                volumes = instance.get('BlockDeviceMappings', [])
                self.volume_cache[instance_id] = []
                for volume in volumes:
                    ebs = volume.get('Ebs', {})
                    volume_id = ebs.get('VolumeId')
                    if volume_id:
                        self.volume_cache[instance_id].append(volume_id)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.servicetype == 'ec2':
            resource_ids.extend(self.volume_cache.get(instance_id, []))
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._ec2_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print(str(self.servicetype)+" resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _ec2_describe_instances(self, **kwargs):
        return self.ec2.describe_instances(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _ec2_create_tags(self, **kwargs):
        return self.ec2.create_tags(**kwargs)