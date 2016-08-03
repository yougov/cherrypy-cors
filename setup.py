#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io
import sys

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx', 'rst.linker'] if needs_sphinx else []
needs_wheel = {'release', 'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

name = 'cherrypy-cors'
description = 'CORS handling as a cherrypy tool.'

setup_params = dict(
    name=name,
    use_scm_version=True,
    author="YouGov, Plc.",
    author_email="opensource@yougov.com",
    description=description or name,
    long_description=long_description,
    url="https://github.com/yougov/" + name,
    py_modules=['cherrypy_cors'],
    install_requires=[
        'cherrypy>=3',
        'httpagentparser>=1.5',
    ],
    extras_require={
    },
    setup_requires=[
        'setuptools_scm>=1.9',
    ] + pytest_runner + sphinx + wheel,
    tests_require=[
        'pytest>=2.8',
        # cherrypy requires but doesn't declare
        'nose',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
    },
)
if __name__ == '__main__':
    setuptools.setup(**setup_params)
