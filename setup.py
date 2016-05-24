#!/usr/bin/env python

"""
Installation configuration for Probedock-Nose2
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='nose2-probedock',
    version='0.1.0',
    packages=['nose2_probedock'],
    url='https://github.com/probedock/probedock-nose2',
    license='MIT',
    author='Benjamin Schubert',
    author_email='ben.c.schubert@gmail.com',
    description='Nose2 plugin for reporting test results to ProbeDock CI',

    install_requires=[
        "probedock",
        "nose2",
    ],

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
)
