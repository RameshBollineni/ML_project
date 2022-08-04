from setuptools import setup
from typing import List

#declaring variables for setup 
PROJECT_NAME='creaditcard',
VERSION='0.0.1',
AUTHOR='ramesh',
DESCRIPTION='THIS IS MY FIRST ML PROJECT',
PACKAGES=['creaditcard']
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

set(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    Packages=PACKAGES,
    install_requires=get_requirements_list()
    
)
