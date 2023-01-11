import pytest
import boto3
import botocore.exceptions
import os
import uuid
from tagger.testHelpers import runBasicCLICommand, generateGenericTestTags, tagStringsToDict

# NOTE: Not finished, multiple required parameters missing to create a kafka cluster 

def runKafkaCLICommand(identifier, tag):
  runBasicCLICommand(identifier=identifier, tag=tag, resourcetype="kafkaCluster")
  
def test_kafka_cluster_tagged():
  #Set up new vault
  kafkaClient = boto3.client('kafka', 
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), 
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), 
    region_name=os.environ.get("AWS_REGION")
  )
  uniqueUID = str(uuid.uuid4())[0: 5]
  clusterName = 'KAFKA_CLUSTER_TEST' + uniqueUID
  clusterArn = kafkaClient.create_cluster_v2(ClusterName=clusterName)['ClusterArn']
  print(clusterArn)
  try:
    kafkaClient.describe_cluster(ClusterArn=clusterArn)
  except botocore.exceptions.ClientError as exc:
    assert False, f'Exception raised {exc}'
  #Tag vault using existing cli tools
  numTags = 3
  tagStrings = generateGenericTestTags('glacier', numTags)
  tagDict = {}
  for n in range(len(tagStrings)): 
    runKafkaCLICommand(identifier=clusterName, tag=tagStrings[n])
  tagStringsToDict(tagStrings, tagDict)
  response = kafkaClient.list_tags_for_resource(ResourceArn=clusterArn)
  print(response['Tags'])
  assert response['Tags'] == tagDict
  #Delete existing vault and assert deletion
  kafkaClient.delete_cluster(ClusterArn=clusterArn)
  with pytest.raises(botocore.exceptions.ClientError):
    kafkaClient.describe_(ClusterArn=clusterArn)
  
test_kafka_cluster_tagged()
