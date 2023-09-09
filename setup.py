from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    This function will return the list of requirement
    '''
    requirement = []
    with open(file_path) as file_obj:
       requirement = file_obj.readlines()
       requirement =  [req.replace("\n","")for req in requirement]
                       
    if HYPHEN_E_DOT in requirement:
           requirement.remove(HYPHEN_E_DOT)

    return requirement

setup(
    name = 'Social media sentiment analysis',
    version = '0.0.1',
    author = 'Rabiya Kouser R',
    author_email = 'rabiyakouser10234@gmail.com',
    packages = find_packages(),
    install_requires = get_requirement('requirement.txt')
)