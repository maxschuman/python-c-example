from setuptools import setup

setup(
   name='maxpysort',
   version='0.1.0',
   author='Max Schuman',
   packages=['maxpysort'],
   description='Demonstration package for connect Python and C code',
   long_description=open('README.md').read(),
   install_requires=[
       "numpy"
   ]
)
