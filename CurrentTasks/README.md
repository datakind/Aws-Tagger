# Here is a list of the current resources that need to be added

## amazon mq - COMPLETED
```
Broker describe_broker()
```
```
Configuration describe_configuration()
```
```
Add tags create_tags()
```

## Appstream - COMPLETED
```
Fleet describe_fleets()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_fleets
```
ImageBulder describe_image_builders()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_image_builders
```
Stack describe_stacks()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_stacks
```
Tag tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.tag_resource

## Braket  - COMPLETED (NOT TESTED)
```
QuantumTask get_quantum_task()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.get_quantum_task
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.tag_resource

## Certificate Manager  - COMPLETED (NOT TESTED)
```
Certificate describe_certificate() or get_certificate()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.describe_certificate or 
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.get_certificate
```
Add tags add_tags_to_certificate()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.add_tags_to_certificate

## Cloud9  - COMPLETED (NOT TESTED)
```
Environment describe_environments()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.describe_environments
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.tag_resource

## CloudFront  - COMPLETED (NOT TESTED)
```
StreamingDistribution get_distribution()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_distribution
```
Add tags tag_resource()
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.tag_resource
```

## CloudTrail  - Currently working on (JAY) - 12/23/22
```
Trail get_trail()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.get_trail
```
Add tags add_tags()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.add_tags

## CloudWatch  - Currently working on (JAY) - 12/23/22
```
Alarm describe_alarms()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarms
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.tag_resource

## CodeArtifact  - Currently working on (JAY) - 12/23/22
```
Domain describe_domain()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.describe_domain
```
Repository describe_repository()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.describe_repository
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.tag_resource

## CodeBuild  - Currently working on (JAY) - 12/23/22
```
Project batch_get_projects()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.batch_get_projects
```
Add tags update_project()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.update_project

## CodeCommit  - Currently working on (JAY) - 12/23/22
```
Repository get_repository()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_repository
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.tag_resource

## CodeGuruReviewer  - Currently working on (JAY) - 12/23/22
```
RepositoryAssociation describe_repository_association()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_repository_association
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.tag_resource

## CodePipeline  - Currently working on (JAY) - 12/23/22
```
Pipeline get_pipeline()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline
```
Webhook list_webhooks()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.list_webhooks
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.tag_resource

## Cognito  - Currently working on (JAY) - 12/23/22
```
IdentityPool describe_identity_pool() tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.describe_identity_pool
```
UserPool describe_user_pool() tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool

## Comprehend  - Currently working on (JAY) - 12/23/22
```
DocumentClassifier describe_document_classifier()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_document_classifier
```
EntityRecognizer describe_entity_recognizer()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_entity_recognizer
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.tag_resource

## Config  - Currently working on (JAY) - 12/23/22
```
ConfigRule describe_config_rules()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_config_rules
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.tag_resource

## DataBrew
```
Job describe_job()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_job
```
Project describe_project()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_project
```
Recipe describe_recipe()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_recipe
```
Schedule describe_schedule()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_schedule
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.tag_resource

## DataExchange
```
DataSet get_data_set()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.get_data_set
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.tag_resource

## DataPipeline
```
Pipeline describe_pipelines()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.describe_pipelines
```
Add tags add_tags()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.add_tags

## DynamoDB
```
Table describe_table()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_table
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.tag_resource

## EC2
```
CustomerGateway describe_customer_gateways()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_customer_gateways
```
EIP describe_addresses()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_addresses
```
NatGateWay describe_nat_gateways()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_nat_gateways
```
ReservedInstance describe_reserved_instances()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_reserved_instances
```
SpotInstanceRequest describe_spot_instance_requests()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_instance_requests
```
VPNConnection describe_vpn_connections()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpn_connections
```
Add tags create_tags()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_tags

## ECS
```
Cluster describe_clusters()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.describe_clusters
```
TaskDefinition describe_task_definition()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.describe_task_definition
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.tag_resource

## EKS
```
Cluster describe_cluster()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_cluster
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.tag_resource

## EMR
```
Cluster describe_cluster()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.describe_cluster
```
Add tags add_tags()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.add_tags

## EMRContainers 
```
VirtualCluster describe_virtual_cluster()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.delete_virtual_cluster
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.tag_resource

## ElasticCache
```
Snapshot describe_snapshots()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_snapshots
```
Add tags add_tags_to_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.add_tags_to_resource

## ElasticInference
```
ElasticInferenceAccelerator describe_accelerators()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerators
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.tag_resource

## ElasticLoadBalancingV2
```
LoadBalancer describe_load_balancers()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancers
```
TargetGroup describe_target_groups()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_groups
```
Add tags add_tags()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.add_tags

## Events
```
Rule describe_rule()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.describe_rule
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.tag_resource

## FSx
```
FileSystem describe_file_systems()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.describe_file_systems
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.tag_resource

