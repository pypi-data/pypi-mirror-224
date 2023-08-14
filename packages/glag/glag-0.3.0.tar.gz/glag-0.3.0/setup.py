# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['glag']
setup_kwargs = {
    'name': 'glag',
    'version': '0.3.0',
    'description': 'glag',
    'long_description': 'glag\n',
    'author': 'Keith Griffon',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
