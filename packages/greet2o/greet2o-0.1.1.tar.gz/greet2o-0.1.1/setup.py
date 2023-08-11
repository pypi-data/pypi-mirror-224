# Author: TETSUO Yamamoto <tetete1118@gmail.com>
# Copyright (c) 2023- TETSUO Yamamoto
# Licence: MIT

from setuptools import setup

DESCRIPTION = 'tetete1118@gmail.com: Receiving and deleting email on an IMAP4 server.'
NAME = 'greet2o'
AUTHOR = 'TETSUO Yamamoto'
AUTHOR_EMAIL = 'tetete1118@gmail.com'
URL = 'https://github.com/tetsu5555/tetete1118@gmail.com'
LICENSE = 'MIT'
DOWNLOAD_URL = URL
VERSION = '0.1.1'
PYTHON_REQUIRES = '>=3.6'
INSTALL_REQUIRES = []
PACKAGES = [
    'greet2o'
]
KEYWORDS = 'greeting greet2o'
CLASSIFIERS=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
]
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES
)
