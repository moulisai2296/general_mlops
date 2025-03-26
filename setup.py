from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''Returns a list of requirements'''
    with open(file_path, 'r') as f:
        requirements = [line.strip() for line in f.readlines() if not line.startswith('#')]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='general_mlops',
    version='0.1',
    author='mouli',
    author_email='moulisai.2296@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)