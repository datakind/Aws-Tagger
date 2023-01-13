import boto3
import uuid
import os
import pytest
import botocore.exceptions
from tagger.sconfig import _client
from tagger.testHelpers import runBasicCLICommand, generateGenericTestTags, tagStringsToDict

def runDynamoDBTableCLI(identifier, tag):
  runBasicCLICommand(identifier=identifier, tag=tag, resourcetype="DynamoDBTable")

def test_dynamo_db_table_tagged(): 
  dynamoClient = boto3.client('dynamodb', 
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), 
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), 
    region_name=os.environ.get("AWS_REGION")
  )

  unique = str(uuid.uuid4())[0:5].upper()
  tableName = 'DYNAMO_DB_TABLE_TEST' + unique

  response = dynamoClient.create_table(
    AttributeDefinitions=[
      {
        'AttributeName': 'Artist',
        'AttributeType': 'S',
      },
      {
        'AttributeName': 'SongTitle',
        'AttributeType': 'S',
      },
    ],
    KeySchema=[
      {
        'AttributeName': 'Artist',
        'KeyType': 'HASH',
      },
      {
        'AttributeName': 'SongTitle',
        'KeyType': 'RANGE',
      },
    ],
    ProvisionedThroughput={
      'ReadCapacityUnits': 5,
      'WriteCapacityUnits': 5,
    },
    TableName=tableName
  )
  try:
    dynamoWaiter = dynamoClient.get_waiter('table_exists')
    dynamoWaiter.wait(TableName=tableName)
  except botocore.exceptions.ClientError as exc:
    assert False, f'Table not found {exc}'

  tableArn = response['TableDescription']['TableArn']

   #Tag vault using existing cli tools
  numTags = 3
  tagStrings = generateGenericTestTags('Dynamo', numTags)
  print("TagStrings")
  print(tagStrings)
  tagDict = {}
  for n in range(len(tagStrings)): 
    print(tagStrings[n])
    runDynamoDBTableCLI(identifier=tableName, tag=tagStrings[n])
  #Check if tags were applied
  tagStringsToDict(tagStrings, tagDict)

  tagsResponse = dynamoClient.list_tags_of_resource(ResourceArn=tableArn)['Tags']
  print(tagsResponse)
  print(tagDict)
  for n in range(len(tagsResponse)):
    #Check if the tagDictionary has the key at n in tagsResponse
    currentKey = tagsResponse[n]['Key']
    if currentKey not in tagDict:
      assert False == True
    assert tagsResponse[n]['Value'] == tagDict[currentKey]
  #Delete existing table
  dynamoClient.delete_table(TableName=tableName)

test_dynamo_db_table_tagged()