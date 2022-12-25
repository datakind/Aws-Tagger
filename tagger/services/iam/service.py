from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry

class IamTagger(object):
    def __init__(self, dryrun, verbose, servicetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.servicetype = servicetype
        self.instanceprofile = _client('iam', role=role, region=region)
    
    def tag(self, resource_arn, tags):
        region = None
        self.sts = _client('sts', role=None, region=None)
        account_id = self.sts.get_caller_identity()["Account"]

        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        service = "iam"
        if self.servicetype == 'IAMInstanceProfile':
            if self.verbose:
                print("tagging %s with %s" % (", ".join(resource_arn), _format_dict(tags)))
            if not self.dryrun:
                try:
                    self._InstanceProfile_create_tags(InstanceProfileName=resource_arn, TagsToAdd=aws_tags)
                except botocore.exceptions.ClientError as exception:
                    if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                        print("IAM Instance Profile not found: %s" % resource_arn)
                    else:
                        raise exception
        elif self.servicetype == 'IAMSAMLProvider':
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
        elif self.servicetype == 'IAMManagedPolicy':
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
        elif self.servicetype == 'IAMOpenIDConnectProvider':
            resource_arn = "oidc-provider/"+resource_arn
            file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)

            aws_tags = _dict_to_aws_tags(tags)

            if self.verbose:
                print("tagging %s with %s" % (file_system_id, _format_dict(tags)))
            if not self.dryrun:
                try:
                    self._openidconnect_create_tags(OpenIDConnectProviderArn=file_system_id, Tags=aws_tags)
                except botocore.exceptions.ClientError as exception:
                    if exception.response["Error"]["Code"] in ['FileSystemNotFound']:
                        print("IAM Managed Profile not found: %s" % file_system_id)
                    else:
                        raise exception
        elif self.servicetype == 'IAMServerCertificate':
            if self.verbose:
                print("tagging %s with %s" % (", ".join(resource_arn), _format_dict(tags)))
            if not self.dryrun:
                try:
                    self._servercertificate_create_tags(ServerCertificateName=resource_arn, Tags=aws_tags)
                except botocore.exceptions.ClientError as exception:
                    if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                        print("IAM Instance Profile not found: %s" % resource_arn)
                    else:
                        raise exception
    
    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _InstanceProfile_create_tags(self, **kwargs):
        return self.instanceprofile.tag_instance_profile(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _ManagedPolicy_create_tags(self, **kwargs):
        return self.ManagedPolicy.tag_policy(**kwargs)
    
    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _samlprovider_create_tags(self, **kwargs):
        return self.samlprovider.tag_saml_provider(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _openidconnect_create_tags(self, **kwargs):
        return self.instanceprofile.tag_open_id_connect_provider(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _servercertificate_create_tags(self, **kwargs):
        return self.instanceprofile.tag_server_certificate(**kwargs)
