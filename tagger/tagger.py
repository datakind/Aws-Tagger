import os
import boto3
import botocore
from retrying import retry
import socket
import csv
from . import sconfig
from . import tagsearch
from typing import Dict, Literal, Any

#tagservices.appstream.service.AppstreamTagger
tagresults = tagsearch.looptagchecker()


class SingleResourceTagger(object):
    # Init each tagger lazy
    # https://zhaoxh.cn/en/post/2018/lazy-load-dict/
    def __init__(self, dryrun, verbose, accesskey, secretaccesskey, role=None, region=None, tag_volumes=False):
        self.taggers: Dict[tagresults, Any] = {}
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.role = role
        self.region = region
        self.tag_volumes = tag_volumes


        # print(self.taggers)

    def tag(self, resource_id, resourcetype, tags, role=None, region=None):
        print(
          f'Resource Identifier: {resource_id}\n' +
          f'Resource Type: {(resourcetype, "Unknown") [resourcetype == None]}\n' +
          f'tags: {tags}'
        )
        
        if resource_id == "":
            return

        if len(tags) == 0:
            return

        tagger = None
        if resourcetype == None:
            searchresult = sconfig.resourcesearch(self.taggers,resource_id,role,region)
            tagger = searchresult[1]
            resource_arn = searchresult[0]
        else:
            # tagger = self.taggers.get(resourcetype)

            tagger = tagsearch.tagselect(resourcetype, self.dryrun, self.verbose, self.accesskey, self.secretaccesskey, role, region, self.tag_volumes)
            resource_arn = resource_id

        if tagger:
            # print(tagger)
            tagger.tag(resource_arn, tags)
        else:
            print("Tagging is not support for this resource %s" % resource_id)

    def _parse_arn(self, resource_arn):
        product = None
        resource_id = None
        parts = resource_arn.split(':')
        if len(parts) > 5:
            product = parts[2]
            resource_id = parts[5]
            resource_parts = resource_id.split('/')
            if len(resource_parts) > 1:
                resource_id = resource_parts[-1]

        return product, resource_id

class MultipleResourceTagger(object):
    def __init__(self, dryrun, verbose, accesskey, secretaccesskey, role=None, region=None, tag_volumes=False):
        self.tagger = SingleResourceTagger(dryrun, verbose, role=role, region=region, accesskey=accesskey, secretaccesskey=secretaccesskey, tag_volumes=tag_volumes)

    def tag(self, resource_ids, resourcetype, tags):
        for resource_id in resource_ids:
            self.tagger.tag(resource_id, resourcetype, tags)

class CSVResourceTagger(object):
    def __init__(self, dryrun, verbose, accesskey, secretaccesskey, role=None, region=None, tag_volumes=False):
        self.dryrun = dryrun
        self.verbose = verbose
        self.accesskey = accesskey
        self.secretaccesskey = secretaccesskey
        self.tag_volumes = tag_volumes
        self.role = role
        self.region = region
        self.regional_tagger = {}
        self.resource_id_column = 'Identifier'
        self.region_column = 'Region'

    def tag(self, filename):
        with open(filename, 'rU') as csv_file:
            reader = csv.reader(csv_file)
            header_row = True
            tag_index = None

            for row in reader:
                if header_row:
                    
                    header_row = False
                    
                    tag_index = self._parse_header(row)
                    tag_index = { k.replace('Tag: ', ''): v for k, v in tag_index.items() }
                    tag_index_nums = list(tag_index.keys())
                    # print(tag_index_nums)
                    for rci in range(len(tag_index_nums)):
                        if tag_index_nums[rci] == "Service":
                            resourceservicetypenum = rci
                        if tag_index_nums[rci] == "Type":
                            resourcetypenum = rci
                else:
                    # print(tag_index, row)
                    self._tag_resource(tag_index, resourceservicetypenum, resourcetypenum, row)
                    pass

    def _parse_header(self, header_row):
        tag_index = {}
        for index, name in enumerate(header_row):
            tag_index[name] = index

        return tag_index

    def _tag_resource(self, tag_index, resourceservicetypenum, resourcetypenum, row):
        resource_id = row[tag_index[self.resource_id_column]]
        tags = {}
        for (key, index) in tag_index.items():
            value = row[index]
            if key != self.resource_id_column and \
                key != self.region_column and \
                value != "" and \
                value != "(not tagged)":
                tags[key] = value
        print(tags)

        if "Service" in tags and\
            "Type" in tags:
            print("Resource Type: "+tags["Service"]+tags["Type"])
            resourcetype = tags["Service"]+tags["Type"]
        else:
            resourcetype == None
        tagger = self._lookup_tagger(tag_index, resourcetype, row)
        tagger.tag(resource_id, resourcetype, tags)

    def _lookup_tagger(self, tag_index, resourcetype, row):
        region = self.region
        region_index = tag_index.get(self.region_column)

        if region_index is not None:
            region = row[region_index]
        if region == '':
            region = None

        tagger = self.regional_tagger.get(region)
        if tagger is None:
            tagger = SingleResourceTagger(self.dryrun, self.verbose, role=self.role, region=region, accesskey=self.accesskey, secretaccesskey=self.secretaccesskey, tag_volumes=self.tag_volumes)
            self.regional_tagger[region] = tagger
        return tagger