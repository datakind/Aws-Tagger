#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import sys
from tagger.tagger import MultipleResourceTagger, CSVResourceTagger
from pprint import pprint

@click.command()
@click.option('--dryrun/--no-dryrun', default=False, help='Verbose output.')
@click.option('--verbose/--no-verbose', default=False, help='Verbose output.')
@click.option('--region', help='AWS region.')
@click.option('--role', help='IAM role to use.')
# TODO: Perhaps a better description for resource would be 'The unique identifier 
# associated with your resource, whether that is its name, instance id, etc'. Resource
# may be too broad a term given that so many different values are associated with any
#given resource
@click.option('--resource', multiple=True, help='Resource ID to tag.')
@click.option('--tag', multiple=True, help='Tag to apply to resource in format "Key:Value".')
@click.option('--resourcetype', help='Specify the resource type for faster processing')
@click.option('--csv', help='CSV file to read data from.')
def cli(dryrun, verbose, region, role, resource, tag, resourcetype, csv):
    # print(resourcetype)
    if csv and (len(resource) > 0 or len(tag) > 0):
        print("Cannot use --resource or --tag with --csv option")
        sys.exit(1)
    if csv:
        tagger = CSVResourceTagger(dryrun, verbose, role, region, tag_volumes=True)
        tagger.tag(csv)
    else:
        tagger = MultipleResourceTagger(dryrun, verbose, resourcetype, role, region, tag_volumes=True)
        tags = _tag_options_to_dict(tag)
        tagger.tag(resource, resourcetype, tags)

def _tag_options_to_dict(tag_options):
    tags = {}
    for tag_option in tag_options:
        key, value = tag_option.split(':')
        tags[key] = value
    return tags

if __name__ == '__main__':
    cli()
