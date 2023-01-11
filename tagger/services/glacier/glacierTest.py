import pytest
import boto3
import botocore.exceptions
import os
import uuid
from tagger.testHelpers import runBasicCLICommand, generateGenericTestTags, tagStringsToDict

def runGlacierCLICommand(identifier, tag):
  runBasicCLICommand(identifier=identifier, tag=tag, resourcetype="glaciervault")
  
def test_glacier_vault_tagged():
  #Set up new vault
  glacierClient = boto3.client('glacier', 
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), 
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), 
    region_name=os.environ.get("AWS_REGION")
  )
  uniqueUID = str(uuid.uuid4())[0: 5]
  vaultName= "GLACIER_VAULT_TEST" + uniqueUID.upper()
  glacierClient.create_vault(vaultName=vaultName)
  try:
    glacierClient.describe_vault(vaultName=vaultName)
  except botocore.exceptions.ClientError as exc:
    assert False, f'Exception raised {exc}'
  #Tag vault using existing cli tools
  numTags = 3
  tagStrings = generateGenericTestTags('glacier', numTags)
  tagDict = {}
  for n in range(len(tagStrings)): 
    runGlacierCLICommand(identifier=vaultName, tag=tagStrings[n])
  tagStringsToDict(tagStrings, tagDict)
  response = glacierClient.list_tags_for_vault(vaultName=vaultName)
  print(response['Tags'])
  assert response['Tags'] == tagDict
  #Delete existing vault and assert deletion
  glacierClient.delete_vault(vaultName=vaultName)
  with pytest.raises(botocore.exceptions.ClientError):
    glacierClient.describe_vault(vaultName="GLACIER_VAULT_TESTER")
  
test_glacier_vault_tagged()
