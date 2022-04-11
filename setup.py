import os
import io
from platform import python_revision
from setuptools import setup, find_packages


APP = ['src/init.py']
NAME = 'py-badge-generator-naayaa-oops'
DESCRIPTION = 'Badge Generator app'
URL = 'https://github.com/NaaYaa-oops/badge-generator-py'
EMAIL = 'seryikotenok232@gmail.com'
AUTHOR = 'NaaYaa-oops'
REQUIRES_PYTHON = '>=2.7.18'
VERSION = '0.1.0'
KEYWORDS = 'py,generator,badges,gh'
REQUIRED = []
EXTRAS = []
OPTIONS = {'argv_emulation': True, }

absolute_path = os.path.abspath(os.path.dirname(__file__))


setup(
    app=APP,
    name=NAME,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    keywords=KEYWORDS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": ""},
    packages=find_packages(),
    python_revision=REQUIRES_PYTHON,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
