import os
from setuptools import setup, find_packages
import warnings

setup(
    name='aws-tagger',
    version='0.6.5',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'boto3',
        'botocore',
        'click>=6.6',
        'docutils>=0.13.1',
        'jmespath>=0.9.1',
        'retrying>=1.3.3',
        's3transfer>=0.1.10',
        'six>=1.10.0'
    ],
    entry_points={
        "console_scripts": [
            "aws-tagger=tagger.cli:cli",
        ]
    },
    author="Jay Justice with Datakind along with, Eric L. Epps, Patrick Cullen and the WaPo platform tools team",
    author_email="it@datakind.org",
    url="https://github.com/datakind/aws-tagger", 
    download_url = "https://github.com/datakind/aws-tagger.git",
    keywords = ['tag', 'tagger', 'tagging', 'aws'],
    classifiers = []
)
