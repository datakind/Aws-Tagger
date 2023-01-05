from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3

class CloudformationStackTagger(object):
    def __init__(self, dryrun, verbose, accesskey, secretaccesskey, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.region = region
        self.cloudformationstack = _client('cloudformation', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    def tag(self, resource_arn, tags,role=None, region=None):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', accesskey=self.accesskey, secretaccesskey=self.secretaccesskey, role=role, region=self.region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = "cloudformation"
        resource_arn = "stack/"+resource_arn
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        aws_tags = _dict_to_aws_tags(tags)

        if self.verbose:
            print("tagging %s with %s" % (file_system_id, _format_dict(tags)))
        if not self.dryrun:
            try:
                # stackdata = self.cloudformationstack.describe_stacks(StackName=file_system_id)
                # stacktemplate = self.cloudformationstack.get_template(StackName=file_system_id)
                # stackdata["Stacks"][0]["TemplateBody"] = str(stacktemplate["TemplateBody"])
                # stackdata["Stacks"][0].pop("StackId", None)
                # stackdata["Stacks"][0].pop("Description", None)
                # stackdata["Stacks"][0].pop("CreationTime", None)
                # stackdata["Stacks"][0].pop("StackStatus", None)
                # stackdata["Stacks"][0].pop("EnableTerminationProtection", None)
                # stackdata["Stacks"][0].pop("DriftInformation", None)
                # stackdata["Stacks"][0].pop("ParentId", None)
                # stackdata["Stacks"][0].pop("RootId", None)
                # stackdata["Stacks"][0]["UsePreviousTemplate"] = True
                # if "LastUpdatedTime" in stackdata["Stacks"][0]:
                #     stackdata["Stacks"][0].pop("LastUpdatedTime", None)
                # stackdata["Stacks"][0]["Tags"].append(aws_tags[0])
                # print(stackdata["Stacks"][0])
                self._cloudformationstack_create_tags(StackName=file_system_id,Tags=aws_tags,UsePreviousTemplate=True,)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['FileSystemNotFound']:
                    print("Cloudformation Stack not found: %s" % resource_arn)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _cloudformationstack_create_tags(self, **kwargs):
        return self.cloudformationstack.update_stack(**kwargs)