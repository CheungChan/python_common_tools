# -*- coding: utf-8 -*-
__author__ = "陈章"
__date__ = "2019-05-06 17:46"

from setuptools import setup, find_packages
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

if os.path.exists("README.md"):
    long_description = open("README.md", "r", encoding="utf-8").read()
else:
    long_description = "python common tools"

requirements = """
"""
install_requires = [i for i in requirements.split() if i]
setup(
    name="python_common_tools",
    version="2.6.1",
    python_requires=">3.5.0",
    author="chenzhang",
    author_email="1377699408@qq.com",
    url="https://github.com/CheungChan/python_common_tools",
    description="python common tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "console_scripts": "az_auto_reload=python_common_tools.autoreload:main"
    },
    # 个人shell工具
    # scripts=[
    #     "python_common_tools/bin/az_kill.sh",
    #     "python_common_tools/bin/az_nohup_start.sh",
    # ],
)
