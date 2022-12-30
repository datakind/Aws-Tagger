import tagger.services as tagservices


def looptagchecker():
    # Define resource list by service+resource
    resourcelist = [
        'AmazonmqBroker',
        'AmazonmqConfiguration',
        'AppstreamFleet',
        'AppstreamImageBulder',
        'AppstreamImageStack',
        'BraketQuantumTask',
        'CertificateManagerCertificate',
        'Cloud9Environment',
        'CloudFrontStreamingDistribution',
        'CloudFrontDistribution',
        'CloudTrailTrail',
        'CloudWatchAlarm',
        'CodeArtifactDomain',
        'CodeArtifactRepository',
        'CodeBuildProject',
        'CodeCommitRepository',
        'CodeGuruReviewerRepositoryAssociation',
        'CodePipelinePipeline',
        'CodePipelineWebhook',
        'CognitoIdentityPool',
        'CognitoUserPool',
        'ComprehendDocumentClassifier',
        'ComprehendEntityRecognizer',
        'ConfigConfigRule',
        'DataBrewJob',
        'DataBrewProject',
        'DataBrewRecipe',
        'DataBrewSchedule',
        'DataExchangeDataSet',
        'DataPipelinePipeline',
        'DynamoDBTable',
        'EC2CustomerGateway',
        'EC2DHCPOptions',
        'EC2Image',
        'EC2InternetGateway',
        'EC2NetworkInterface',
        'EC2ReservedInstance',
        'EC2NatGateway',
        'EC2NetworkAcl',
        'EC2RouteTable',
        'EC2EIP',
        'EC2SecurityGroup',
        'EC2Subnet',
        'EC2Instance',
        'EC2Snapshot',
        'EC2SpotInstanceRequest',
        'EC2VPC',
        'EC2VPNConnection',
        'EC2VPNGateway',
        'EC2Volume',
        'ECSCluster',
        'ECSTaskDefinition',
        'EFSFileSystem',
        'EKSCluster',
        'EMRCluster',
        'EMRContainersVirtualCluster',
        'ElasticCacheCacheCluster',
        'ElasticCacheSnapshot',
        'ElasticBeanstalkApplication',
        'ElasticInferenceElasticInferenceAccelerator',
        'ElasticLoadBalancingLoadBalancer',
        'ElasticLoadBalancingV2LoadBalancer',
        'ElasticLoadBalancingV2TargetGroup',
        'EventsRule',
        'FSxFileSystem',
        'ForecastDataset',
        'ForecastDatasetGroup',
        'ForecastForecast',
        'ForecastForecastExportJob',
        'ForecastPredictor',
        'ForecastPredictorBacktestExportJob',
        'FraudDetectorDetector',
        'FraudDetectorEntityType',
        'FraudDetectorEventType',
        'FraudDetectorExternalModel',
        'FraudDetectorLabel',
        'FraudDetectorModel',
        'FraudDetectorOutcome',
        'FraudDetectorVariable',
        'GlacierVault',
        'GlueCrawler',
        'GlueJob',
        'GlueTrigger',
        'GreengrassConnectorDefinition',
        'GreengrassCoreDefinition',
        'GreengrassDeviceDefinition',
        'GreengrassFunctionDefinition',
        'GreengrassGroup',
        'GreengrassLoggerDefinition',
        'GreengrassResourceDefinition',
        'GreengrassSubscriptionDefinition',
        'IAMInstanceProfile',
        'IAMManagedPolicy',
        'IAMOpenIDConnectProvider',
        'IAMSAMLProvider',
        'IAMServerCertificate',
        'IotAnalyticsDataset',
        'IoTEventsDetectorModel',
        'IoTEventsInput',
        'KMSKey',
        'KafkaCluster',
        'KinesisStream',
        'KinesisAnalyticsApplication',
        'MacieClassificationJob',
        'MacieCustomDataIdentifier',
        'MacieFindingsFilter',
        'MacieMember',
        'OpenSearchServiceDomain',
        'OrganizationsAccount',
        'OrganizationsRoot',
        'OrganizationsPolicy',
        'QLDBLedger',
        'RAMResourceShare',
        'RDSDBCluster',
        'RDSDBClusterParameterGroup',
        'RDSDBClusterSnapshot',
        'RDSDBInstance',
        'RDSDBParameterGroup',
        'RDSDBSecurityGroup',
        'RDSDBSnapshot',
        'RDSDBSubnetGroup',
        'RDSEventSubscription',
        'RDSOptionGroup',
        'RDSReservedDBInstance',
        'RedshiftCluster',
        'RedshiftClusterSubnetGroup',
        'RedshiftParameterGroup',
        'RedshiftHSMClientCertificate',
        'ResourceGroupsGroup',
        'RoboMakerRobotApplication',
        'RoboMakerSimulationApplication',
        'RoboMakerSimuationJob',
        'Route53Domain',
        'Route53HealthCheck',
        'Route53HostedZone',
        'Route53ResolverResolverEndpoint',
        'Route53ResolverResolverRule',
        'SageMakerNotebookInstance',
        'S3Bucket',
        'SecretsManagerSecret',
        'SESConfigurationSet',
        'SESContactList',
        'SESDedicatedIpPool',
        'SESIdentity',
        'SNSTopic',
        'SQSQueue',
        'SSMParameter',
        'StepFunctionsActivity',
        'StepFunctionsStateMachine',
        'StorageGatewayGateway',
        'WorkspacesWorkspace',
    ]
    return resourcelist

