from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT-8",
    version="0.1",
    author="Kushal",
    packages=find_packages(),
    install_requires = requirements,
)