#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as readme:
    long_description = readme.read()

setup_args = dict(
    name='cherrypy-cors',
    use_scm_version=True,
    url='https://bitbucket.org/yougov/cherrypy-cors/',
    author='YouGov, Plc.',
    author_email='gustavo.picon@yougov.com',
    long_description=long_description,
    license='Apache License 2.0',
    py_modules=['cherrypy_cors'],
    description='CORS handling as a cherrypy tool.',
    install_requires=[
        'cherrypy>=3',
        'httpagentparser>=1.5'
    ],
    setup_requires=[
        'setuptools_scm',
    ]
)

if __name__ == '__main__':
    setup(**setup_args)
