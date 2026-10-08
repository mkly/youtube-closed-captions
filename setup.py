#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

with open('README.rst') as f:
    readme = f.read()

setup(
    name='youtube-closed-captions',
    version='1.0.0',
    description='Download closed captions from Youtube',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Mike Lay',
    author_email='mike@mkly.io',
    license=license,
    python_requires='>=3.12',
    url='https://github.com/mkly/youtube-closed-captions',
    project_urls={
        'Issues': 'https://github.com/mkly/youtube-closed-captions/issues',
    },
    packages=find_packages(exclude=('test', 'test.*')),
    install_requires=[
        'yt-dlp>=2023.1.1',
        'pycaption>=1.1.0',
        'beautifulsoup4>=4.9.0',
        'cssutils>=2.0.0',
        'lxml>=4.9.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License'
    ]
)