## Forecast
```
Dataset describe_dataset()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_dataset
```
DatasetGroup describe_dataset_group()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_dataset_group
```
DatasetImportJob describe_dataset_import_job()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_dataset_import_job
```
Forecast describe_forecast()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_forecast
```
ForecastExportJob describe_forecast_export_job()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_forecast_export_job
```
Predictor describe_predictor()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_predictor
```
PredictorBacktestExportJob describe_predictor_backtest_export_job()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_predictor_backtest_export_job
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.tag_resource

## FraudDetector
```
Detector describe_detector()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.describe_detector
```
EntityType get_entity_types()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_entity_types
```
EventType get_event_types()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_event_types
```
ExternalModel get_external_models()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_external_models
```
Label get_labels()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_labels
```
Model get_models()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_models
```
Outcome get_outcomes()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_outcomes
```
Variable get_variables()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_variables
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.tag_resource

## Glacier COMPLETED
```
Vault describe_vault()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.describe_vault
```
Add tags add_tags_to_vault()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.add_tags_to_vault

## Glue COMPLETED
```
Crawler get_crawler()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_crawler
```
Job get_job()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_job
```
Trigger get_trigger()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_trigger
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.tag_resource

## Greengrass
```
ConnectorDefinition get_connector_definition()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_connector_definition
```
CoreDefinition get_core_definition()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_core_definition
```
DeviceDefinition get_device_definition()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_device_definition
```
FunctionDefinition get_function_definition()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_function_definition
```
Group get_group()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_group
```
LoggerDefinition get_logger_definition()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_logger_definition
```
ResourceDefinition get_resource_definition()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_resource_definition
```
SubscriptionDefinition get_subscription_definition()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.tag_resource

## IAM
```
OpenIDConnectProivder get_open_id_connect_provider() tag_open_id_connect_provider()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_open_id_connect_provider
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_open_id_connect_provider
```
ServerCertificate get_server_certificate() tag_server_certificate()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_server_certificate
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_server_certificate

## IotAnalytics
```
Dataset describe_dataset()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_dataset
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.tag_resource

## IoTEvents
```
DetectorModel describe_detector_model()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.describe_detector_model
```
Input describe_input()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.describe_input
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.tag_resource

## KMS
```
Key - doesn't work or need specific permissions describe_key()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.describe_key
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.tag_resource

## Kafha COMPLETED
```
Cluster describe_cluster() describe_cluster_v2()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.describe_cluster
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.describe_cluster_v2
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.tag_resource

## KinesisAnalytics
```
Application describe_application()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.describe_application
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.tag_resource

## Macie
```
ClassificationJob describe_classification_job()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.describe_classification_job
```
CustomDataIdentifier get_custom_data_identifier()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_custom_data_identifier
```
FindingsFilter get_findings_filter()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_findings_filter
```
Member get_master_account()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_master_account
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.tag_resource

## OpenSearchService
```
Domain describe_domain()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_domain
```
Add tags add_tags()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.add_tags

## Organizations
```
Root list_roots()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_roots
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.tag_resource

## QLDB
```
Ledger describe_ledger()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.describe_ledger
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.tag_resource

## RAM
```
ResourceShare get_resource_shares()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.get_resource_shares
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.tag_resource

## RDS
```
DBCluster describe_db_clusters()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_clusters
```
DBClusterParameterGroup describe_db_cluster_parameter_groups()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_parameter_groups
```
DBClusterSnapshot describe_db_cluster_snapshots()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_parameter_groups
```
DBParameterGroup describe_db_parameter_groups()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_parameter_groups
```
DBSecurityGroup describe_db_security_groups()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_security_groups
```
DBSnapshot describe_db_snapshots()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_snapshots
```
DBSubnetGroup describe_db_subnet_groups()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_subnet_groups
```
EventSubscription describe_event_subscriptions()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_event_subscriptions
```
OptionGroup describe_option_groups()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_option_groups
```
ReservedDBInstance describe_reserved_db_instances()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_reserved_db_instances
```
Add tags add_tags_to_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_tags_to_resource

## Redshift
```
Cluster describe_clusters()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_clusters
```
ClusterSubnetGroup describe_cluster_subnet_groups()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_cluster_subnet_groups
```
HSMClientCertificate describe_hsm_client_certificates()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_hsm_client_certificates
```
Add tags create_tags()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_tags

## RoboMaker
```
RobotApplication describe_robot_application()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_robot_application
```
SimulationApplication describe_simulation_application()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_application
```
SimuationJob describe_simulation_job()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.tag_resource

## Route53
```
Domain get_domain_detail() update_tags_for_domain()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.get_domain_detail
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.update_tags_for_domain
```
HealthCheck get_health_check()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_health_check
```
Add tags change_tags_for_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.change_tags_for_resource

## Route53Resolver
```
ResolverEndpoint get_resolver_endpoint()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_endpoint
```
ResolverRule get_resolver_rule()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.tag_resource

## SES
```
ConfigurationSet get_configuration_set()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_configuration_set
```
ContactList get_contact_list()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_contact_list
```
DedicatedIpPool get_dedicated_ip_pool()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_dedicated_ip_pool
```
Identity get_email_identity()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_email_identity
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.tag_resource

## SQS
```
Queue list_queues()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_queues
```
Add tags tag_queue()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.tag_queue

## SSM
```
Parameter describe_parameters()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_parameters
```
Add tags add_tags_to_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.add_tags_to_resource

## StepFunctions
```
Activity describe_activity()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_activity
```
StateMachine describe_state_machine()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_state_machine
```
Add tags tag_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.tag_resource

## StorageGateway
```
Gateway describe_gateway_information()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_gateway_information
```
Add tags add_tags_to_resource()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.add_tags_to_resource

## Workspaces
```
Workspace describe_workspaces()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces
```
Add tags create_tags()
```
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.create_tags
