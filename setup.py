#!/usr/bin/env python
install_requires = ['pybluez','gattlib']
tests_require = []
# %%
from setuptools import setup,find_packages

setup(name='pybluez-examples',
      packages=find_packages(),
      version="0.0.1",
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pybluez-examples',
      long_description=open('README.rst').read(),
      description='Examples of the versatile PyBluez module for Bluetooth from Python',
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require},
      python_requires='>=2.7',
	  )

