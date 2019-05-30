# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='Antibiograms',
    version='0.1.0',
    description='First version of the Antibiograms research project',
    long_description=readme,
    author='Alex Calle',
    author_email='alex.calle.clavel@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests'))
)
