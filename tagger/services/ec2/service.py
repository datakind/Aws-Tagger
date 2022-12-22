from tagger.sconfig import _client, _dict_to_aws_tags, _format_dict, _is_retryable_exception
import botocore
from retrying import retry

class EC2Tagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None, tag_volumes=False):
        self.dryrun = dryrun
        self.verbose = verbose

        self.ec2 = _client('ec2', role=role, region=region)
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
        resource_ids.extend(self.volume_cache.get(instance_id, []))
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._ec2_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("EC2 Resource not found: %s" % instance_id)
                else:
                    raise exception


    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _ec2_describe_instances(self, **kwargs):
        return self.ec2.describe_instances(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _ec2_create_tags(self, **kwargs):
        return self.ec2.create_tags(**kwargs)

class AMITagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None):
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
                    print("EC2 AMI Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _ami_describe_instances(self, **kwargs):
        return self.ami.describe_images(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _ami_create_tags(self, **kwargs):
        return self.ami.create_tags(**kwargs)

class DHCPOTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.dopt = _client('ec2', role=role, region=region)
    
    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._dhcp_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("EC2 DHCP Option Resource not found: %s" % instance_id)
                else:
                    raise exception


    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _describe_dhcp_options(self, **kwargs):
        return self.dopt.describe_dhcp_options(**kwargs)
    
    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _dhcp_create_tags(self, **kwargs):
        return self.dopt.create_tags(**kwargs)

class InternetGatewayTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.igw = _client('ec2', role=role, region=region)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._dhcp_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("EC2 Internet Gateway Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _describe_InternetGateway(self, **kwargs):
        return self.igw.describe_internet_gateways(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _dhcp_create_tags(self, **kwargs):
        return self.igw.create_tags(**kwargs)

class NetworkAclTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.acl = _client('ec2', role=role, region=region)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._NetworkAcl_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("EC2 Network ACL Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _describe_NetworkAcl(self, **kwargs):
        return self.acl.describe_network_acls(**kwargs)
        
    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _NetworkAcl_create_tags(self, **kwargs):
        return self.acl.create_tags(**kwargs)

class NetworkInterfaceTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.eni = _client('ec2', role=role, region=region)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._NetworkInterface_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("EC2 Network Interface Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _describe_NetworkInterface(self, **kwargs):
        return self.eni.describe_network_interfaces(**kwargs)
    
    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _NetworkInterface_create_tags(self, **kwargs):
        return self.eni.create_tags(**kwargs)

class RouteTableTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.rtb = _client('ec2', role=role, region=region)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._RouteTable_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("EC2 Route Table Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _describe_RouteTable(self, **kwargs):
        return self.rtb.describe_route_tables(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _RouteTable_create_tags(self, **kwargs):
        return self.rtb.create_tags(**kwargs)

class SecurityGroupTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.sg = _client('ec2', role=role, region=region)
    
    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._SecurityGroup_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("EC2 Security Group Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _describe_SecurityGroup(self, **kwargs):
        return self.sg.describe_security_groups(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _SecurityGroup_create_tags(self, **kwargs):
        return self.sg.create_tags(**kwargs)

class SubnetTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.subnet = _client('ec2', role=role, region=region)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._Subnet_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("EC2 Subnet Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _describe_Subnet(self, **kwargs):
        return self.subnet.describe_subnets(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _Subnet_create_tags(self, **kwargs):
        return self.subnet.create_tags(**kwargs)

class VPCTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None):
        self.dryrun = dryrun
        self.verbose = verbose
        self.vpc = _client('ec2', role=role, region=region)

    def tag(self, instance_id, tags):
        aws_tags = _dict_to_aws_tags(tags)
        print(aws_tags)
        resource_ids = [instance_id]
        if self.verbose:
            print("tagging %s with %s" % (", ".join(resource_ids), _format_dict(tags)))
        if not self.dryrun:
            try:
                self._VPC_create_tags(Resources=resource_ids, Tags=aws_tags)
            except botocore.exceptions.ClientError as exception:
                if exception.response["Error"]["Code"] in ['InvalidSnapshot.NotFound', 'InvalidVolume.NotFound', 'InvalidInstanceID.NotFound']:
                    print("EC2 VPC Resource not found: %s" % instance_id)
                else:
                    raise exception

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _describe_VPC(self, **kwargs):
        return self.vpc.describe_vpcs(**kwargs)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=30000, wait_exponential_multiplier=1000)
    def _VPC_create_tags(self, **kwargs):
        return self.vpc.create_tags(**kwargs)