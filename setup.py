#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

with open('README.rst') as f:
    readme = f.read()

setup(
    name='Youtube Closed Captions',
    version='0.1.0',
    description='Download closed captions from Youtube',
    long_description=readme,
    author='Mike Lay',
    author_email='mike@mkly.io',
    license=license,
    packages=find_packages(exclude=('test')),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: Apache Software License'
    ]
)
