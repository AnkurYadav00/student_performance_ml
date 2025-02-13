from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = '-e .'

def get_requirements(filename: str) -> List[str]:
    '''this function reads requirements file, fetches required packages names'''
    requirements = []
    with open(filename, 'r') as obj:
        requirements = obj.readlines()
        requirements = list(map(lambda x: x.replace('\n', ''), requirements))

    if HYPHON_E_DOT in requirements:
        requirements.remove(HYPHON_E_DOT)

    return requirements

setup(
    name="studentPerformance",
    version="0.01",
    author='ankur',
    author_email='datasciencecraze@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)