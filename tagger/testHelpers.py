import subprocess

def runBasicCLICommand(identifier, tag, resourcetype):
  subprocess.run([
    'aws-tagger', '--identifier', identifier, '--tag', tag,
    '--resourcetype', resourcetype
  ], shell=True)

def generateGenericTestTags(resourceName, iterations): 
  x = range(iterations)
  arr = []
  for n in x:
    arr.append(f'{resourceName.capitalize()}Key{n}:ReturnValue{n}')
  return arr

def tagStringsToDict(tagStrings, tagDict): 
  for n in range(len(tagStrings)):
    keyValuePair = tagStrings[n].split(":")
    tagDict[keyValuePair[0]] = keyValuePair[1]
  



