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
aws-tagger --resource i-07a9d0e5 --tag "App:Foobar"  
```

### IAM Roles
AWS Tagger also supports cross-account role assumption. You will still need to configure the initial AWS credentials using one of the methods above, but the role will be used to call the actuall AWS API.

```
aws-tagger --role arn:aws:iam::11111111111:role/MyRole --resource i-07a9d0e5 --tag "App:Foobar"
```

## Usage

### Tag individual resource with a single tag
```
aws-tagger --resource i-07a9d0e5 --tag "App:Foobar"  
```

### Tag multiple resources with multiple tags
```
aws-tagger --resource i-07a9d0e5 --resource i-0456e3a9 --tag "App:Foobar" --tag "Team:My Team"
```

### Tag multiple resources from a CSV file
AWS Tagger can also take input from a CSV file. The column names of the CSV file are the tag keys and the colume values are the tag values.
The resource id must be in a column called Id. To switch between regions, you can add a Region column with the standard AWS regions names like us-east-1. If the Region column is missing it assumes that the region is the same as the AWS credentials.
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
aws-tagger --resource i-07a9d0e5 --tag "App:Foobar"  
```

### Organizations (Organization unit, Root, or Policy)
Must specificy the organization identifier (which is orgid/accountnumber - Check Tag Editor in aws for details)
```
aws-tagger --resource o-1234567890/123456789012 --tag "App:Foobar" --resourcetype "OrganizationsAccount"  
or
aws-tagger --resource r-1234567890/123456789012 --tag "App:Foobar" --resourcetype "OrganizationsRoot"  
or
aws-tagger --resource p-1234567890/123456789012 --tag "App:Foobar" --resourcetype "OrganizationsPolicy"  
```

### Snapshots
```
aws-tagger --resource snap-12345678 --tag "App:Foobar"  
```

### AMI Images
```
aws-tagger --resource ami-12345678 --tag "App:Foobar"  
```

### Volume Drive
```
aws-tagger --resource vol-12345678 --tag "App:Foobar"  
```

### VPC (Virtual Private Cloud)
```
aws-tagger --resource vpc-12345678 --tag "App:Foobar"  
```

### DHCP Options
```
aws-tagger --resource dopt-12345678 --tag "App:Foobar"  
```

### Internet Gateway
```
aws-tagger --resource igw-12345678 --tag "App:Foobar"  
```

### Network Acl
```
aws-tagger --resource acl-12345678 --tag "App:Foobar"  
```

### Network Interface
```
aws-tagger --resource eni-12345678 --tag "App:Foobar"  
```

### Route Table
```
aws-tagger --resource rtb-12345678 --tag "App:Foobar"  
```

### Security Group
```
aws-tagger --resource sg-12345678 --tag "App:Foobar"  
```

### Subnet
```
aws-tagger --resource subnet-12345678 --tag "App:Foobar"  
```

### EC2 CustomerGateway
```
aws-tagger --resource resourceid --tag "App:Foobar" --resourcetype "Ec2CustomerGateway"
```

### EC2 Elastic IP
```
aws-tagger --resource resourceid --tag "App:Foobar" --resourcetype "Ec2EIP"
```

### EC2 Network Gateway
```
aws-tagger --resource resourceid --tag "App:Foobar" --resourcetype "Ec2NatGateway"
```

### EC2 Reserved Instance
```
aws-tagger --resource resourceid --tag "App:Foobar" --resourcetype "Ec2ReservedInstance"
```

### EC2 Spot Instance Request
```
aws-tagger --resource resourceid --tag "App:Foobar" --resourcetype "Ec2SpotInstanceRequest"
```

### EC2 VPN Connection
```
aws-tagger --resource resourceid --tag "App:Foobar" --resourcetype "Ec2VPNConnection"
```

### S3 buckets
```
aws-tagger --resource my-bucket --tag "App:Foobar"  
```

### Cloudformation Stacks
```
aws-tagger --resource mystackname/asdf1234-as12-df34-gh56-qwerty012345 --tag "App:Foobar"  
```

### Kafka Cluster
```
aws-tagger --resource myclustername/asdf1234-as12-df34-gh56-qwerty012345-1 --tag "App:Foobar" --resourcetype "KafkaCluster"
```

