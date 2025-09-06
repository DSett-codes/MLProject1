from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements: List[str] = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()
            # skip empty lines, comments and editable/install markers
            if not req or req.startswith('#'):
                continue
            if req.startswith('-e') or req == HYPEN_E_DOT:
                continue
            requirements.append(req)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Debmalya',
author_email='settdebmalya273@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)