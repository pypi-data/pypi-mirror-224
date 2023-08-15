from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Module for auto-naming unique constraint.'


setup(
    name='django-suc',
    version=VERSION,
    author='Yun Chin',
    author_email='razzzer@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['django'],
    keywords=[],
)
