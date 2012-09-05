import os
import sys

import .daemonize

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='jonesy-daemon',
    version=daemonize.__version__,
    description='The jonesy-daemon daemonization library',
    author=daemonize.__author__,
    url='http://github.com/bkjones/jonesy-daemon',
    author_email='bkjones@gmail.com',
    packages='daemonize',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
