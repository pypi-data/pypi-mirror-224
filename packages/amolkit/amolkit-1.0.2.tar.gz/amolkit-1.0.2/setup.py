import sys,os
from setuptools import setup, find_packages

try:
     with open("README.md","r") as f:
          long_description=f.read()
except:
     long_description=""
     pass

setup(name='amolkit', 
      version='1.0.2', 
      description='Library for extracting molecule information', 
      long_description=long_description,
      url='https://github.com/anmolecule/amolkit', 
      author='Anmol Kumar', 
      author_email='anmolecule@gmail.com', 
      license='BSD 3-Clause "New" or "Revised" License',
      packages=find_packages(), 
      zip_safe=False)

