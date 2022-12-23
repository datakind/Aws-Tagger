import os
import boto3
import botocore
from retrying import retry
import tagger.services as tagservices
import socket
import csv
from . import sconfig
from . import tagsearch

#tagservices.appstream.service.AppstreamTagger
    
    
class SingleResourceTagger(object):
    # Init each tagger lazy
    # https://zhaoxh.cn/en/post/2018/lazy-load-dict/
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None, tag_volumes=False):
        self.taggers = {}
        # EC2 Resources
        self.taggers['ec2'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ec2', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['ami'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ami', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['dopt'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'dopt', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['igw'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'igw', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['acl'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'acl', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['igw'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'igw', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['eni'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'eni', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['rtb'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'rtb', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['sg'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'sg', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['subnet'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'subnet', role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['vpc'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'vpc', role=role, region=region, tag_volumes=tag_volumes)
        
        # Organization resources
        self.taggers['organization'] = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, role=role, region=region)
        
        # Elastic File System resources
        self.taggers['elasticfilesystem'] = tagservices.efs.service.EFSTagger(dryrun, verbose, role=role, region=region)
        self.taggers['GlacierVault'] = tagservices.glacier.service.glacierTagger(dryrun, verbose, role=role, region=region)

        # Other resources currently
        self.taggers['rds'] = tagservices.rds.service.RDSTagger(dryrun, verbose, role=role, region=region)
        self.taggers['elasticloadbalancing'] = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, role=role, region=region)
        self.taggers['elasticbenstalkapp'] = tagservices.elasticbeanstalk.service.EBSATagger(dryrun, verbose, role=role, region=region)
        self.taggers['resourcegroup'] = tagservices.resourcegroups.service.ResourceGroupTagger(dryrun, verbose, role=role, region=region)
        self.taggers['snstopic'] = tagservices.sns.service.SNSTopicTagger(dryrun, verbose, role=role, region=region)
        self.taggers['cloudformationstack'] = tagservices.cloudformation.service.CloudformationStackTagger(dryrun, verbose, role=role, region=region)
        self.taggers['secretsmanagersecret'] = tagservices.secretsmanager.service.SecretManagerSecretTagger(dryrun, verbose, role=role, region=region)
        self.taggers['sagemakernotebookinstance'] = tagservices.sagemaker.service.SagemakerNotebookInstanceTagger(dryrun, verbose, role=role, region=region)
        self.taggers['elasticache'] = tagservices.elasticcache.service.ElasticacheTagger(dryrun, verbose, role=role, region=region)
        self.taggers['instanceprofile'] = tagservices.iam.service.InstanceProfileTagger(dryrun, verbose, role=role, region=region)
        self.taggers['route53hostedzone'] = tagservices.route53.service.Route53HostedZoneTagger(dryrun, verbose, role=role, region=region)
        self.taggers['managedpolicy'] = tagservices.iam.service.ManagedPolicyTagger(dryrun, verbose, role=role, region=region)
        self.taggers['samlprovider'] = tagservices.iam.service.SamlProviderTagger(dryrun, verbose, role=role, region=region)
        self.taggers['s3'] = tagservices.s3.service.S3Tagger(dryrun, verbose, role=role, region=region)
        self.taggers['es'] = tagservices.es.service.ESTagger(dryrun, verbose, role=role, region=region)
        self.taggers['kinesis'] = tagservices.kinesis.service.KinesisTagger(dryrun, verbose, role=role, region=region)
        self.taggers['cloudfront'] = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, role=role, region=region)
        self.taggers['logs'] = tagservices.cloudwatch.service.CloudWatchLogsTagger(dryrun, verbose, role=role, region=region)
        self.taggers['dynamodb'] = tagservices.dynamodb.service.DynamoDBTagger(dryrun, verbose, role=role, region=region)
        self.taggers['lambda'] = tagservices.awslambda.service.LambdaTagger(dryrun, verbose, role=role, region=region)
        self.taggers['redshiftclusergroup'] = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, role=role, region=region)
        self.taggers['GlueRole'] = tagservices.glue.service.glueRoleTagger(dryrun, verbose, role=role, region=region)

    def tag(self, resource_id, resourcetype, tags, role=None, region=None):
        print(
          f'Resource Identifier: {resource_id}\n' +
          f'Resource Type: {(resourcetype, "Unknown") [resourcetype == None]}\n' +
          f'tags: {tags}'
        )
        if resource_id == "":
            return

        if len(tags) == 0:
            return

        tagger = None
        if resourcetype == None:
            searchresult = sconfig.resourcesearch(self.taggers,resource_id,role,region)
            tagger = searchresult[1]
            resource_arn = searchresult[0]
        else:
            print(resourcetype)
            # TODO: Comment below out if non-functional
            searchresult = tagsearch.checkresource(resourcetype)
            if self.taggers.get(resourcetype) == None:
              #TODO: Do something if tagger does not exist in code
              # Perhaps throwing an exception
              tagger = self.taggers['GlacierVault']
            else: 
              tagger = self.taggers[resourcetype]
            print(searchresult)
            # tagger = self.taggers['GlacierVault']
            resource_arn = resource_id
            # tagger = searchresult[1]
            # resource_arn = searchresult[0]
            # add function for resourcetypechecker
            pass
        if tagger:
            tagger.tag(resource_arn, tags)
        else:
            print("Tagging is not support for this resource %s" % resource_id)

    def _parse_arn(self, resource_arn):
        product = None
        resource_id = None
        parts = resource_arn.split(':')
        if len(parts) > 5:
            product = parts[2]
            resource_id = parts[5]
            resource_parts = resource_id.split('/')
            if len(resource_parts) > 1:
                resource_id = resource_parts[-1]

        return product, resource_id

class MultipleResourceTagger(object):
    def __init__(self, dryrun, verbose, resourcetype, role=None, region=None, tag_volumes=False):
        self.tagger = SingleResourceTagger(dryrun, verbose, role=role, region=region, resourcetype=resourcetype, tag_volumes=tag_volumes)

    def tag(self, resource_ids, resourcetype, tags):
        for resource_id in resource_ids:
            self.tagger.tag(resource_id, resourcetype, tags)

class CSVResourceTagger(object):
    def __init__(self, dryrun, verbose, role=None, region=None, tag_volumes=False):
        self.dryrun = dryrun
        self.verbose = verbose
        self.tag_volumes = tag_volumes
        self.role = role
        self.region = region
        self.regional_tagger = {}
        self.resource_id_column = 'Id'
        self.region_column = 'Region'

    def tag(self, filename):
        with open(filename, 'rU') as csv_file:
            reader = csv.reader(csv_file)
            header_row = True
            tag_index = None

            for row in reader:
                if header_row:
                    header_row = False
                    tag_index = self._parse_header(row)
                else:
                    self._tag_resource(tag_index, row)

    def _parse_header(self, header_row):
        tag_index = {}
        for index, name in enumerate(header_row):
            tag_index[name] = index

        return tag_index

    def _tag_resource(self, tag_index, row):
        resource_id = row[tag_index[self.resource_id_column]]
        tags = {}
        for (key, index) in tag_index.items():
            value = row[index]
            if key != self.resource_id_column and key != self.region_column and value != "":
                tags[key] = value

        tagger = self._lookup_tagger(tag_index, row)
        tagger.tag(resource_id, tags)

    def _lookup_tagger(self, tag_index, row):
        region = self.region
        region_index = tag_index.get(self.region_column)

        if region_index is not None:
            region = row[region_index]
        if region == '':
            region = None

        tagger = self.regional_tagger.get(region)
        if tagger is None:
            tagger = SingleResourceTagger(self.dryrun, self.verbose, role=self.role, region=region, tag_volumes=self.tag_volumes)
            self.regional_tagger[region] = tagger

        return tagger