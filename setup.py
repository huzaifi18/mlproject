from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(path:str)->List[str]:
    """this function will return the list of requirements

    Args:
        path (str): file path

    Returns:
        List[str]: list of requirements
    """
    requirements = []
    with open(path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(
    name="mlproject",
    version="0.0.1",
    author="Huzaifi",
    author_email="huzaifiok@gmail.com",
    packages=find_packages(),
    url="https://github.com/huzaifi18/mlproject",
    license="MIT",
    install_requires=get_requirements('requirements.txt'),
    
)