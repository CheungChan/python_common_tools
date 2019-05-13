# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2019-05-06 17:46'

from setuptools import setup

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


setup(
    name='python_common_tools',
    version='1.0.5',
    author='chenzhang',
    author_email='1377699408@qq.com',
    url='https://github.com/CheungChan/python_common_tools',
    description='python common tools',
    long_description="python common tools include cache compress linux log network",
    long_description_content_type="text/markdown",
    packages=['python_common_tools'],
    install_requires=[
        'asn1crypto==0.24.0',
        'autopep8==1.4.4',
        'bcrypt==3.1.6',
        'certifi==2019.3.9',
        'cffi==1.12.3',
        'chardet==3.0.4',
        'cryptography==2.6.1',
        'entrypoints==0.3',
        'flake8==3.7.7',
        'idna==2.8',
        'logzero==1.5.0',
        'mccabe==0.6.1',
        'paramiko==2.4.2',
        'pyasn1==0.4.5',
        'pycodestyle==2.5.0',
        'pycparser==2.19',
        'pyflakes==2.1.1',
        'PyNaCl==1.3.0',
        'requests==2.21.0',
        'six==1.12.0',
        'stackprinter==0.2.0',
        'urllib3==1.24.2'
    ],
    entry_points={
        "console_scripts": "test_pct=python_common_tools.test:main"
    }
)
