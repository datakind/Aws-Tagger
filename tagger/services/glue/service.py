from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception
import botocore
from retrying import retry

# NOTE: Glue role tagging implementation is currently incomplete.

# NOTE: boto3.client('glue').tag_resource may require role to 
# be explicitly defined. For now, we require passing role, 
# or we raise an exception, but perhaps there is a function
# that can infer roles from a glue resource identifier
class glueRoleTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.role = role
        self.region = region
        self.glue = _client('glue', role=role, region=region)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        print('Glue Resource_ids')
        print(resource_ids)
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.role: 
          roleClient = _client('iam', role=self.role, region=self.region)
          print("List role policies: ")
          rolePolicies = roleClient.list_role_policies(RoleName=resource_ids[0])
          print(rolePolicies)
          print("Get Role")
          print(roleClient.get_role(RoleName=resource_ids[0]))
          print(roleClient.get_role_policy(RoleName=resource_ids[0], PolicyName="glue.amazonaws.com"))
          raise exception
          print(
            f'Tagging glue Resource {resource_ids} currently requires user to pass in a role\n' +
            f'For example: "aws-tagger --role arn:aws:iam:111111111:role/MyRole --resource <RESOURCE_IDENTIFIER> --tag <YOUR_TAG>'
          )
        
        if not self.dryrun:
            try:
                self._glue_tag_resource(ResourceArn=self.role, TagsToAdd=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _glue_tag_resource(self, **kwargs):
        return self.glue.tag_resource(**kwargs)

'''class InstanceProfileTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.instanceprofile = _client('iam', role=role, region=region)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._InstanceProfile_create_tags(InstanceProfileName=resource_ids[0], TagsToAdd=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("IAM Instance Profile not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _describe_InstanceProfile(self, **kwargs):
        return self.instanceprofile.list_instance_profiles(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _InstanceProfile_create_tags(self, **kwargs):
        # return self.instanceprofile.tag_instance_profile(**kwargs)
        return self.instanceprofile.tag_instance_profile(**kwargs)
'''