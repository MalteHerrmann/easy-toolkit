import os
import re

from setuptools import find_packages, setup

# Read version from easytk.__version__
this_dir = os.path.dirname(__file__)
with open(os.path.join(this_dir, "easytk", "__init__.py"), "r") as f:
    for line in f:
        if "__version__" in line:
            version = re.search(r'__version__ = "([^"]+)"', line).group(1)
            break

# Read license
with open(os.path.join(this_dir, "LICENSE"), "r") as f:
    license_contents = f.read()

NAME = "easy-toolkit"
VERSION = version
DESCRIPTION = "A simple API wrapper to create functional tkinter GUIs using only a few lines."
KEYWORDS = "tkinter gui api scripting interaction"
AUTHOR = "Malte Herrmann"
AUTHOR_EMAIL = "malteherrmann.mail@web.de"
URL = "https://github.com/MalteHerrmann/easy-toolkit"
LICENSE = license_contents
PACKAGES = find_packages(exclude=["examples", "tests", "tests.*"])

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Topic :: Software Development :: Libraries"
]

params = {
    "name": NAME,
    "version": VERSION,
    "description": DESCRIPTION,
    "keywords": KEYWORDS,
    "author": AUTHOR,
    "author_email": AUTHOR_EMAIL,
    "url": URL,
    "license": LICENSE,
    "packages": PACKAGES,
    "classifiers": CLASSIFIERS
}

setup(**params)
