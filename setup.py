#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages

# Python versions this package is compatible with
python_requires = '>=3.6, <4'

# Packages that this package imports. List everything apart from standard lib packages.
install_requires = [
    'sensirion-i2c-driver>=1.0.0,<2.0',
    'sensirion-driver-adapters>=2.1.9,<3.0',
    'sensirion-driver-support-types>=1.1.0,<2.0',
    'sensirion-shdlc-sensorbridge>=0.1.0,<0.3.0'
]

# Packages required for tests and docs
extras_require = {
    'test': [
        'flake8~=3.7.8',
        'pytest~=6.2.5',
        'pytest-cov~=3.0.0',
    ]
}

# Read version number from version.py
version_line = open("sensirion_i2c_sen66/version.py", "rt").read()
result = re.search(r"^version = ['\"]([^'\"]*)['\"]", version_line, re.M)
if result:
    version_string = result.group(1)
else:
    raise RuntimeError("Unable to find version string")

# Use README.rst and CHANGELOG.md as package description
root_path = os.path.dirname(__file__)
long_description = open(os.path.join(root_path, 'README.md')).read()

setup(
    name='sensirion_i2c_sen66',
    version=version_string,
    author='Sensirion',
    author_email='info@sensirion.com',
    description='I2C driver for the Sensirion SEN66 sensor family',
    license='BSD',
    keywords="""Sensirion SEN66
        I2C
        SEN66""",
    project_urls={
        "Documentation": "https://sensirion.github.io/python-i2c-sen66",
        "Repository": "https://github.com/Sensirion/python-i2c-sen66",
        "Changelog": "https://github.com/Sensirion/python-i2c-sen66/blob/master/CHANGELOG.md",
    },
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=python_requires,
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
