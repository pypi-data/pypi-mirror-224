from setuptools import setup, find_packages

setup(
    name='glag',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'json'
    ],
)

