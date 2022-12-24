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

        # Amazon Mq Resources
        self.taggers['AmazonmqBroker'] = tagservices.mq.service.mqTagger(dryrun, verbose, 'AmazonmqBroker', role=role, region=region)
        self.taggers['AmazonmqConfiguration'] = tagservices.mq.service.mqTagger(dryrun, verbose, 'AmazonmqConfiguration', role=role, region=region)

        # Braket Resources
        self.taggers['BraketQuantumTask'] = tagservices.braket.service.braketTagger(dryrun, verbose, role=role, region=region)

        # Appstream Resources
        self.taggers['AppstreamFleet'] = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamFleet', role=role, region=region)
        self.taggers['AppstreamImageBulder'] = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamImageBulder', role=role, region=region)
        self.taggers['AppstreamImageStack'] = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamImageStack', role=role, region=region)

        # Certificate Manager
        self.taggers['CertificateManagerCertificate'] = tagservices.certificatemanager.service.certificatemanagerTagger(dryrun, verbose, role=role, region=region)

        # Cloud9 Resources
        self.taggers['Cloud9Environment'] = tagservices.cloud9.service.cloud9Tagger(dryrun, verbose, role=role, region=region)

        # Cloudfront Resources
        self.taggers['CloudFrontDistribution'] = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, 'CloudFrontDistribution', role=role, region=region)
        self.taggers['CloudFrontStreamingDistribution'] = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, 'CloudFrontStreamingDistribution', role=role, region=region)

        # CloudTrail Resources
        self.taggers['CloudTrailTrail'] = tagservices.cloudtrail.service.cloudtrailTagger(dryrun, verbose, role=role, region=region)
        
        # Cloudwatch Resources
        self.taggers['CloudWatchAlarm'] = tagservices.cloudwatch.service.CloudWatchTagger(dryrun, verbose, role=role, region=region)
        
        # CodeArtifact Resources
        self.taggers['CodeArtifactDomain'] = tagservices.cloudwatch.service.CloudWatchTagger(dryrun, verbose, "CodeArtifactDomain", role=role, region=region)
        self.taggers['CodeArtifactRepository'] = tagservices.cloudwatch.service.CloudWatchTagger(dryrun, verbose, "CodeArtifactRepository", role=role, region=region)

        # CodeCommit Resources
        self.taggers['CodeCommitRepository'] = tagservices.codecommit.service.codecommitTagger(dryrun, verbose, role=role, region=region)
        
        # CodeCommit Resources
        self.taggers['CodeGuruReviewerRepositoryAssociation'] = tagservices.codegurureviewer.service.codegurureviewerTagger(dryrun, verbose, role=role, region=region)

        # CodePipeline Resources
        self.taggers['CodePipelinePipeline'] = tagservices.codepipeline.service.codepipelineTagger(dryrun, verbose, "CodeArtifactDomain", role=role, region=region)
        self.taggers['CodePipelineWebhook'] = tagservices.codepipeline.service.codepipelineTagger(dryrun, verbose, "CodeArtifactRepository", role=role, region=region)

        # Cognito Resources
        self.taggers['CognitoIdentityPool'] = tagservices.cognito.service.cognitoTagger(dryrun, verbose, "CognitoIdentityPool", role=role, region=region)
        self.taggers['CognitoUserPool'] = tagservices.cognito.service.cognitoTagger(dryrun, verbose, "CognitoUserPool", role=role, region=region)

        # Comprehend Resources
        self.taggers['ComprehendDocumentClassifier'] = tagservices.comprehend.service.comprehendTagger(dryrun, verbose, "CognitoIdentityPool", role=role, region=region)
        self.taggers['ComprehendEntityRecognizer'] = tagservices.comprehend.service.comprehendTagger(dryrun, verbose, "CognitoUserPool", role=role, region=region)

        # CodeCommit Resources
        self.taggers['ConfigConfigRule'] = tagservices.configservice.service.configserviceTagger(dryrun, verbose, role=role, region=region)

        # DataBrew Resources
        self.taggers['DataBrewJob'] = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewJob", role=role, region=region)
        self.taggers['DataBrewProject'] = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewProject", role=role, region=region)
        self.taggers['DataBrewRecipe'] = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewRecipe", role=role, region=region)
        self.taggers['DataBrewSchedule'] = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewSchedule", role=role, region=region)

        # DataExchange Resources
        self.taggers['DataExchangeDataSet'] = tagservices.dataexchange.service.dataexchangeTagger(dryrun, verbose, role=role, region=region)

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
        self.taggers['logs'] = tagservices.cloudwatch.service.CloudWatchLogsTagger(dryrun, verbose, role=role, region=region)
        self.taggers['dynamodb'] = tagservices.dynamodb.service.DynamoDBTagger(dryrun, verbose, role=role, region=region)
        self.taggers['lambda'] = tagservices.awslambda.service.LambdaTagger(dryrun, verbose, role=role, region=region)
        self.taggers['redshiftclusergroup'] = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, role=role, region=region)
        self.taggers['cloudformationstack'] = tagservices.cloudformation.service.CloudformationStackTagger(dryrun, verbose, role=role, region=region)

        # Glue Resources
        self.taggers['GlueCrawler'] = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueCrawler', role=role, region=region)
        self.taggers['GlueJob'] = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueJob', role=role, region=region)
        self.taggers['GlueTrigger'] = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueTrigger', role=role, region=region)

        # Kafka Resources
        self.taggers['KafkaCluster'] = tagservices.kafka.service.kafkaTagger(dryrun, verbose, role=role, region=region)

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
            searchresult = tagsearch.checkresource(resourcetype)
            if searchresult == True:
                tagger = self.taggers[resourcetype]
                resource_arn = resource_id

            # We wont need a catch block here because if there is no
            # tagger the code will be stopped at line 94.
            
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