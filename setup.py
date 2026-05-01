from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(name="ML-OPS_Project1",
      version="0.1.0",
      author="Maddy",
      packages=find_packages(),
      install_requires=requirements,
      description="A machine learning project for MLOps course",
)