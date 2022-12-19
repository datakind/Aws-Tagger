from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry

class InstanceProfileTagger(object):
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

class ManagedPolicyTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.ManagedPolicy = _client('iam', role=role, region=region)

    def tag(self, resource_arn, tags):
        region = None

        self.sts = _client('sts', role=None, region=None)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "iam"
        resource_arn = "policy/"+resource_arn
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)

        aws_tags = _dict_to_aws_tags(tags)

        if self.verbose:
            print("tagging %s with %s" % (file_system_id, _format_dict(tags)))
        if not self.dryrun:
            try:
                self._ManagedPolicy_create_tags(PolicyArn=file_system_id, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['FileSystemNotFound']:
                    print("IAM Managed Profile not found: %s" % file_system_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _ManagedPolicy_create_tags(self, **kwargs):
        return self.ManagedPolicy.tag_policy(**kwargs)


class SamlProviderTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.samlprovider = _client('iam', role=role, region=region)

    def tag(self, resource_arn, tags):
        region = None

        self.sts = _client('sts', role=None, region=None)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "iam"
        resource_arn = "saml-provider/"+resource_arn
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)

        aws_tags = _dict_to_aws_tags(tags)

        if self.verbose:
            print("tagging %s with %s" % (file_system_id, _format_dict(tags)))
        if not self.dryrun:
            try:
                self._samlprovider_create_tags(SAMLProviderArn=file_system_id, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['FileSystemNotFound']:
                    print("IAM SAML Provider Resource not found: %s" % file_system_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _samlprovider_create_tags(self, **kwargs):
        return self.samlprovider.tag_saml_provider(**kwargs)