### Mq Broker
```
aws-tagger --resource mybrokername/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "AmazonmqBroker"
```

### Mq Configuration (Not Tested)
```
aws-tagger --resource mybrokername/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "AmazonmqConfiguration"
```

### Braket Task (Not Tested)
```
aws-tagger --resource device/quantum-simulator/amazon/mytaskname --tag "App:Foobar" --resourcetype "BraketQuatumTask"
```

### DataBrew Jobs (Not Tested)
```
aws-tagger --resource job/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataBrewJob"
```

### DataBrew Projects (Not Tested)
```
aws-tagger --resource project/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataBrewProject"
```

### DataBrew Recipes (Not Tested)
```
aws-tagger --resource recipe/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataBrewRecipe"
```

### DataBrew Schedules (Not Tested)
```
aws-tagger --resource schedule/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataBrewSchedule"
```

### DataExchange DataSets (Not Tested)
```
aws-tagger --resource data-sets/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataExchangeDataSet"
```

### DataPipeline Pipelines (Not Tested)
```
aws-tagger --resource pipeline/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DataPipelinePipeline"
```

### DynamoDB tables (Not Tested)
```
aws-tagger --resource table/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DynamoDBTable"
```

### ECS Clusters (Not Tested)
```
aws-tagger --resource cluster/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DynamoDBTable"
```

### ECS Task Definitions (Not Tested)
```
aws-tagger --resource task-definition/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "DynamoDBTable"
```

### EKS Cluster (Not Tested)
```
aws-tagger --resource cluster/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "EKSCluster"
```

### EMR Cluster (Not Tested)
```
aws-tagger --resource myclustername --tag "App:Foobar" --resourcetype "EMRCluster"
```

### EMRContainters Virtual Cluster (Not Tested)
```
aws-tagger --resource virtualclusters/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "EMRContainersVirtualCluster"
```

### ElastiCache Snapshot (Not Tested)
```
aws-tagger --resource snapshot:a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "ElasticCacheSnapshot"
```

### Elasticache clusters
```
aws-tagger --resource cluster:my-cluster --tag "App:Foobar" --resourcetype "ElasticCacheSnapshot"
```

### Elastic Inference Accelerator (Not Tested)
```
aws-tagger --resource elastic-inference-accelerator/a-asdf1234-df34-gh56-qwerty012345 --tag "App:Foobar" --resourcetype "ElasticInferenceElasticInferenceAccelerator"
```

### Elastic Load Balancers
```
aws-tagger --resource loadbalancer/my-elb --tag "App:Foobar" --resourcetype "ElasticLoadBalancingLoadBalancer"

aws-tagger --resource loadbalancer/app/my-elb --tag "App:Foobar" --resourcetype "ElasticLoadBalancingV2LoadBalancer"
```

### Event Rules
```
aws-tagger --resource rule/myrulename --tag "App:Foobar" --resourcetype "EventsRule"
```

### FSx File System
```
aws-tagger --resource file-system/myfilesystemid --tag "App:Foobar" --resourcetype "FSxFileSystem"
```

### Forecast Dataset
```
aws-tagger --resource dataset/myresourceid --tag "App:Foobar" --resourcetype "ForecastDataset"
```

### Forecast Dataset Group
```
aws-tagger --resource dataset-group/myresourceid --tag "App:Foobar" --resourcetype "ForecastDatasetGroup"
```

### Forecasts
```
aws-tagger --resource forecast/myresourceid --tag "App:Foobar" --resourcetype "ForecastForecast"
```

### Forecast export jobs
```
aws-tagger --resource forecast-export-job/myresourceid --tag "App:Foobar" --resourcetype "ForecastForecastExportJob"
```

### Forecast Predictor
```
aws-tagger --resource what-if-forecast/myresourceid --tag "App:Foobar" --resourcetype "ForecastPredictor"
```

### Forecast Predictor Backtest Export jobs
```
aws-tagger --resource what-if-forecast-export/myresourceid --tag "App:Foobar" --resourcetype "ForecastDataset"
```

### Forecast Predictor Backtest Export jobs
```
aws-tagger --resource what-if-forecast-export/myresourceid --tag "App:Foobar" --resourcetype "ForecastDataset"
```

