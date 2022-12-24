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

### Organizations
Must specificy the organization identifier (which is orgid/accountnumber - Check Tag Editor in aws for details)
```
aws-tagger --resource o-1234567890/123456789012 --tag "App:Foobar"  
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
### Redshift Cluster Parameter Groups
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
```
aws-tagger --resource resourcename --tag "App:Foobar"  

```

## AWS Resource Support (by arn)
AWS Tagger supports the following AWS resource types using the arn of the resource

### EFS files systems
```
aws-tagger --resource arn:aws:elasticfilesystem:us-east-1:1111111111:file-system/fs-1111111 --tag "App:Foobar"  
```

### Elastic Load Balancers
```
aws-tagger --resource arn:aws:elasticloadbalancing:us-east-1:11111111111:loadbalancer/my-elb --tag "App:Foobar"  
```

### RDS instances 
```
aws-tagger --resource arn:aws:rds:us-east-1:111111111:db:my-db --tag "App:Foobar"  
```

### Application Load Balancers
```
aws-tagger --resource arn:aws:elasticloadbalancing:us-east-1:11111111111:loadbalancer/app/nile-content-api-syd-44c45100/f02ac6f33df89ba8 --tag "App:Foobar"  
```

### Elasticache clusters
```
aws-tagger --resource arn:aws:elasticache:us-east-1:111111111:cluster:my-cluster --tag "App:Foobar"  
```

### Elasticsearch domains 
```
aws-tagger --resource arn:aws:es:us-east-1:111111111:domain/my-domain --tag "App:Foobar"  
```

### Kinesis streams
```
aws-tagger --resource arn:aws:kinesis:us-east-1:111111111:stream/my-stream --tag "App:Foobar"  
```