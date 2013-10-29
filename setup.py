#!/usr/bin/env python

import os
from setuptools import setup
from setuptools.command.test import test


setup_args = dict(
    name='cherrypy-cors',
    version='1.0',
    url='http://yougov.kilnhg.com/Code/Repositories/global/cherrypy-cors/',
    author='Yougov',
    author_email='gustavo.picon@yougov.com',
    license='Apache License 2.0',
    py_modules=['cherrypy_cors'],
    description='CORS handling as a cherrypy tool.',
)

if __name__ == '__main__':
    setup(**setup_args)
