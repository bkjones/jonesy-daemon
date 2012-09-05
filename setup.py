import os
import sys

import .jonesy_daemon

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='jonesy_daemon',
    version=jonesy_daemon.__version__,
    description='The jonesy_daemon daemonization library',
    author=jonesy_daemon.__author__,
    url='http://github.com/bkjones/jonesy_daemon',
    author_email='bkjones@gmail.com',
    packages='jonesy_daemon',
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
