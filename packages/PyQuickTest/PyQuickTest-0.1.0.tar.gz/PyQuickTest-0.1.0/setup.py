#!/usr/bin/env python
# -*- coding: utf-8 *-*


""" ~*~ Docstring ~*~
      PyQuickTest is an experimental python testing
             framework designed to deliver an
    easy-and-quick-to-start python testing mechanism.           
                                    ~*~ Docstring ~*~

    ~*~ CHANGELOG ~*~
     ____________________________________________________________________________________
    | VERSION |    DATE    |                           CONTENT                           |
    |====================================================================================|
    |         |            | Initial release, including the following features:          |
    |         |            |     -Decorators for test functions.                         |
    |         |            |     -Assertions functions for test functions.               |
    |         |            |     -Testing routine functions for:                         |
    |  0.0.1  | 2023/08/06 |         *A single function.                                 |
    |         |            |         *A given group/subgroup of functions.               |
    |         |            |         *All functions from a given file.                   |
    |         |            |     -Generators functions for random inputs.                |
    |         |            |     -a CLI tool for running tests.                          |
    |------------------------------------------------------------------------------------|
    |         |            | Adding a smart assertion error printing to avoid useless    |
    |  0.1.0  | 2023/08/06 | lines, and a more detailed test session start message that  |
    |         |            | includes informations about the OS & the software versions. |
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                                                                         ~*~ CHANGELOG ~*~ """


#=--------------=#
# Import section #
#=--------------=#

from   __future__ import annotations
import os
from setuptools import setup

# =------------------------------= #


#=------------------=#
# Authorship section #
#=------------------=#

__author__       = "Quentin Raimbaud"
__maintainer__   = "Quentin Raimbaud"
__contact__      = "quentin.raimbaud.contact@gmail.com"
__organization__ = None
__credits__      = []
__copyright__    = None
__license__      = None
__date__         = "2023/08/06"
__version__      = "0.0.1"
__status__       = "Development"
__filename__     = "setup.py"

# =--------------------------------------------------------= #


#=-------------------------------=#
# Local utility functions section #
#=-------------------------------=#

def read_file(filename: str) -> str:
    """Read the content of a given file."""
    with open(filename, 'r') as file:
        return file.read()

# =-----------------------= #


#=----------------------=#
# Setup function section #
#=----------------------=#

setup(
    name                          = "PyQuickTest",
    version                       = read_file(os.path.join(os.getcwd(), "VERSION")),
    author                        = "Quentin Raimbaud",
    author_email                  = "quentin.raimbaud.contact@gmail.com",
    description                   = "PyQuickTest is an experimental python testing framework designed to \
                           deliver an easy-and-quick-to-start python testing mechanism.",
    long_description              = read_file(os.path.join(os.getcwd(), "README.md")),
    long_description_content_type = "text/markdown",
    license                       = "PSFL",
    keywords                      = ["Code testing",  "Experimental",  "Testing framework"],
    url                           = "https://github.com/quentinemusee/PyQuickTest",
    download_url                  = "https://pypi.org/project/pyquicktest/",
    packages                      = ["pyquicktest"],
    classifiers                   = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    entry_points                  = {
        "console_scripts": [
            "pqt = pyquicktest.cli:cli",
        ]
    },
    install_requires              = [
        "colorama"
    ],
)

# =---------------------------------------------------------------------------------= #