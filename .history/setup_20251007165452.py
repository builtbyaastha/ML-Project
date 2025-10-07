from setuptools import setup, find_packages

def get_requirements()

setup(
    name='my_project',
    version='0.1.0',
    author='Aastha',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)