# aws-tagger
Tagging AWS resources is hard because each resource type has a different API which is slightly different. The AWS bulk tagging tool eliminates these differences so that you can simplify specify the resource ID and the tags and it takes care of the rest.  Any tags that already exist on the resource will not be removed, but the values will be updated if the tag key already exists. Tags are case sensitive.

## Install
```
git clone https://github.com/datakind/aws-tagger.git
cd aws-tagger
pip install . #To install directly from this repo once cloned
```

## AWS credentials
AWS Tagger uses the standard AWS credential configuration options. 

### Environment variables
```
export AWS_REGION="us-east-1"
export AWS_ACCESS_KEY_ID="aka..."
export AWS_SECRET_ACCESS_KEY="123..."
aws-tagger --identifier i-07a9d0e5 --tag "App:Foobar"  
```

### IAM Roles
AWS Tagger also supports cross-account role assumption. You will still need to configure the initial AWS credentials using one of the methods above, but the role will be used to call the actuall AWS API.

```
aws-tagger --role arn:aws:iam::11111111111:role/MyRole --identifier i-07a9d0e5 --tag "App:Foobar"
```

## Usage

NOTE: DO NOT PUT DOLLAR SIGNS IN YOUR TAGS $$$

### Tag individual resource with a single tag
```
aws-tagger --identifier i-07a9d0e5 --tag "App:Foobar"  
```

### Tag multiple resources with multiple tags
```
aws-tagger --identifier i-07a9d0e5 --identifier i-0456e3a9 --tag "App:Foobar" --tag "Team:My Team"
```

