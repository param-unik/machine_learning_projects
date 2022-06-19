from setuptools import setup, find_packages
from typing import List


# Declaring variables for setup function
PROJECT_NAME = 'housing predictor'
VERSION = '0.0.1'
AUTHOR = 'Param'
DESCRIPTION = 'This is a first FSDS batch NOV batch'
REQUIREMENTS_FILE_NAME = 'requirements.txt'


def get_requirements_list() -> List[str]:
    '''
    Desciption : This function is going to return list of requirements mentioned in requirement.txt file

    return This function is going to return a list which contains name of libraries mentioned in the requirements.txt file

    '''
    with open(REQUIREMENTS_FILE_NAME) as req_file:
        data =  req_file.readlines()

    return data.remove('-e .')

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
