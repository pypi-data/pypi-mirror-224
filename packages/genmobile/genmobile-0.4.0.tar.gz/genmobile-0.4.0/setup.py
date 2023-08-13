#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['genmobile'],
    package_dir={'': 'src'},
    requires=['genmsg'],
    scripts=['scripts/genmobile_message_artifacts'],
    package_data = {'genmobile': [
           'templates/genmobile_project/*',
           'gradle/*',
        ]},
)

setup(**d)
