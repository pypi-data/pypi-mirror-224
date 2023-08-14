#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pandas>=1.0.0',
    ]

test_requirements = [ ]

setup(
    author="Liam Brown",
    author_email='pcrxn@proton.me',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Obtain tidy alignment coverage info from sorted BAM files",
    entry_points={
        'console_scripts': [
            'aligncov=aligncov.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='aligncov',
    name='aligncov',
    packages=find_packages(include=['aligncov', 'aligncov.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pcrxn/aligncov',
    version='0.0.2',
    zip_safe=False,
)