### Tag multiple resources from a CSV file
AWS Tagger can also take input from a CSV file. The column names of the CSV file are the tag keys and the colume values are the tag values.
The resource id must be in a column called Identifier (refer to the layout from https://us-east-1.console.aws.amazon.com/resource-groups/tag-editor/). To switch between regions, you can add a Region column with the standard AWS regions names like us-east-1. If the Region column is missing it assumes that the region is the same as the AWS credentials.
```
echo 'Id,Region,App' > my-resources.csv
echo 'i-11111111,us-east-1,Foobar' >> my-resources.csv
echo 'i-22222222,us-east-1,Foobar' >> my-resources.csv

aws-tagger --csv my-resources.csv
```

## AWS Resource Support (by identifier's first section string)
AWS Tagger supports the following AWS resource types using there resource identifier's first section to detmine the type of resource

### EC2 instances
Any EC2 volumes that are attached to the instance will be automatically tagged.
```
aws-tagger --identifier i-07a9d0e5 --tag "App:Foobar"  
```

### Organizations (Organization unit, Root, or Policy)
Must specificy the organization identifier (which is orgid/accountnumber - Check Tag Editor in aws for details)
```
aws-tagger --identifier o-1234567890/123456789012 --tag "App:Foobar" --resourcetype "OrganizationsAccount"  
or
aws-tagger --identifier r-1234567890/123456789012 --tag "App:Foobar" --resourcetype "OrganizationsRoot"  
or
aws-tagger --identifier p-1234567890/123456789012 --tag "App:Foobar" --resourcetype "OrganizationsPolicy"  
```

### Snapshots
```
aws-tagger --identifier snap-12345678 --tag "App:Foobar"  
```

### AMI Images
```
aws-tagger --identifier ami-12345678 --tag "App:Foobar"  
```

### Volume Drive
```
aws-tagger --identifier vol-12345678 --tag "App:Foobar"  
```

### VPC (Virtual Private Cloud)
```
aws-tagger --identifier vpc-12345678 --tag "App:Foobar"  
```

### DHCP Options
```
aws-tagger --identifier dopt-12345678 --tag "App:Foobar"  
```

### Internet Gateway
```
aws-tagger --identifier igw-12345678 --tag "App:Foobar"  
```

### Network Acl
```
aws-tagger --identifier acl-12345678 --tag "App:Foobar"  
```

### Network Interface
```
aws-tagger --identifier eni-12345678 --tag "App:Foobar"  
```

### Route Table
```
aws-tagger --identifier rtb-12345678 --tag "App:Foobar"  
```

### Security Group
```
aws-tagger --identifier sg-12345678 --tag "App:Foobar"  
```

### Subnet
```
aws-tagger --identifier subnet-12345678 --tag "App:Foobar"  
```

### EC2 CustomerGateway
```
aws-tagger --identifier resourceid --tag "App:Foobar" --resourcetype "Ec2CustomerGateway"
```

### EC2 Elastic IP
```
aws-tagger --identifier resourceid --tag "App:Foobar" --resourcetype "Ec2EIP"
```

### EC2 Network Gateway
```
aws-tagger --identifier resourceid --tag "App:Foobar" --resourcetype "Ec2NatGateway"
```

### EC2 Reserved Instance
```
aws-tagger --identifier resourceid --tag "App:Foobar" --resourcetype "Ec2ReservedInstance"
```

### EC2 Spot Instance Request
```
aws-tagger --identifier resourceid --tag "App:Foobar" --resourcetype "Ec2SpotInstanceRequest"
```

### EC2 VPN Connection
```
aws-tagger --identifier resourceid --tag "App:Foobar" --resourcetype "Ec2VPNConnection"
```

### S3 buckets
```
aws-tagger --identifier my-bucket --tag "App:Foobar"  
```

### Cloudformation Stacks - CURRENTLY DOESN'T WORK! NEED TO FIX
```
aws-tagger --identifier mystackname/asdf1234-as12-df34-gh56-qwerty012345 --tag "App:Foobar"   
```

### Kafka Cluster
```
aws-tagger --identifier myclustername/asdf1234-as12-df34-gh56-qwerty012345-1 --tag "App:Foobar" --resourcetype "KafkaCluster"
```

### Mq Broker
```
aws-tagger --identifier mybrokername/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "AmazonmqBroker"
```

### Mq Configuration (Not Tested)
```
aws-tagger --identifier mybrokername/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "AmazonmqConfiguration"
```

### Braket Task (Not Tested)
```
aws-tagger --identifier device/quantum-simulator/amazon/mytaskname --tag "App:Foobar" --resourcetype "BraketQuatumTask"
```

### DataBrew Jobs (Not Tested)
```
aws-tagger --identifier job/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataBrewJob"
```

### DataBrew Projects (Not Tested)
```
aws-tagger --identifier project/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataBrewProject"
```

### DataBrew Recipes (Not Tested)
```
aws-tagger --identifier recipe/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataBrewRecipe"
```

### DataBrew Schedules (Not Tested)
```
aws-tagger --identifier schedule/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataBrewSchedule"
```

### DataExchange DataSets (Not Tested)
```
aws-tagger --identifier data-sets/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataExchangeDataSet"
```

### DataPipeline Pipelines (Not Tested)
```
aws-tagger --identifier pipeline/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataPipelinePipeline"
```

### DynamoDB tables (Not Tested)
```
aws-tagger --identifier table/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DynamoDBTable"
```

### ECS Clusters (Not Tested)
```
aws-tagger --identifier cluster/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DynamoDBTable"
```

### ECS Task Definitions (Not Tested)
```
aws-tagger --identifier task-definition/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DynamoDBTable"
```

### EKS Cluster (Not Tested)
```
aws-tagger --identifier cluster/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "EKSCluster"
```

### EMR Cluster (Not Tested)
```
aws-tagger --identifier myclustername --tag "App:Foobar" --resourcetype "EMRCluster"
```

### EMRContainters Virtual Cluster (Not Tested)
```
aws-tagger --identifier virtualclusters/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "EMRContainersVirtualCluster"
```

### ElastiCache Snapshot (Not Tested)
```
aws-tagger --identifier snapshot:a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "ElasticCacheSnapshot"
```

### Elasticache clusters
```
aws-tagger --identifier cluster:my-cluster --tag "App:Foobar" --resourcetype "ElasticCacheSnapshot"
```

### Elastic Inference Accelerator (Not Tested)
```
aws-tagger --identifier elastic-inference-accelerator/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "ElasticInferenceElasticInferenceAccelerator"
```

### Elastic Load Balancers
```
aws-tagger --identifier loadbalancer/my-elb --tag "App:Foobar" --resourcetype "ElasticLoadBalancingLoadBalancer"

aws-tagger --identifier loadbalancer/app/my-elb --tag "App:Foobar" --resourcetype "ElasticLoadBalancingV2LoadBalancer"
```

### Event Rules
```
aws-tagger --identifier rule/myrulename --tag "App:Foobar" --resourcetype "EventsRule"
```

### FSx File System
```
aws-tagger --identifier file-system/myfilesystemid --tag "App:Foobar" --resourcetype "FSxFileSystem"
```

### Forecast Dataset
```
aws-tagger --identifier dataset/myresourceid --tag "App:Foobar" --resourcetype "ForecastDataset"
```

### Forecast Dataset Group
```
aws-tagger --identifier dataset-group/myresourceid --tag "App:Foobar" --resourcetype "ForecastDatasetGroup"
```

### Forecasts
```
aws-tagger --identifier forecast/myresourceid --tag "App:Foobar" --resourcetype "ForecastForecast"
```

### Forecast export jobs
```
aws-tagger --identifier forecast-export-job/myresourceid --tag "App:Foobar" --resourcetype "ForecastForecastExportJob"
```

### Forecast Predictor
```
aws-tagger --identifier what-if-forecast/myresourceid --tag "App:Foobar" --resourcetype "ForecastPredictor"
```

### Forecast Predictor Backtest Export jobs
```
aws-tagger --identifier what-if-forecast-export/myresourceid --tag "App:Foobar" --resourcetype "ForecastDataset"
```

### Forecast Predictor Backtest Export jobs
```
aws-tagger --identifier what-if-forecast-export/myresourceid --tag "App:Foobar" --resourcetype "ForecastDataset"
```

### FraudDectector Dectectors
```
aws-tagger --identifier detector/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorDetector"
```

### FraudDectector Entity-Types
```
aws-tagger --identifier entity-type/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorEntityType"
```

### FraudDectector Event-Types
```
aws-tagger --identifier event-type/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorEventType"
```

### FraudDectector External Models
```
aws-tagger --identifier external-model/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorExternalModel"
```

### FraudDectector Labels
```
aws-tagger --identifier label/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorLabel"
```

### FraudDectector Models
```
aws-tagger --identifier model/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorModel"
```

### FraudDectector Outcomes
```
aws-tagger --identifier outcome/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorOutcome"
```

### FraudDectector Variables
```
aws-tagger --identifier variable/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorVariable"
```

### GreenGrass Connector Definitions
```
aws-tagger --identifier /greengrass/definition/connectors/resourceid --tag "App:Foobar" --resourcetype "GreengrassConnectorDefinition"
```

### GreenGrass Core Definitions
```
aws-tagger --identifier /greengrass/definition/cores/resourceid --tag "App:Foobar" --resourcetype "GreengrassCoreDefinition"
```

### GreenGrass Device Definitions
```
aws-tagger --identifier /greengrass/definition/devices/resourceid --tag "App:Foobar" --resourcetype "GreengrassDeviceDefinition"
```

### GreenGrass Function Definitions
```
aws-tagger --identifier /greengrass/definition/functions/resourceid --tag "App:Foobar" --resourcetype "GreengrassFunctionDefinition"
```

### GreenGrass Groups
```
aws-tagger --identifier /greengrass/groups/resourceid --tag "App:Foobar" --resourcetype "GreengrassGroup"
```

### GreenGrass Logger Definitions
```
aws-tagger --identifier /greengrass/definition/loggers/resourceid --tag "App:Foobar" --resourcetype "GreengrassLoggerDefinition"
```

### GreenGrass Resource Definitions
```
aws-tagger --identifier /greengrass/definition/resources/resourceid --tag "App:Foobar" --resourcetype "GreengrassConnectorDefinition"
```

### GreenGrass Subscription Definitions
```
aws-tagger --identifier /greengrass/definition/subscriptions/resourceid --tag "App:Foobar" --resourcetype "GreengrassSubscriptionDefinition"
```

### IAM OpenID Connect Providers
```
aws-tagger --identifier oidc-provider/resourceid --tag "App:Foobar" --resourcetype "IAMOpenIDConnectProvider"
```

### IOT Analytics Dataset
```
aws-tagger --identifier dataset/resourceid --tag "App:Foobar" --resourcetype "IotAnalyticsDataset"
```

### IOT Events Detector Models
```
aws-tagger --identifier detectorModel/resourceid --tag "App:Foobar" --resourcetype "IoTEventsDetectorModel"
```

### IOT Events Inputs
```
aws-tagger --identifier input/resourceid --tag "App:Foobar" --resourcetype "IoTEventsInput"
```

### Kinesis Analytics Application
```
aws-tagger --identifier application/resourceid --tag "App:Foobar" --resourcetype "KinesisAnalyticsApplication"
```

### Macie Classification Jobs
```
aws-tagger --identifier classification-job/resourceid --tag "App:Foobar" --resourcetype "MacieClassificationJob"
```

### Macie Custom Data Identifier
```
aws-tagger --identifier custom-data-identifier/resourceid --tag "App:Foobar" --resourcetype "MacieCustomDataIdentifier"
```

### Macie Findings Filters
```
aws-tagger --identifier findings-filter/resourceid --tag "App:Foobar" --resourcetype "MacieFindingsFilter"
```

### Macie Members
```
aws-tagger --identifier member/resourceid --tag "App:Foobar" --resourcetype "MacieMember"
```

### OpenSearch Domains
```
aws-tagger --identifier domain/resourceid --tag "App:Foobar" --resourcetype "OpenSearchServiceDomain"
```

### QLDB Ledgers
```
aws-tagger --identifier ledger/resourceid --tag "App:Foobar" --resourcetype "QLDBLedger"
```

### RAM Resource Share
```
aws-tagger --identifier resource-share/resourceid --tag "App:Foobar" --resourcetype "RAMResourceShare"
```

### RDS DBCluster
```
aws-tagger --identifier cluster:resourceid --tag "App:Foobar" --resourcetype "RDSDBCluster"
```

### RDS DBCluster Parameter Group
```
aws-tagger --identifier cluster-pg:resourceid --tag "App:Foobar" --resourcetype "RDSDBClusterParameterGroup"
```

### RDS RDSDBCluster Snapshot
```
aws-tagger --identifier cluster-snapshot:resourceid --tag "App:Foobar" --resourcetype "RDSDBClusterSnapshot"
```

### RDS DBInstance
```
aws-tagger --identifier db:resourceid --tag "App:Foobar" --resourcetype "RDSDBInstance"
```

### RDS Parameter Groups
```
aws-tagger --identifier pg:resourceid --tag "App:Foobar" --resourcetype "RDSDBParameterGroup"
```

### RDS DBSecurity Group
```
aws-tagger --identifier secgrp:resourceid --tag "App:Foobar" --resourcetype "RDSDBSecurityGroup"
```

### RDS DBSnapshot
```
aws-tagger --identifier snapshot:resourceid --tag "App:Foobar" --resourcetype "RDSDBSnapshot"
```

### RDS DBSubnetGroup
```
aws-tagger --identifier subgrp:resourceid --tag "App:Foobar" --resourcetype "RDSDBSubnetGroup"
```

### RDS EventSubscription
```
aws-tagger --identifier es:resourceid --tag "App:Foobar" --resourcetype "RDSEventSubscription"
```

### RDS DBOption Group
```
aws-tagger --identifier og:resourceid --tag "App:Foobar" --resourcetype "RDSOptionGroup"
```

### RDS ReservedDBInstance
```
aws-tagger --identifier ri:resourceid --tag "App:Foobar" --resourcetype "RDSReservedDBInstance"
```

### Redshift Cluster
```
aws-tagger --identifier cluster:resourceid --tag "App:Foobar" --resourcetype "RedshiftCluster"
```

### Redshift Subnet Group
```
aws-tagger --identifier subnetgroup:resourceid --tag "App:Foobar" --resourcetype "RedshiftClusterSubnetGroup"
```

### Redshift Parameter Group
```
aws-tagger --identifier parametergroup:resourceid --tag "App:Foobar" --resourcetype "RedshiftParameterGroup"
```

### Redshift HSM Client Certificate
```
aws-tagger --identifier hsmclientcertificate:resourceid --tag "App:Foobar" --resourcetype "RedshiftHSMClientCertificate"
```

### RoboMaker Robot Application
```
aws-tagger --identifier robot-application/resourceid --tag "App:Foobar" --resourcetype "RoboMakerRobotApplication"
```

### RoboMaker Simulation Job
```
aws-tagger --identifier simulation-job/resourceid --tag "App:Foobar" --resourcetype "RoboMakerSimuationJob"
```

### RoboMaker Simulation Application
```
aws-tagger --identifier simulation-job-application/resourceid --tag "App:Foobar" --resourcetype "RoboMakerSimulationApplication"
```

### Route53Resolver Endpoint
```
aws-tagger --identifier resolver-endpoint/resourceid --tag "App:Foobar" --resourcetype "Route53ResolverResolverEndpoint"
```

### Route53Resolver Rule
```
aws-tagger --identifier resolver-rule/resourceid --tag "App:Foobar" --resourcetype "Route53ResolverResolverRule"
```

### SES Configuration Set
```
aws-tagger --identifier configuration-set/resourceid --tag "App:Foobar" --resourcetype "SESConfigurationSet"
```

### SES Contact List
```
aws-tagger --identifier contact-list/resourceid --tag "App:Foobar" --resourcetype "SESContactList"
```

### SES Dedicated IpPool
```
aws-tagger --identifier dedicated-ip-pool/resourceid --tag "App:Foobar" --resourcetype "SESDedicatedIpPool"
```

### SES Identities
```
aws-tagger --identifier indentity/resourceid --tag "App:Foobar" --resourcetype "SESIdentity"
```

### StepFunctions Activity
```
aws-tagger --identifier activity:resourceid --tag "App:Foobar" --resourcetype "StepFunctionsActivity"
```

### StepFunctions StateMachine
```
aws-tagger --identifier stateMachine:resourceid --tag "App:Foobar" --resourcetype "StepFunctionsStateMachine"
```

### Storage Gateways
```
aws-tagger --identifier gateway/resourceid --tag "App:Foobar" --resourcetype "StorageGatewayGateway"
```

## AWS Resource Support (by searching)
AWS Tagger supports the following AWS resource types by searching for the type of resource directly

### Notebook Instances
### Resource Groups
### SNS Topics
### Instance Profiles
### EFS files systems
### ElasticBeanStalk Apps
### Managed Policies
### SAML Providers
### Lambda Functions
### Route53 Hosted Zone
### Secret Manager Secrets
### Glacier Vaults
### Glue Crawlers
### Glue Job
### Glue Trigger
### Appstream Fleets --resouretype "AppstreamFleet"
### Appstream ImageBulder --resouretype "AppstreamImageBulder" (Not tested)
### Appstream ImageStack --resouretype "AppstreamImageStack" (Not tested)
### Certificate Manager --resouretype "CertificateManagerCertificate" (Not tested)
### Cloud9 Environment --resouretype "Cloud9Environment" (Not tested)
### CloudFront Distributions --resouretype "CloudFrontDistribution" (Not tested)
### CloudFront Streaming Distributions --resouretype "CloudFrontStreamingDistribution" (Not tested)
### CloudTrail Trail --resouretype "CloudTrailTrail" (Not tested)
### CloudWatch Alarm --resouretype "CloudWatchAlarm" (Not tested)
### CodeArtifact Domain --resouretype "CodeArtifactDomain" (Not tested)
### CodeArtifact Repository --resouretype "CodeArtifactRepository" (Not tested)
### CodeCommit Repository --resouretype "CodeCommitRepository" (Not tested)
### CodeGuru-Reviewer RepositoryAssociation --resouretype "CodeGuruReviewerRepositoryAssociation" (Not tested)
### CodePipeline Pipeline --resouretype "CodePipelinePipeline" (Not tested)
### CodePipeline Webhook --resouretype "CodePipelineWebhook" (Not tested)
### Cognito IdentityPool --resouretype "CognitoIdentityPool" (Not tested)
### Cognito UserPool --resouretype "CognitoUserPool" (Not tested)
### Comprehend Document-Classifier --resouretype "ComprehendDocumentClassifier" (Not tested)
### Comprehend Entity-Recognizer --resouretype "ComprehendEntityRecognizer" (Not tested)
### Config Rules --resouretype "ConfigConfigRule" (Not tested)
### IAM Server Certificates --resouretype "IAMServerCertificate" (Not tested)
### Route53 Domains --resouretype "Route53Domain" (Not tested)
### Route53 HealthCheck --resouretype "Route53HealthCheck" (Not tested)
### SQS Queue --resouretype "SQSQueue" (Not tested)
### SSM Parameter --resouretype "SSMParameter" (Not tested)
### Workspaces --resouretype "WorkspacesWorkspace" (Not tested)
```
aws-tagger --identifier resourcename --tag "App:Foobar"  

```

## AWS Resource Support (by arn)
AWS Tagger supports the following AWS resource types using the arn of the resource

### EFS files systems
```
aws-tagger --identifier arn:aws:elasticfilesystem:us-east-1:1111111111:file-system/fs-1111111 --tag "App:Foobar"  
```


### Application Load Balancers
```
aws-tagger --identifier arn:aws:elasticloadbalancing:us-east-1:11111111111:loadbalancer/app/nile-content-api-syd-44c45100/f02ac6f33df89ba8 --tag "App:Foobar"  
```

### Elasticsearch domains 
```
aws-tagger --identifier arn:aws:es:us-east-1:111111111:domain/my-domain --tag "App:Foobar"  
```

### Kinesis streams
```
aws-tagger --identifier arn:aws:kinesis:us-east-1:111111111:stream/my-stream --tag "App:Foobar"  
```