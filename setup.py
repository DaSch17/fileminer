#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()



requirements = [ ]

test_requirements = [ ]

setup(
    author="Danaël Schlewer--Becker",
    author_email='.',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="MIT license",
    long_description= " ", #readme + '\n\n' + history
    include_package_data=True,
    keywords='fileminer',
    name='fileminer',
    packages=find_packages(include=['fileminer', 'fileminer.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='',
    version='0.1.0',
    zip_safe=False,
)
