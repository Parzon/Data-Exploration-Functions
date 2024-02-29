from setuptools import setup, find_packages

setup(
    name='pytools',
    version='0.1',
    packages=find_packages(),
    description='A collection of utility functions for data analysis',
    author='Parzon',
    author_email='parzon7l@gmail.com',
    install_requires=[
        'pandas>=1.0',
        'numpy>=1.18',
        'matplotlib>=3.2',
        'seaborn>=0.10',
        'scikit-learn>=0.22',
    ],
)
