import subprocess
import pytest
import boto3
import botocore.exceptions
import os
import uuid

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
  subprocess.run([
    'aws-tagger', '--identifier', vaultName, '--tag', "GlacierTestOne:ReturnOne",
    '--resourcetype', 'glaciervault'
  ], shell=True)
  subprocess.run([
    'aws-tagger', "--identifier", vaultName, "--tag", "GlacierTestTwo:ReturnTwo",
    '--resourcetype', 'glaciervault'
  ], shell=True)

  response = glacierClient.list_tags_for_vault(vaultName=vaultName)

  print(response['Tags'])

  assert response['Tags'] == {
    'GlacierTestOne': 'ReturnOne',
    'GlacierTestTwo': 'ReturnTwo'
  }

  glacierClient.delete_vault(vaultName=vaultName)
  

  with pytest.raises(botocore.exceptions.ClientError):
    glacierClient.describe_vault(vaultName="GLACIER_VAULT_TESTER")
  
test_glacier_vault_tagged()
