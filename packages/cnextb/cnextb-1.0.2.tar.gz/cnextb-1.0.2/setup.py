from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))

str_version = '1.0.2'

with open(path.join(here, 'README.txt'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='cnextb',
      version=str_version,
      description='test board developped by CNEXLABS',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      python_requires='>=3')