### FraudDectector Dectectors
```
aws-tagger --resource detector/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorDetector"
```

### FraudDectector Entity-Types
```
aws-tagger --resource entity-type/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorEntityType"
```

### FraudDectector Event-Types
```
aws-tagger --resource event-type/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorEventType"
```

### FraudDectector External Models
```
aws-tagger --resource external-model/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorExternalModel"
```

### FraudDectector Labels
```
aws-tagger --resource label/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorLabel"
```

### FraudDectector Models
```
aws-tagger --resource model/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorModel"
```

### FraudDectector Outcomes
```
aws-tagger --resource outcome/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorOutcome"
```

### FraudDectector Variables
```
aws-tagger --resource variable/myresourcepath --tag "App:Foobar" --resourcetype "FraudDetectorVariable"
```

### GreenGrass Connector Definitions
```
aws-tagger --resource /greengrass/definition/connectors/resourceid --tag "App:Foobar" --resourcetype "GreengrassConnectorDefinition"
```

### GreenGrass Core Definitions
```
aws-tagger --resource /greengrass/definition/cores/resourceid --tag "App:Foobar" --resourcetype "GreengrassCoreDefinition"
```

### GreenGrass Device Definitions
```
aws-tagger --resource /greengrass/definition/devices/resourceid --tag "App:Foobar" --resourcetype "GreengrassDeviceDefinition"
```

### GreenGrass Function Definitions
```
aws-tagger --resource /greengrass/definition/functions/resourceid --tag "App:Foobar" --resourcetype "GreengrassFunctionDefinition"
```

### GreenGrass Groups
```
aws-tagger --resource /greengrass/groups/resourceid --tag "App:Foobar" --resourcetype "GreengrassGroup"
```

### GreenGrass Logger Definitions
```
aws-tagger --resource /greengrass/definition/loggers/resourceid --tag "App:Foobar" --resourcetype "GreengrassLoggerDefinition"
```

### GreenGrass Resource Definitions
```
aws-tagger --resource /greengrass/definition/resources/resourceid --tag "App:Foobar" --resourcetype "GreengrassConnectorDefinition"
```

### GreenGrass Subscription Definitions
```
aws-tagger --resource /greengrass/definition/subscriptions/resourceid --tag "App:Foobar" --resourcetype "GreengrassSubscriptionDefinition"
```

### IAM OpenID Connect Providers
```
aws-tagger --resource oidc-provider/resourceid --tag "App:Foobar" --resourcetype "IAMOpenIDConnectProvider"
```

### IOT Analytics Dataset
```
aws-tagger --resource dataset/resourceid --tag "App:Foobar" --resourcetype "IotAnalyticsDataset"
```

### IOT Events Detector Models
```
aws-tagger --resource detectorModel/resourceid --tag "App:Foobar" --resourcetype "IoTEventsDetectorModel"
```

### IOT Events Inputs
```
aws-tagger --resource input/resourceid --tag "App:Foobar" --resourcetype "IoTEventsInput"
```

### Kinesis Analytics Application
```
aws-tagger --resource application/resourceid --tag "App:Foobar" --resourcetype "KinesisAnalyticsApplication"
```

### Macie Classification Jobs
```
aws-tagger --resource classification-job/resourceid --tag "App:Foobar" --resourcetype "MacieClassificationJob"
```

### Macie Custom Data Identifier
```
aws-tagger --resource custom-data-identifier/resourceid --tag "App:Foobar" --resourcetype "MacieCustomDataIdentifier"
```

### Macie Findings Filters
```
aws-tagger --resource findings-filter/resourceid --tag "App:Foobar" --resourcetype "MacieFindingsFilter"
```

### Macie Members
```
aws-tagger --resource member/resourceid --tag "App:Foobar" --resourcetype "MacieMember"
```

### OpenSearch Domains
```
aws-tagger --resource domain/resourceid --tag "App:Foobar" --resourcetype "OpenSearchServiceDomain"
```

### QLDB Ledgers
```
aws-tagger --resource ledger/resourceid --tag "App:Foobar" --resourcetype "QLDBLedger"
```

### RAM Resource Share
```
aws-tagger --resource resource-share/resourceid --tag "App:Foobar" --resourcetype "RAMResourceShare"
```

