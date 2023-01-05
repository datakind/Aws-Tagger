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
        'RedshiftClusterParameterGroup',
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
    resourcetype = resourcetype.lower()
    # Amazon Mq Resources 
    if resourcetype == "AmazonmqBroker".lower():
        tagger = tagservices.mq.service.mqTagger(dryrun, verbose, servicetype='AmazonmqBroker', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "AmazonmqConfiguration".lower():
        tagger = tagservices.mq.service.mqTagger(dryrun, verbose, 'AmazonmqConfiguration', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    
    # Braket Resources
    if resourcetype == "BraketQuantumTask".lower():
        tagger = tagservices.braket.service.braketTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Appstream Resources
    if resourcetype == "AppstreamFleet".lower():
        tagger = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamFleet', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "AppstreamImageBulder".lower():
        tagger = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamImageBulder', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "AppstreamImageStack".lower():
        tagger = tagservices.appstream.service.appstreamTagger(dryrun, verbose, 'AppstreamImageStack', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Certificate Manager
    if resourcetype == "CertificateManagerCertificate".lower():
        tagger = tagservices.certificatemanager.service.certificatemanagerTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Cloud9 Resources
    if resourcetype == "Cloud9Environment".lower():
        tagger = tagservices.cloud9.service.cloud9Tagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # CloudFront Resources
    if resourcetype == "CloudFrontDistribution".lower():
        tagger = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, 'CloudFrontDistribution', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "CloudFrontStreamingDistribution".lower():
        tagger = tagservices.cloudfront.service.CloudfrontTagger(dryrun, verbose, 'CloudFrontStreamingDistribution', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Cloud Trail Resouces 
    if resourcetype == "CloudTrailTrail".lower():
        tagger = tagservices.cloudtrail.service.cloudtrailTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Cloudwatch Resources
    if resourcetype == "CloudWatchAlarm".lower():
        tagger = tagservices.cloudwatch.service.CloudWatchTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # CodeArtifact Resources
    if resourcetype == "CodeArtifactDomain".lower():
        tagger = tagservices.codeartifact.service.codeartifactTagger(dryrun, verbose, "CodeArtifactDomain", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "CodeArtifactRepository".lower():
        tagger = tagservices.codeartifact.service.codeartifactTagger(dryrun, verbose, "CodeArtifactRepository", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        

    #  CodeCommit Resources
    if resourcetype == "CodeCommitRepository".lower():
        tagger = tagservices.codecommit.service.codecommitTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # CodeGuru Resources
    if resourcetype == "CodeGuruReviewerRepositoryAssociation".lower():
        tagger = tagservices.codegurureviewer.service.codegurureviewerTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        

    # CodePipeline Resources
    if resourcetype == "CodePipelinePipeline".lower():
        tagger = tagservices.codepipeline.service.codepipelineTagger(dryrun, verbose, "CodeArtifactDomain", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "CodePipelineWebhook".lower():
        tagger = tagservices.codepipeline.service.codepipelineTagger(dryrun, verbose, "CodeArtifactRepository", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Cognito Resources
    if resourcetype == "CognitoIdentityPool".lower():
        tagger = tagservices.cognito.service.cognitoTagger(dryrun, verbose, "CognitoIdentityPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "CognitoUserPool".lower():
        tagger = tagservices.cognito.service.cognitoTagger(dryrun, verbose, "CognitoUserPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    
    # Comprehend Resources
    if resourcetype == "ComprehendDocumentClassifier".lower():
        tagger = tagservices.comprehend.service.comprehendTagger(dryrun, verbose, "ComprehendDocumentClassifier", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ComprehendEntityRecognizer".lower():
        tagger = tagservices.comprehend.service.comprehendTagger(dryrun, verbose, "ComprehendEntityRecognizer", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    
    # Config Resources
    if resourcetype == "ConfigConfigRule".lower():
        tagger = tagservices.configservice.service.configserviceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # DataBrew Resources
    if resourcetype == "DataBrewJob".lower():
        tagger = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "DataBrewProject".lower():
        tagger = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewProject", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "DataBrewRecipe".lower():
        tagger = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewRecipe", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "DataBrewSchedule".lower():
        tagger = tagservices.databrew.service.databrewTagger(dryrun, verbose, "DataBrewSchedule", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)


    # DataExchange Resources
    if resourcetype == "DataExchangeDataSet".lower():
        tagger = tagservices.dataexchange.service.dataexchangeTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # DataPipeline Resources
    if resourcetype == "DataPipelinePipeline".lower():
        tagger = tagservices.datapipeline.service.datapipelineTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # DynamoDB Resources
    if resourcetype == "DynamoDBTable".lower():
        tagger = tagservices.dynamodb.service.DynamoDBTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # ElastiCache Resources
    if resourcetype == "ElasticCacheCacheCluster".lower():
        tagger = tagservices.elasticcache.service.ElasticacheTagger(dryrun, verbose, "ElasticCacheCacheCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ElasticCacheSnapshot".lower():
        tagger = tagservices.elasticcache.service.ElasticacheTagger(dryrun, verbose, "ElasticCacheSnapshot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Elastic Inference Resources
    if resourcetype == "ElasticInferenceElasticInferenceAccelerator".lower():
        tagger = tagservices.elasticinference.service.elasticinferenceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Elastic Beanstalk Resources
    if resourcetype == "ElasticBeanstalkApplication".lower():
        tagger = tagservices.elasticbeanstalk.service.EBSATagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # EKS Resources
    if resourcetype == "EKSCluster".lower():
        tagger = tagservices.eks.service.eksTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # EMR Resources
    if resourcetype == "EMRCluster".lower():
        tagger = tagservices.emr.service.emrTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # EMRContainers Resources
    if resourcetype == "EMRContainersVirtualCluster".lower():
        tagger = tagservices.emrcontainers.service.emrcontainersTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # EC2 Resources
    if resourcetype == "ec2".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ec2', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2Instance".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ec2', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "ami".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'ami', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "dopt".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'dopt', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "igw".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'igw', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "acl".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'acl', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "eni".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'eni', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "rtb".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'rtb', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "sg".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'sg', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "subnet".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'subnet', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "vpc".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2VPC', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2VPC".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2VPC', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2VPNGateway".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2VPNGateway', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2Snapshot".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2Snapshot', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2Subnet".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2Subnet', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2SecurityGroup".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2SecurityGroup', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2Volume".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2Volume', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2CustomerGateway".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2CustomerGateway', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2Image".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2Image', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2InternetGateway".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2InternetGateway', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2NetworkInterface".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2NetworkInterface', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2NetworkAcl".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2NetworkAcl', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2RouteTable".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2RouteTable', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2DHCPOptions".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'EC2DHCPOptions', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2EIP".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2EIP', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2NatGateway".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2NatGateway', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2ReservedInstance".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2ReservedInstance', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2SpotInstanceRequest".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2SpotInstanceRequest', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
    if resourcetype == "EC2VPNConnection".lower():
        tagger = tagservices.ec2.service.EC2Tagger(dryrun, verbose, 'Ec2VPNConnection', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region, tag_volumes=tag_volumes)
        
    # ECS Resources
    if resourcetype == "ECSCluster".lower():
        tagger = tagservices.ecs.service.ecsTagger(dryrun, verbose, "ECSCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ECSTaskDefinition".lower():
        tagger = tagservices.ecs.service.ecsTagger(dryrun, verbose, "ECSTaskDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Elastic File System resources
    if resourcetype == "ECSTaskDefinition".lower():
        tagger = tagservices.ecs.service.ecsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    if resourcetype == "EFSFileSystem".lower():
        tagger = tagservices.efs.service.EFSTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    
    # Elasticloadbalancing Resources
    if resourcetype == "ElasticLoadBalancingLoadBalancer".lower():
        tagger = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, "ElasticLoadBalancingLoadBalancer", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    if resourcetype == "ElasticLoadBalancingV2LoadBalancer".lower():
        tagger = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, "ElasticLoadBalancingV2LoadBalancer", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    if resourcetype == "ElasticLoadBalancingV2TargetGroup".lower():
        tagger = tagservices.elasticloadbalancing.service.LBTagger(dryrun, verbose, "ElasticLoadBalancingV2TargetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # EventBridge Resources
    if resourcetype == "EventsRule".lower():
        tagger = tagservices.events.service.eventsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Forecast Resources
    if resourcetype == "ForecastDataset".lower():
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastDataset", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastDatasetGroup".lower():
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastDatasetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastForecast".lower():
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastForecast", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastForecastExportJob".lower():
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastForecastExportJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastPredictor".lower():
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastPredictor", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "ForecastPredictorBacktestExportJob".lower():
        tagger = tagservices.forecast.service.forecastTagger(dryrun, verbose, "ForecastPredictorBacktestExportJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # FraudDetector Resources
    if resourcetype == "FraudDetectorDetector".lower():
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorDetector", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorEntityType".lower():
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorEntityType", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorEventType".lower():
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorEventType", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorExternalModel".lower():
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorExternalModel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorLabel".lower():
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorLabel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorModel".lower():
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorModel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorOutcome".lower():
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorOutcome", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "FraudDetectorVariable".lower():
        tagger = tagservices.frauddectector.service.frauddectectorTagger(dryrun, verbose, "FraudDetectorVariable", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Fsx Resources
    if resourcetype == "FSxFileSystem".lower():
        tagger = tagservices.fsx.service.fsxTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Glacier Resources
    if resourcetype == "GlacierVault".lower():
        tagger = tagservices.glacier.service.glacierTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Glue Resources
    if resourcetype == "GlueCrawler".lower():
        tagger = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueCrawler', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GlueJob".lower():
        tagger = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueJob', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GlueTrigger".lower():
        tagger = tagservices.glue.service.glueTagger(dryrun, verbose, 'GlueTrigger', accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # GreenGrass Resources
    if resourcetype == "GreengrassConnectorDefinition".lower():
       tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassConnectorDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassCoreDefinition".lower():
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassCoreDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassDeviceDefinition".lower():
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassDeviceDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassFunctionDefinition".lower():
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassFunctionDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassGroup".lower():
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassLoggerDefinition".lower():
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassLoggerDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassResourceDefinition".lower():
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassResourceDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "GreengrassSubscriptionDefinition".lower():
        tagger = tagservices.greengrass.service.greengrassTagger(dryrun, verbose, "GreengrassSubscriptionDefinition", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # IAM Resources
    if resourcetype == "IAMInstanceProfile".lower():
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMInstanceProfile", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IAMManagedPolicy".lower():
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMManagedPolicy", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IAMOpenIDConnectProvider".lower():
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMOpenIDConnectProvider", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IAMSAMLProvider".lower():
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMSAMLProvider", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IAMServerCertificate".lower():
        tagger = tagservices.iam.service.IamTagger(dryrun, verbose, "IAMServerCertificate", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # IOTAnalytics Resources
    if resourcetype == "IotAnalyticsDataset".lower():
        tagger = tagservices.iotanalytics.service.iotanalyticsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # OTEvents Resources
    if resourcetype == "IoTEventsDetectorModel".lower():
        tagger = tagservices.iotevents.service.ioteventsiotanalyticsTagger(dryrun, verbose, "IoTEventsDetectorModel", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "IoTEventsInput".lower():
        tagger = tagservices.iotevents.service.ioteventsiotanalyticsTagger(dryrun, verbose, "IoTEventsInput", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Kafka Resources
    if resourcetype == "KafkaCluster".lower():
        tagger = tagservices.kafka.service.kafkaTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # KinesisAnalytics Resources
    if resourcetype == "KinesisAnalyticsApplication".lower():
        tagger = tagservices.kinesisanalytics.service.kinesisanalyticsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Macie Resources
    if resourcetype == "MacieClassificationJob".lower():
        tagger = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieClassificationJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "MacieCustomDataIdentifier".lower():
        tagger = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieCustomDataIdentifier", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "MacieFindingsFilter".lower():
        tagger = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieFindingsFilter", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "MacieMember".lower():
        tagger = tagservices.macie.service.macieTagger(dryrun, verbose, "MacieMember", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)


    # OpenSearchService Resources
    if resourcetype == "OpenSearchServiceDomain".lower():
        tagger = tagservices.opensearchservice.service.opensearchserviceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Organization resources
    if resourcetype == "OrganizationsAccount".lower():
        tagger = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, "OrganizationsAccount", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "OrganizationsRoot".lower():
        tagger = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, "OrganizationsRoot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "OrganizationsPolicy".lower():
        tagger = tagservices.organizations.service.OrganizationTagger(dryrun, verbose, "OrganizationsPolicy", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

        
    # QLDB Resources
    if resourcetype == "QLDBLedger".lower():
        tagger = tagservices.qldb.service.qldbTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # RAM Resources
    if resourcetype == "RAMResourceShare".lower():
        tagger = tagservices.ram.service.ramTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # RDS resources
    if resourcetype == "RDSDBCluster".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBClusterParameterGroup".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBClusterParameterGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBClusterSnapshot".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBClusterSnapshot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBInstance".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBInstance", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBParameterGroup".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBParameterGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBSecurityGroup".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBSecurityGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBSnapshot".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBSnapshot", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSDBSubnetGroup".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSDBSubnetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSEventSubscription".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSEventSubscription", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSOptionGroup".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSOptionGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RDSReservedDBInstance".lower():
        tagger = tagservices.rds.service.RDSTagger(dryrun, verbose, "RDSReservedDBInstance", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Redshift Resources
    if resourcetype == "RedshiftCluster".lower():
        tagger = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftCluster", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RedshiftClusterSubnetGroup".lower():
        tagger = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftClusterSubnetGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RedshiftClusterParameterGroup".lower():
        tagger = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftClusterParameterGroup", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RedshiftHSMClientCertificate".lower():
        tagger = tagservices.redshift.service.RedshiftclusterGroupTagger(dryrun, verbose, "RedshiftHSMClientCertificate", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Resource Groups Resources
    if resourcetype == "resourcegroup".lower() or resourcetype == "ResourceGroupsGroup".lower():
        tagger = tagservices.resourcegroups.service.ResourceGroupTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # RoboMaker Resoureces
    if resourcetype == "RoboMakerRobotApplication".lower():
        tagger = tagservices.robomaker.service.robomakerTagger(dryrun, verbose, "RoboMakerRobotApplication", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RoboMakerSimulationApplication".lower():
        tagger = tagservices.robomaker.service.robomakerTagger(dryrun, verbose, "RoboMakerSimulationApplication", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "RoboMakerSimuationJob".lower():
        tagger = tagservices.robomaker.service.robomakerTagger(dryrun, verbose, "RoboMakerSimuationJob", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Route53 Resources
    if resourcetype == "Route53HealthCheck".lower():
        tagger = tagservices.route53.service.Route53Tagger(dryrun, verbose, "route53hostedzone", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "Route53HostedZone".lower():
        tagger = tagservices.route53.service.Route53Tagger(dryrun, verbose, "Route53HostedZone", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        
    # Route53Resolver Resources
    if resourcetype == "Route53ResolverResolverEndpoint".lower():
        tagger = tagservices.route53resolver.service.route53resolverTagger(dryrun, verbose, "Route53ResolverResolverEndpoint", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "Route53ResolverResolverRule".lower():
        tagger = tagservices.route53resolver.service.route53resolverTagger(dryrun, verbose, "Route53ResolverResolverRule", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SageMaker Resources
    if resourcetype == "SageMakerNotebookInstance".lower():
        tagger = tagservices.sagemaker.service.SagemakerNotebookInstanceTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # S3 Resources
    if resourcetype == "S3Bucket".lower():
        tagger = tagservices.s3.service.S3Tagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SecretManager Resources
    if resourcetype == "SecretsManagerSecret".lower():
        tagger = tagservices.secretsmanager.service.SecretManagerSecretTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SES Resources
    if resourcetype == "SESConfigurationSet".lower():
        tagger = tagservices.ses.service.sesTagger(dryrun, verbose, "SESConfigurationSet", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "SESContactList".lower():
        tagger = tagservices.ses.service.sesTagger(dryrun, verbose, "SESContactList", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "SESDedicatedIpPool".lower():
        tagger = tagservices.ses.service.sesTagger(dryrun, verbose, "SESDedicatedIpPool", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "SESIdentity".lower():
        tagger = tagservices.ses.service.sesTagger(dryrun, verbose, "SESIdentity", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SNS Resources
    if resourcetype == "SNSTopic".lower():
        tagger = tagservices.sns.service.SNSTopicTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SQS Resources
    if resourcetype == "SQSQueue".lower():
        tagger = tagservices.sqs.service.sqsTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # SSM Resources
    if resourcetype == "SSMParameter".lower():
        tagger = tagservices.ssm.service.ssmTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # StepFunctions Resources
    if resourcetype == "StepFunctionsActivity".lower():
        tagger = tagservices.stepfunctions.service.stepfunctionsTagger(dryrun, verbose, "StepFunctionsActivity", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "StepFunctionsStateMachine".lower():
        tagger = tagservices.stepfunctions.service.stepfunctionsTagger(dryrun, verbose, "StepFunctionsStateMachine", accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
        

    # StorageGateWay Resources
    if resourcetype == "StorageGatewayGateway".lower():
        tagger = tagservices.storagegateway.service.storagegatewayTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Workspaces Resources
    if resourcetype == "WorkspacesWorkspace".lower():
        tagger = tagservices.workspaces.service.workspacesTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    # Other resources currently
    if resourcetype == "elasticbenstalkapp".lower():
        tagger = tagservices.elasticbeanstalk.service.EBSATagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "es".lower():
        tagger = tagservices.es.service.ESTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "kinesis".lower():
        tagger = tagservices.kinesis.service.KinesisTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "logs".lower():
        tagger = tagservices.cloudwatch.service.CloudWatchTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "lambda".lower() or resourcetype == "LambdaFunction".lower():
        tagger = tagservices.awslambda.service.LambdaTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)
    if resourcetype == "cloudformationstack".lower():
        tagger = tagservices.cloudformation.service.CloudformationStackTagger(dryrun, verbose, accesskey=accesskey, secretaccesskey=secretaccesskey, role=role, region=region)

    return tagger