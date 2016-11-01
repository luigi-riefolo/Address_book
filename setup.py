#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Setup script for Address Book API.
Also installs included versions of third party libraries, 
if those libraries are not already installed.
"""


from __future__ import print_function
import sys

if sys.version_info < (2, 6):
    print('addressbook API requires python version >= 2.6.', file=sys.stderr)
    sys.exit(1)




from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    # 'python setup.py test' simply installs 
    # minimal requirements and runs the tests

    description = "run the automated test suite"
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--doctest-modules', '--verbose',
            './addressbook', './addressbook/tests'
        ]
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))



from setuptools import setup, find_packages
import addressbook
version = addressbook.__version__

tests_require = ['pytest>=2.8.0', 'coverage-4.2', 'pytest-cov-2.4.0']

setup(
    name='Address Book API',
    version=version,
    author='Luigi Riefolo',
    author_email='luigi.riefolo@gmail.com',
    url='http://github.com/luigi-riefolo/addressbook',
    description='Python address book API',
    long_description=open('README.md').read(),
    license='MIT License',
    packages=find_packages(exclude=['*tests*']),
    include_package_data=True,
    install_requires=map(str.strip, open('requirements/' + 'base.txt')),
    tests_require=tests_require,
    platforms=['any'],
    classifiers=(
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Production/Stable',
        'Environment :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ),
    keywords="address book API",
    cmdclass={'test': PyTest}
)
