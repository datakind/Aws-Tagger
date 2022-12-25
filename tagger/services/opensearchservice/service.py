from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _name_to_arn
import botocore
from retrying import retry
import boto3
import os

class opensearchserviceTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.role = role
<<<<<<< HEAD
        self.region = region
        self.opensearch = _client('opensearch', role=role, region=region)
=======
        self.openSearch = _client('opensearch', role=role, region=region)
>>>>>>> b4241d0c6fab1706490bc7406b5ec592b4061313

    def tag(self, resource_arn, tags):
        my_session = boto3.session.Session()
        region = my_session.region_name

        self.sts = _client('sts', role=self.role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = 'es'
        resource_arn = f'domain/{resource_arn}'
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)
        aws_tags = _dict_to_aws_tags(tags)
<<<<<<< HEAD
        
=======
        print(aws_tags)
        resource_ids = [instance_id]
        # Get Domain ARN of OpenSearchService Resource
        region = os.environ.get("AWS_REGION")
        self.sts = _client('sts', role=self.role, region=region)
        account_id = self.sts.get_caller_identity()["Account"]
        service = 'es'
        resource_arn = f'domain/{resource_ids[0]}'
        
        
        file_system_id = _name_to_arn(resource_name=resource_arn,region=region,service=service,account_id=account_id)

        print(file_system_id)

>>>>>>> b4241d0c6fab1706490bc7406b5ec592b4061313
        if self.verbose:
            print("tagging %s with %s" % (", ".join(file_system_id), _format_dict(tags)))
        if not self.dryrun:
            try:
<<<<<<< HEAD
                self._opensearch_create_tags(ARN=file_system_id, TagList=aws_tags)
=======
                self._opensearch_add_tags(ARN=resource_ids[0], TagList=aws_tags)
>>>>>>> b4241d0c6fab1706490bc7406b5ec592b4061313
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("Resource not found: %s" % file_system_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
<<<<<<< HEAD
    def _opensearch_create_tags(self, **kwargs):
        return self.opensearch.add_tags(**kwargs)
=======
    def _opensearch_add_tags(self, **kwargs):
        return self.openSearch.add_tags(**kwargs)
        arn:aws:es:us-west-2:630730735895:domain/helgesontestdomainone

        arn:aws:es:us-west-2:630730735895:domain/helgesontestdomainone
>>>>>>> b4241d0c6fab1706490bc7406b5ec592b4061313
