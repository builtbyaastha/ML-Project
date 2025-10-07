from setuptools import setup, find_packages

def get_requirements(file_path:str)->list[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements

setup(
    name='my_project',
    version='0.1.0',
    author='Aastha',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)