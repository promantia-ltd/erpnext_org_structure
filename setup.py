# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_org_structure/__init__.py
from erpnext_org_structure import __version__ as version

setup(
	name='erpnext_org_structure',
	version=version,
	description='erpnext_org_structure',
	author='admin',
	author_email='admin@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