def checkresource(resourcetype):
    taglist = looptagchecker()
    for tag in taglist:
        if str(resourcetype).lower() == str(tag).lower():
            return True
    return False

def tagselect(resourcetype,dryrun,verbose,accesskey,secretaccesskey,role,region,tag_volumes):
    # Amazon Mq Resources 
    if resourcetype == "AmazonmqBroker":
        tagger = tagservices.mq.service.mqTagger(dryrun, verbose, servicetype='AmazonmqBroker', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "AmazonmqConfiguration":
        tagger = tagservices.mq.service.mqTagger(dryrun, verbose, 'AmazonmqConfiguration', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    
    # Braket Resources
    if resourcetype == "BraketQuantumTask":
        tagger = tagservices.braket.service.braketTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Appstream Resources
    if resourcetype == "AppstreamFleet":
        tagger = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamFleet', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "AppstreamImageBulder":
        tagger = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamImageBulder', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "AppstreamImageStack":
        tagger = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamImageStack', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Certificate Manager
    if resourcetype == "CertificateManagerCertificate":
        tagger = tagservices.certificatemanager.service.certificatemanagerTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Cloud9 Resources
    if resourcetype == "Cloud9Environment":
        tagger = tagservices.cloud9.service.cloud9Tagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # CloudFront Resources
    if resourcetype == "CloudFrontDistribution":
        tagger = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, 'CloudFrontDistribution', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "CloudFrontStreamingDistribution":
        tagger = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, 'CloudFrontStreamingDistribution', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Cloud Trail Resouces 
    if resourcetype == "CloudTrailTrail":
        tagger = tagservices.cloudtrail.service.cloudtrailTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Cloudwatch Resources
    if resourcetype == "CloudWatchAlarm":
        tagger = tagservices.cloudwatch.service.CloudWatchTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # CodeArtifact Resources
    if resourcetype == "CodeArtifactDomain":
        tagger = tagservices.codeartifact.service.codeartifactTagger(dryrun, verbose, "CodeArtifactDomain", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "CodeArtifactRepository":
        tagger = tagservices.codeartifact.service.codeartifactTagger(dryrun, verbose, "CodeArtifactRepository", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        

    #  CodeCommit Resources
    if resourcetype == "CodeCommitRepository":
        tagger = tagservices.codecommit.service.codecommitTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # CodeGuru Resources
    if resourcetype == "CodeGuruReviewerRepositoryAssociation":
        tagger = tagservices.codegurureviewer.service.codegurureviewerTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        

    # CodePipeline Resources
    if resourcetype == "CodePipelinePipeline":
        tagger = tagservices.codepipeline.service.codepipelineTagger(dryrun, verbose, "CodeArtifactDomain", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "CodePipelineWebhook":
        tagger = tagservices.codepipeline.service.codepipelineTagger(dryrun, verbose, "CodeArtifactRepository", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Cognito Resources
    if resourcetype == "CognitoIdentityPool":
        tagger = tagservices.cognito.service.cognitoTagger(dryrun, verbose, "CognitoIdentityPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "CognitoUserPool":
        tagger = tagservices.cognito.service.cognitoTagger(dryrun, verbose, "CognitoUserPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    
    # Comprehend Resources
    if resourcetype == "ComprehendDocumentClassifier":
        tagger = tagservices.comprehend.service.comprehendTagger(dryrun, verbose, "ComprehendDocumentClassifier", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ComprehendEntityRecognizer":
        tagger = tagservices.comprehend.service.comprehendTagger(dryrun, verbose, "ComprehendEntityRecognizer", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    
    # Config Resources
    if resourcetype == "ConfigConfigRule":
        tagger = tagservices.configservice.service.configserviceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # DataBrew Resources
    if resourcetype == "DataBrewJob":
        tagger = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "DataBrewProject":
        tagger = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewProject", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "DataBrewRecipe":
        tagger = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewRecipe", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "DataBrewSchedule":
        tagger = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewSchedule", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)


    # DataExchange Resources
    if resourcetype == "DataExchangeDataSet":
        tagger = tagservices.dataexchange.service.dataexchangeTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # DataPipeline Resources
    if resourcetype == "DataPipelinePipeline":
        tagger = tagservices.datapipeline.service.datapipelineTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # DynamoDB Resources
    if resourcetype == "DynamoDBTable":
        tagger = tagservices.dynamodb.service.DynamoDBTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # ElastiCache Resources
    if resourcetype == "ElasticCacheCacheCluster":
        tagger = tagservices.elasticcache.service.ElasticacheTagger(dryrun, verbose, "ElasticCacheCacheCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ElasticCacheSnapshot":
        tagger = tagservices.elasticcache.service.ElasticacheTagger(dryrun, verbose, "ElasticCacheSnapshot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Elastic Inference Resources
    if resourcetype == "ElasticInferenceElasticInferenceAccelerator":
        tagger = tagservices.elasticinference.service.elasticinferenceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # EKS Resources
    if resourcetype == "EKSCluster":
        tagger = tagservices.eks.service.eksTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # EMR Resources
    if resourcetype == "EMRCluster":
        tagger = tagservices.emr.service.emrTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # EMRContainers Resources
    if resourcetype == "EMRContainersVirtualCluster":
        tagger = tagservices.emrcontainers.service.emrcontainersTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # EC2 Resources
    if resourcetype == "ec2":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ec2', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2Instance":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ec2', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "ami":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ami', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "dopt":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'dopt', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "igw":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'igw', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "acl":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'acl', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "eni":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'eni', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "rtb":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'rtb', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "sg":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'sg', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "subnet":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'subnet', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "vpc":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'vpc', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2CustomerGateway":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2CustomerGateway', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2EIP":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2EIP', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2NatGateway":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2NatGateway', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2ReservedInstance":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2ReservedInstance', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2SpotInstanceRequest":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2SpotInstanceRequest', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2VPNConnection":
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2VPNConnection', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        
    # ECS Resources
    if resourcetype == "ECSCluster":
        tagger = tagservices.ecs.service.ecsTagger(dryrun, verbose, "ECSCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ECSTaskDefinition":
        tagger = tagservices.ecs.service.ecsTagger(dryrun, verbose, "ECSTaskDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Elastic File System resources
    if resourcetype == "ECSTaskDefinition":
        tagger = tagservices.efs.service.EFSTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Elasticloadbalancing Resources
    if resourcetype == "ElasticLoadBalancingLoadBalancer":
        tagger = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, "ElasticLoadBalancingLoadBalancer", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    if resourcetype == "ElasticLoadBalancingV2LoadBalancer":
        tagger = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, "ElasticLoadBalancingV2LoadBalancer", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    if resourcetype == "ElasticLoadBalancingV2TargetGroup":
        tagger = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, "ElasticLoadBalancingV2TargetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # EventBridge Resources
    if resourcetype == "EventsRule":
        tagger = tagservices.events.service.eventsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Forecast Resources
    if resourcetype == "ForecastDataset":
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastDataset", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastDatasetGroup":
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastDatasetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastForecast":
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastForecast", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastForecastExportJob":
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastForecastExportJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastPredictor":
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastPredictor", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastPredictorBacktestExportJob":
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastPredictorBacktestExportJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # FraudDetector Resources
    if resourcetype == "FraudDetectorDetector":
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorDetector", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorEntityType":
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorEntityType", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorEventType":
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorEventType", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorExternalModel":
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorExternalModel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorLabel":
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorLabel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorModel":
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorModel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorOutcome":
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorOutcome", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorVariable":
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorVariable", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Fsx Resources
    if resourcetype == "FSxFileSystem":
        tagger = tagservices.fsx.service.fsxTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Glacier Resources
    if resourcetype == "GlacierVault":
        tagger = tagservices.glacier.service.glacierTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Glue Resources
    if resourcetype == "GlueCrawler":
        tagger = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueCrawler', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GlueJob":
        tagger = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueJob', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GlueTrigger":
        tagger = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueTrigger', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # GreenGrass Resources
    if resourcetype == "GreengrassConnectorDefinition":
       tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassConnectorDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassCoreDefinition":
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassCoreDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassDeviceDefinition":
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassDeviceDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassFunctionDefinition":
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassFunctionDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassGroup":
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassLoggerDefinition":
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassLoggerDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassResourceDefinition":
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassResourceDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassSubscriptionDefinition":
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassSubscriptionDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # IAM Resources
    if resourcetype == "IAMInstanceProfile":
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMInstanceProfile", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IAMManagedPolicy":
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMManagedPolicy", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IAMOpenIDConnectProvider":
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMOpenIDConnectProvider", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IAMSAMLProvider":
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMSAMLProvider", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IAMServerCertificate":
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMServerCertificate", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # IOTAnalytics Resources
    if resourcetype == "IotAnalyticsDataset":
        tagger = tagservices.iotanalytics.service.iotanalyticsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # OTEvents Resources
    if resourcetype == "IoTEventsDetectorModel":
        tagger = tagservices.iotevents.service.ioteventsiotanalyticsTagger(dryrun, verbose, "IoTEventsDetectorModel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IoTEventsInput":
        tagger = tagservices.iotevents.service.ioteventsiotanalyticsTagger(dryrun, verbose, "IoTEventsInput", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Kafka Resources
    if resourcetype == "KafkaCluster":
        tagger = tagservices.kafka.service.kafkaTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # KinesisAnalytics Resources
    if resourcetype == "KinesisAnalyticsApplication":
        tagger = tagservices.kinesisanalytics.service.kinesisanalyticsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Macie Resources
    if resourcetype == "MacieClassificationJob":
        tagger = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieClassificationJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "MacieCustomDataIdentifier":
        tagger = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieCustomDataIdentifier", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "MacieFindingsFilter":
        tagger = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieFindingsFilter", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "MacieMember":
        tagger = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieMember", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)


    # OpenSearchService Resources
    if resourcetype == "OpenSearchServiceDomain":
        tagger = tagservices.opensearchservice.service.opensearchserviceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Organization resources
    if resourcetype == "OrganizationsAccount":
        tagger = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, "OrganizationsAccount", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "OrganizationsRoot":
        tagger = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, "OrganizationsRoot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "OrganizationsPolicy":
        tagger = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, "OrganizationsPolicy", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        
    # QLDB Resources
    if resourcetype == "QLDBLedger":
        tagger = tagservices.qldb.service.qldbTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # RAM Resources
    if resourcetype == "RAMResourceShare":
        tagger = tagservices.ram.service.ramTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # RDS resources
    if resourcetype == "RDSDBCluster":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBClusterParameterGroup":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBClusterParameterGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBClusterSnapshot":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBClusterSnapshot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBInstance":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBInstance", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBParameterGroup":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBParameterGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBSecurityGroup":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBSecurityGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBSnapshot":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBSnapshot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBSubnetGroup":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBSubnetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSEventSubscription":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSEventSubscription", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSOptionGroup":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSOptionGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSReservedDBInstance":
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSReservedDBInstance", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Redshift Resources
    if resourcetype == "RedshiftCluster":
        tagger = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RedshiftClusterSubnetGroup":
        tagger = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftClusterSubnetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RedshiftParameterGroup":
        tagger = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftParameterGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RedshiftHSMClientCertificate":
        tagger = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftHSMClientCertificate", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Resource Groups Resources
    if resourcetype == "resourcegroup":
        tagger = tagservices.resourcegroups.service.ResourceGroupTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # RoboMaker Resoureces
    if resourcetype == "RoboMakerRobotApplication":
        tagger = tagservices.robomaker.service.robomakerTagger(dryrun, verbose, "RoboMakerRobotApplication", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RoboMakerSimulationApplication":
        tagger = tagservices.robomaker.service.robomakerTagger(dryrun, verbose, "RoboMakerSimulationApplication", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RoboMakerSimuationJob":
        tagger = tagservices.robomaker.service.robomakerTagger(dryrun, verbose, "RoboMakerSimuationJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Route53 Resources
    if resourcetype == "Route53HealthCheck":
        tagger = tagservices.route53.service.Route53Tagger(dryrun, verbose, "route53hostedzone", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "Route53HostedZone":
        tagger = tagservices.route53.service.Route53Tagger(dryrun, verbose, "Route53HostedZone", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Route53Resolver Resources
    if resourcetype == "Route53ResolverResolverEndpoint":
        tagger = tagservices.route53resolver.service.route53resolverTagger(dryrun, verbose, "Route53ResolverResolverEndpoint", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "Route53ResolverResolverRule":
        tagger = tagservices.route53resolver.service.route53resolverTagger(dryrun, verbose, "Route53ResolverResolverRule", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SageMaker Resources
    if resourcetype == "SageMakerNotebookInstance":
        tagger = tagservices.sagemaker.service.SagemakerNotebookInstanceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # S3 Resources
    if resourcetype == "S3Bucket":
        tagger = tagservices.s3.service.S3Tagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SecretManager Resources
    if resourcetype == "SecretsManagerSecret":
        tagger = tagservices.secretsmanager.service.SecretManagerSecretTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SES Resources
    if resourcetype == "SESConfigurationSet":
        tagger = tagservices.ses.service.sesTagger(dryrun, verbose, "SESConfigurationSet", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "SESContactList":
        tagger = tagservices.ses.service.sesTagger(dryrun, verbose, "SESContactList", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "SESDedicatedIpPool":
        tagger = tagservices.ses.service.sesTagger(dryrun, verbose, "SESDedicatedIpPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "SESIdentity":
        tagger = tagservices.ses.service.sesTagger(dryrun, verbose, "SESIdentity", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SNS Resources
    if resourcetype == "SNSTopic":
        tagger = tagservices.sns.service.SNSTopicTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SQS Resources
    if resourcetype == "SQSQueue":
        tagger = tagservices.sqs.service.sqsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SSM Resources
    if resourcetype == "SSMParameter":
        tagger = tagservices.ssm.service.ssmTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # StepFunctions Resources
    if resourcetype == "StepFunctionsActivity":
        tagger = tagservices.stepfunctions.service.stepfunctionsTagger(dryrun, verbose, "StepFunctionsActivity", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "StepFunctionsStateMachine":
        tagger = tagservices.stepfunctions.service.stepfunctionsTagger(dryrun, verbose, "StepFunctionsStateMachine", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        

    # StorageGateWay Resources
    if resourcetype == "StorageGatewayGateway":
        tagger = tagservices.storagegateway.service.storagegatewayTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Workspaces Resources
    if resourcetype == "WorkspacesWorkspace":
        tagger = tagservices.workspaces.service.workspacesTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Other resources currently
    if resourcetype == "elasticbenstalkapp":
        tagger = tagservices.elasticbeanstalk.service.EBSATagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "es":
        tagger = tagservices.es.service.ESTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "kinesis":
        tagger = tagservices.kinesis.service.KinesisTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "logs":
        tagger = tagservices.cloudwatch.service.CloudWatchTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "lambda":
        tagger = tagservices.awslambda.service.LambdaTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "cloudformationstack":
        tagger = tagservices.cloudformation.service.CloudformationStackTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    return tagger