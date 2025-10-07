from setuptools import setup, find_packages

hyphen_e_dot = '-e .'
def get_requirements(file_path:str)->list[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name='my_project',
    version='0.1.0',
    author='Aastha',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)