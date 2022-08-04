import os
from setuptools import setup, find_packages
import warnings

setup(
    name='aws-tagger-uiuc',
    version='0.6.4',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'boto3>=1.4.4',
        'botocore>=1.5.7',
        'click>=6.6',
        'docutils>=0.13.1',
        'futures>=3.0.5',
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
    author="Eric L. Epps, modified from v0.6.3 from Patrick Cullen and the WaPo platform tools team",
    author_email="eepps2@illinois.edu",
    url="https://github.com/ericepps-uiuc/aws-tagger",
    download_url = "https://github.com/ericepps-uiuc/aws-tagger/tarball/v0.6.4",
    keywords = ['tag', 'tagger', 'tagging', 'aws'],
    classifiers = []
)
