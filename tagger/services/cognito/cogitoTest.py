import os
import uuid
import botocore
import pytest
from tagger.sconfig import _client, resourcesearch
from tagger.testHelpers import runBasicCLICommand, generateGenericTestTags, tagStringsToDict

def runCognitoIdentityPoolCLI(identifier, tag):
  runBasicCLICommand(identifier=identifier, tag=tag, resourcetype="CognitoIdentityPool")

def runCognitoUserPoolCLI(identifer, tag):
  runBasicCLICommand(identifer=identifer, tag=tag, resourcettype="CognitoUserPool")

def test_cogito_identity_pool_tagged(): 
  cogitoClient = _client('cognito-identity', 
    accesskey=os.environ.get("AWS_ACCESS_KEY_ID"),
    secretaccesskey=os.environ.get("AWS_SECRET_ACCESS_KEY"), 
    role=None, 
    region=os.environ.get("AWS_REGION")
  )
  uniqueUID = str(uuid.uuid4())[0: 5]
  identityName = "COGITO_IDENTITY_POOL_TEST" + uniqueUID.upper()
  identityPoolId = cogitoClient.create_identity_pool(
    IdentityPoolName=identityName,
    AllowUnauthenticatedIdentities=True
  )

  #Tag vault using existing cli tools
  numTags = 3
  tagStrings = generateGenericTestTags('cogitoIdentityPool', numTags)
  tagDict = {}
  for n in range(len(tagStrings)): 
    runCognitoIdentityPoolCLI(identifier=identityName, tag=tagStrings[n])
  #Check if tags were applied
  tagStringsToDict(tagStrings, tagDict)
  searchResult = resourcesearch()
  
test_cogito_identity_tagged()