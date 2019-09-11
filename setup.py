#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='EobotExchangePybot',
    version='0.1.1',
    description='A bot that makes exchanges on Eobot API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JBthePenguin/EobotExchangePybot',
    author='JBthePenguin',
    author_email='jbthepenguin@netcourrier.com',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Terminals",
        "Topic :: Internet",
        "Topic :: System"],
    plateformes='LINUX',
    packages=find_packages(),
    download_url='https://github.com/JBthePenguin/EobotExchangePybot',
    license='GPL Version 3',
    keywords='bot exchange eobot',
    install_requires=['eobot-py'],
)
