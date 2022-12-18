from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception, _arn_to_name, _aws_tags_to_dict
import botocore
from retrying import retry

class S3Tagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.s3 = _client('s3', role=role, region=region)

    def tag(self, bucket_name, tags):
        try:
            if bucket_name.startswith('arn:'):
                bucket_name = _arn_to_name(bucket_name)
            response = self._s3_get_bucket_tagging(Bucket=bucket_name)
            # add existing tags
            for (key, value) in _aws_tags_to_dict(response.get('TagSet', [])).items():
                if key not in tags:
                    tags[key] = value
        except botocore.exceptions.ClientError as exception:
            if exception.response["Error"]["Code"] not in ['NoSuchTagSet', 'NoSuchBucket']:
                raise exception

        aws_tags = _dict_to_aws_tags(tags)
        if self.verbose:
            print("tagging %s with %s" % (bucket_name, _format_dict(tags)))
        if not self.dryrun:
            try:
                self._s3_put_bucket_tagging(Bucket=bucket_name, Tagging={'TagSet': aws_tags})
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['NoSuchBucket']:
                    print("S3 Resource not found: %s" % bucket_name)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _s3_get_bucket_tagging(self, **kwargs):
        return self.s3.get_bucket_tagging(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _s3_put_bucket_tagging(self, **kwargs):
        return self.s3.put_bucket_tagging(**kwargs)