### RDS DBCluster
```
aws-tagger --resource cluster:resourceid --tag "App:Foobar" --resourcetype "RDSDBCluster"
```

### RDS DBCluster Parameter Group
```
aws-tagger --resource cluster-pg:resourceid --tag "App:Foobar" --resourcetype "RDSDBClusterParameterGroup"
```

### RDS RDSDBCluster Snapshot
```
aws-tagger --resource cluster-snapshot:resourceid --tag "App:Foobar" --resourcetype "RDSDBClusterSnapshot"
```

### RDS DBInstance
```
aws-tagger --resource db:resourceid --tag "App:Foobar" --resourcetype "RDSDBInstance"
```

### RDS Parameter Groups
```
aws-tagger --resource pg:resourceid --tag "App:Foobar" --resourcetype "RDSDBParameterGroup"
```

### RDS DBSecurity Group
```
aws-tagger --resource secgrp:resourceid --tag "App:Foobar" --resourcetype "RDSDBSecurityGroup"
```

### RDS DBSnapshot
```
aws-tagger --resource snapshot:resourceid --tag "App:Foobar" --resourcetype "RDSDBSnapshot"
```

### RDS DBSubnetGroup
```
aws-tagger --resource subgrp:resourceid --tag "App:Foobar" --resourcetype "RDSDBSubnetGroup"
```

### RDS EventSubscription
```
aws-tagger --resource es:resourceid --tag "App:Foobar" --resourcetype "RDSEventSubscription"
```

### RDS DBOption Group
```
aws-tagger --resource og:resourceid --tag "App:Foobar" --resourcetype "RDSOptionGroup"
```

### RDS ReservedDBInstance
```
aws-tagger --resource ri:resourceid --tag "App:Foobar" --resourcetype "RDSReservedDBInstance"
```

### Redshift Cluster
```
aws-tagger --resource cluster:resourceid --tag "App:Foobar" --resourcetype "RedshiftCluster"
```

### Redshift Subnet Group
```
aws-tagger --resource subnetgroup:resourceid --tag "App:Foobar" --resourcetype "RedshiftClusterSubnetGroup"
```

### Redshift Parameter Group
```
aws-tagger --resource parametergroup:resourceid --tag "App:Foobar" --resourcetype "RedshiftParameterGroup"
```

### Redshift HSM Client Certificate
```
aws-tagger --resource hsmclientcertificate:resourceid --tag "App:Foobar" --resourcetype "RedshiftHSMClientCertificate"
```

### RoboMaker Robot Application
```
aws-tagger --resource robot-application/resourceid --tag "App:Foobar" --resourcetype "RoboMakerRobotApplication"
```

### RoboMaker Simulation Job
```
aws-tagger --resource simulation-job/resourceid --tag "App:Foobar" --resourcetype "RoboMakerSimuationJob"
```

### RoboMaker Simulation Application
```
aws-tagger --resource simulation-job-application/resourceid --tag "App:Foobar" --resourcetype "RoboMakerSimulationApplication"
```

### Route53Resolver Endpoint
```
aws-tagger --resource resolver-endpoint/resourceid --tag "App:Foobar" --resourcetype "Route53ResolverResolverEndpoint"
```

### Route53Resolver Rule
```
aws-tagger --resource resolver-rule/resourceid --tag "App:Foobar" --resourcetype "Route53ResolverResolverRule"
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
```
aws-tagger --resource resourcename --tag "App:Foobar"  

```

## AWS Resource Support (by arn)
AWS Tagger supports the following AWS resource types using the arn of the resource

### EFS files systems
```
aws-tagger --resource arn:aws:elasticfilesystem:us-east-1:1111111111:file-system/fs-1111111 --tag "App:Foobar"  
```


### Application Load Balancers
```
aws-tagger --resource arn:aws:elasticloadbalancing:us-east-1:11111111111:loadbalancer/app/nile-content-api-syd-44c45100/f02ac6f33df89ba8 --tag "App:Foobar"  
```

### Elasticsearch domains 
```
aws-tagger --resource arn:aws:es:us-east-1:111111111:domain/my-domain --tag "App:Foobar"  
```

### Kinesis streams
```
aws-tagger --resource arn:aws:kinesis:us-east-1:111111111:stream/my-stream --tag "App:Foobar"  
```