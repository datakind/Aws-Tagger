import os
import boto3
import botocore
from retrying import retry
import tagger.services as tagservices
import socket
import csv
from . import sconfig
from . import tagsearch
from typing import Dict, Literal, Any

#tagservices.appstream.service.AppstreamTagger
tagresults = tagsearch.looptagchecker()

class SingleResourceTagger(object):
    # Init each tagger lazy
    # https://zhaoxh.cn/en/post/2018/lazy-load-dict/
    def __init__(self, dryrun, verbose, accesskey, secretaccesskey, role=None, region=None, tag_volumes=False):
        self.taggers: Dict[tagresults, Any] = {}

        # Amazon Mq Resources
        self.taggers['AmazonmqBroker'] = tagservices.mq.service.mqTagger(dryrun, verbose, servicetype='AmazonmqBroker', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['AmazonmqConfiguration'] = tagservices.mq.service.mqTagger(dryrun, verbose, 'AmazonmqConfiguration', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Braket Resources
        self.taggers['BraketQuantumTask'] = tagservices.braket.service.braketTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Appstream Resources
        self.taggers['AppstreamFleet'] = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamFleet', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['AppstreamImageBulder'] = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamImageBulder', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['AppstreamImageStack'] = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamImageStack', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Certificate Manager
        self.taggers['CertificateManagerCertificate'] = tagservices.certificatemanager.service.certificatemanagerTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Cloud9 Resources
        self.taggers['Cloud9Environment'] = tagservices.cloud9.service.cloud9Tagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Cloudfront Resources
        self.taggers['CloudFrontDistribution'] = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, 'CloudFrontDistribution', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['CloudFrontStreamingDistribution'] = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, 'CloudFrontStreamingDistribution', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # CloudTrail Resources
        self.taggers['CloudTrailTrail'] = tagservices.cloudtrail.service.cloudtrailTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # Cloudwatch Resources
        self.taggers['CloudWatchAlarm'] = tagservices.cloudwatch.service.CloudWatchTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # CodeArtifact Resources
        self.taggers['CodeArtifactDomain'] = tagservices.codeartifact.service.codeartifactTagger(dryrun, verbose, "CodeArtifactDomain", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['CodeArtifactRepository'] = tagservices.codeartifact.service.codeartifactTagger(dryrun, verbose, "CodeArtifactRepository", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # CodeCommit Resources
        self.taggers['CodeCommitRepository'] = tagservices.codecommit.service.codecommitTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # CodeCommit Resources
        self.taggers['CodeGuruReviewerRepositoryAssociation'] = tagservices.codegurureviewer.service.codegurureviewerTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # CodePipeline Resources
        self.taggers['CodePipelinePipeline'] = tagservices.codepipeline.service.codepipelineTagger(dryrun, verbose, "CodeArtifactDomain", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['CodePipelineWebhook'] = tagservices.codepipeline.service.codepipelineTagger(dryrun, verbose, "CodeArtifactRepository", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Cognito Resources
        self.taggers['CognitoIdentityPool'] = tagservices.cognito.service.cognitoTagger(dryrun, verbose, "CognitoIdentityPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['CognitoUserPool'] = tagservices.cognito.service.cognitoTagger(dryrun, verbose, "CognitoUserPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Comprehend Resources
        self.taggers['ComprehendDocumentClassifier'] = tagservices.comprehend.service.comprehendTagger(dryrun, verbose, "CognitoIdentityPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ComprehendEntityRecognizer'] = tagservices.comprehend.service.comprehendTagger(dryrun, verbose, "CognitoUserPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # CodeCommit Resources
        self.taggers['ConfigConfigRule'] = tagservices.configservice.service.configserviceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # DataBrew Resources
        self.taggers['DataBrewJob'] = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['DataBrewProject'] = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewProject", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['DataBrewRecipe'] = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewRecipe", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['DataBrewSchedule'] = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewSchedule", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # DataExchange Resources
        self.taggers['DataExchangeDataSet'] = tagservices.dataexchange.service.dataexchangeTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # DataPipeline Resources
        self.taggers['DataPipelinePipeline'] = tagservices.datapipeline.service.datapipelineTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # DynamoDB Resources
        self.taggers['DynamoDBTable'] = tagservices.dynamodb.service.DynamoDBTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # ElastiCache Resources
        self.taggers['ElasticCacheCacheCluster'] = tagservices.elasticcache.service.ElasticacheTagger(dryrun, verbose, "ElasticCacheCacheCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ElasticCacheSnapshot'] = tagservices.elasticcache.service.ElasticacheTagger(dryrun, verbose, "ElasticCacheSnapshot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Elastic Inference Resources
        self.taggers['ElasticInferenceElasticInferenceAccelerator'] = tagservices.elasticinference.service.elasticinferenceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # EKS Resources
        self.taggers['EKSCluster'] = tagservices.eks.service.eksTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # EMR Resources
        self.taggers['EMRCluster'] = tagservices.emr.service.emrTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # EMRContainers Resources
        self.taggers['EMRContainersVirtualCluster'] = tagservices.emrcontainers.service.emrcontainersTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # EC2 Resources
        self.taggers['ec2'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ec2', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['EC2Instance'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ec2', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['ami'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ami', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['dopt'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'dopt', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['igw'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'igw', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['acl'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'acl', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['igw'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'igw', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['eni'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'eni', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['rtb'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'rtb', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['sg'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'sg', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['subnet'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'subnet', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['vpc'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'vpc', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['EC2CustomerGateway'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2CustomerGateway', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['EC2EIP'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2EIP', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['EC2NatGateway'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2NatGateway', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['EC2ReservedInstance'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2ReservedInstance', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['EC2SpotInstanceRequest'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2SpotInstanceRequest', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        self.taggers['EC2VPNConnection'] = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2VPNConnection', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        
        # ECS Resources
        self.taggers['ECSCluster'] = tagservices.ecs.service.ecsTagger(dryrun, verbose, "ECSCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ECSTaskDefinition'] = tagservices.ecs.service.ecsTagger(dryrun, verbose, "ECSTaskDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Elastic File System resources
        self.taggers['Elasticfilesystem'] = tagservices.efs.service.EFSTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # Elasticloadbalancing Resources
        self.taggers['ElasticLoadBalancingLoadBalancer'] = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, "ElasticLoadBalancingLoadBalancer", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ElasticLoadBalancingV2LoadBalancer'] = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, "ElasticLoadBalancingV2LoadBalancer", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ElasticLoadBalancingV2TargetGroup'] = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, "ElasticLoadBalancingV2TargetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # EventBridge Resources
        self.taggers['EventsRule'] = tagservices.events.service.eventsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Forecast Resources
        self.taggers['ForecastDataset'] = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastDataset", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ForecastDatasetGroup'] = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastDatasetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ForecastForecast'] = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastForecast", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ForecastForecastExportJob'] = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastForecastExportJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ForecastPredictor'] = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastPredictor", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['ForecastPredictorBacktestExportJob'] = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastPredictorBacktestExportJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # FraudDetector Resources
        self.taggers['FraudDetectorDetector'] = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorDetector", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['FraudDetectorEntityType'] = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorEntityType", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['FraudDetectorEventType'] = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorEventType", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['FraudDetectorExternalModel'] = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorExternalModel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['FraudDetectorLabel'] = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorLabel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['FraudDetectorModel'] = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorModel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['FraudDetectorOutcome'] = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorOutcome", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['FraudDetectorVariable'] = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorVariable", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Fsx Resources
        self.taggers['FSxFileSystem'] = tagservices.fsx.service.fsxTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Glacier Resources
        self.taggers['GlacierVault'] = tagservices.glacier.service.glacierTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Glue Resources
        self.taggers['GlueCrawler'] = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueCrawler', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['GlueJob'] = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueJob', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['GlueTrigger'] = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueTrigger', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # GreenGrass Resources
        self.taggers['GreengrassConnectorDefinition'] = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassConnectorDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['GreengrassCoreDefinition'] = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassCoreDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['GreengrassDeviceDefinition'] = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassDeviceDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['GreengrassFunctionDefinition'] = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassFunctionDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['GreengrassGroup'] = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['GreengrassLoggerDefinition'] = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassLoggerDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['GreengrassResourceDefinition'] = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassResourceDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['GreengrassSubscriptionDefinition'] = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassSubscriptionDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # IAM Resources
        self.taggers['IAMInstanceProfile'] = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMInstanceProfile", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['IAMManagedPolicy'] = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMManagedPolicy", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['IAMOpenIDConnectProvider'] = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMOpenIDConnectProvider", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['IAMSAMLProvider'] = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMSAMLProvider", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['IAMServerCertificate'] = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMServerCertificate", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # IOTAnalytics Resources
        self.taggers['IotAnalyticsDataset'] = tagservices.iotanalytics.service.iotanalyticsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # IOTEvents Resources
        self.taggers['IoTEventsDetectorModel'] = tagservices.iotevents.service.ioteventsiotanalyticsTagger(dryrun, verbose, "IoTEventsDetectorModel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['IoTEventsInput'] = tagservices.iotevents.service.ioteventsiotanalyticsTagger(dryrun, verbose, "IoTEventsInput", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Kafka Resources
        self.taggers['KafkaCluster'] = tagservices.kafka.service.kafkaTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # KinesisAnalytics Resources
        self.taggers['KinesisAnalyticsApplication'] = tagservices.kinesisanalytics.service.kinesisanalyticsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Macie Resources
        self.taggers['MacieClassificationJob'] = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieClassificationJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['MacieCustomDataIdentifier'] = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieCustomDataIdentifier", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['MacieFindingsFilter'] = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieFindingsFilter", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['MacieMember'] = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieMember", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # OpenSearchService Resources
        self.taggers['OpenSearchServiceDomain'] = tagservices.opensearchservice.service.opensearchserviceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Organization resources
        self.taggers['OrganizationsAccount'] = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, "OrganizationsAccount", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['OrganizationsRoot'] = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, "OrganizationsRoot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['OrganizationsPolicy'] = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, "OrganizationsPolicy", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # QLDB Resources
        self.taggers['QLDBLedger'] = tagservices.qldb.service.qldbTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # RAM Resources
        self.taggers['RAMResourceShare'] = tagservices.ram.service.ramTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # RDS resources
        self.taggers['RDSDBCluster'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSDBClusterParameterGroup'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBClusterParameterGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSDBClusterSnapshot'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBClusterSnapshot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSDBInstance'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBInstance", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSDBParameterGroup'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBParameterGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSDBSecurityGroup'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBSecurityGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSDBSnapshot'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBSnapshot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSDBSubnetGroup'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBSubnetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSEventSubscription'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSEventSubscription", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSOptionGroup'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSOptionGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RDSReservedDBInstance'] = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSReservedDBInstance", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # Redshift Resources
        self.taggers['RedshiftCluster'] = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RedshiftClusterSubnetGroup'] = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftClusterSubnetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RedshiftParameterGroup'] = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftParameterGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RedshiftHSMClientCertificate'] = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftHSMClientCertificate", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # Resource Groups Resources
        self.taggers['resourcegroup'] = tagservices.resourcegroups.service.ResourceGroupTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # RoboMaker Resoureces
        self.taggers['RoboMakerRobotApplication'] = tagservices.robomaker.service.robomakerTagger(dryrun, verbose, "RoboMakerRobotApplication", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RoboMakerSimulationApplication'] = tagservices.robomaker.service.robomakerTagger(dryrun, verbose, "RoboMakerSimulationApplication", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['RoboMakerSimuationJob'] = tagservices.robomaker.service.robomakerTagger(dryrun, verbose, "RoboMakerSimuationJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Route53 Resources
        self.taggers['Route53HealthCheck'] = tagservices.route53.service.Route53Tagger(dryrun, verbose, "route53hostedzone", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['Route53HostedZone'] = tagservices.route53.service.Route53Tagger(dryrun, verbose, "Route53HostedZone", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
        # Route53Resolver Resources
        self.taggers['Route53ResolverResolverEndpoint'] = tagservices.route53resolver.service.route53resolverTagger(dryrun, verbose, "Route53ResolverResolverEndpoint", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['Route53ResolverResolverRule'] = tagservices.route53resolver.service.route53resolverTagger(dryrun, verbose, "Route53ResolverResolverRule", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # SageMaker Resources
        self.taggers['SageMakerNotebookInstance'] = tagservices.sagemaker.service.SagemakerNotebookInstanceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # S3 Resources
        self.taggers['S3Bucket'] = tagservices.s3.service.S3Tagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # SecretManager Resources
        self.taggers['SecretsManagerSecret'] = tagservices.secretsmanager.service.SecretManagerSecretTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # SES Resources
        self.taggers['SESConfigurationSet'] = tagservices.ses.service.sesTagger(dryrun, verbose, "SESConfigurationSet", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['SESContactList'] = tagservices.ses.service.sesTagger(dryrun, verbose, "SESContactList", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['SESDedicatedIpPool'] = tagservices.ses.service.sesTagger(dryrun, verbose, "SESDedicatedIpPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['SESIdentity'] = tagservices.ses.service.sesTagger(dryrun, verbose, "SESIdentity", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # SNS Resources
        self.taggers['SNSTopic'] = tagservices.sns.service.SNSTopicTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # SQS Resources
        self.taggers['SQSQueue'] = tagservices.sqs.service.sqsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # SSM Resources
        self.taggers['SSMParameter'] = tagservices.ssm.service.ssmTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # StepFunctions Resources
        self.taggers['StepFunctionsActivity'] = tagservices.stepfunctions.service.stepfunctionsTagger(dryrun, verbose, "StepFunctionsActivity", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['StepFunctionsStateMachine'] = tagservices.stepfunctions.service.stepfunctionsTagger(dryrun, verbose, "StepFunctionsStateMachine", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        

        # StorageGateWay Resources
        self.taggers['StorageGatewayGateway'] = tagservices.storagegateway.service.storagegatewayTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        # Workspaces Resources
        self.taggers['WorkspacesWorkspace'] = tagservices.workspaces.service.workspacesTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)





        


        # # Other resources currently
        self.taggers['elasticbenstalkapp'] = tagservices.elasticbeanstalk.service.EBSATagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['es'] = tagservices.es.service.ESTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['kinesis'] = tagservices.kinesis.service.KinesisTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['logs'] = tagservices.cloudwatch.service.CloudWatchTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['lambda'] = tagservices.awslambda.service.LambdaTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        self.taggers['cloudformationstack'] = tagservices.cloudformation.service.CloudformationStackTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        

        

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
            tagger = self.taggers.get(resourcetype)
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
    def __init__(self, dryrun, verbose, accesskey, secretaccesskey, role=None, region=None, tag_volumes=False):
        print(accesskey)
        print("this is a test")
        self.tagger = SingleResourceTagger(dryrun, verbose, role=role, region=region, accesskey=accesskey, secretaccesskey=secretaccesskey, tag_volumes=tag_volumes)

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
        self.resource_id_column = 'Identifier'
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
                    tag_index = { k.replace('Tag: ', ''): v for k, v in tag_index.items() }
                    tag_index_nums = list(tag_index.keys())
                    # print(tag_index_nums)
                    for rci in range(len(tag_index_nums)):
                        if tag_index_nums[rci] == "Service":
                            resourceservicetypenum = rci
                        if tag_index_nums[rci] == "Type":
                            resourcetypenum = rci
                    print(resourceservicetypenum)
                    print(resourcetypenum)
                else:
                    # print(tag_index, row)
                    self._tag_resource(tag_index, resourceservicetypenum, resourcetypenum, row)
                    pass

    def _parse_header(self, header_row):
        tag_index = {}
        for index, name in enumerate(header_row):
            tag_index[name] = index

        return tag_index

    def _tag_resource(self, tag_index, resourceservicetypenum, resourcetypenum, row):
        resource_id = row[tag_index[self.resource_id_column]]
        tags = {}
        for (key, index) in tag_index.items():
            value = row[index]
            if key != self.resource_id_column and \
                key != self.region_column and \
                value != "" and \
                value != "(not tagged)":
                tags[key] = value
        print(tags)

        if "Service" in tags and\
            "Type" in tags:
            print("Resource Type: "+tags["Service"]+tags["Type"])
            resourcetype = tags["Service"]+tags["Type"]
        else:
            resourcetype == None
        tagger = self._lookup_tagger(tag_index, resourcetype, row)
        tagger.tag(resource_id, resourcetype, tags)

    def _lookup_tagger(self, tag_index, resourcetype, row):
        region = self.region
        region_index = tag_index.get(self.region_column)

        if region_index is not None:
            region = row[region_index]
        if region == '':
            region = None

        tagger = self.regional_tagger.get(region)
        if tagger is None:
            tagger = SingleResourceTagger(self.dryrun, self.verbose, resourcetype, role=self.role, region=region, tag_volumes=self.tag_volumes)
            self.regional_tagger[region] = tagger
        return tagger