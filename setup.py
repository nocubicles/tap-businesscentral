#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-businesscentral",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_businesscentral"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
        "odata @ https://github.com/dreamdata-io/python-odata/archive/master.zip"
    ],
    entry_points="""
    [console_scripts]
    tap-businesscentral=tap_businesscentral:main
    """,
    packages=["tap_businesscentral"],
    package_data = {
        "schemas": ["tap_businesscentral/schemas/*.json"]
    },
    include_package_data=True,
)
