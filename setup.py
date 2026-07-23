#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

with open('README.rst') as f:
    readme = f.read()

setup(
    name='Youtube Closed Captions',
    version='0.2.0',
    description='Download closed captions from Youtube',
    long_description=readme,
    author='Mike Lay',
    author_email='mike@mkly.io',
    license=license,
    packages=find_packages(exclude=('test', 'test.*')),
    install_requires=[
        'yt-dlp>=2023.1.1',
        'pycaption>=1.1.0',
        'beautifulsoup4>=4.9.0',
        'cssutils>=2.0.0',
        'lxml>=4.9.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License'
    ]
)

