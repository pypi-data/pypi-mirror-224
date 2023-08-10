# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['argus_dynamixel']

package_data = \
{'': ['*']}

install_requires = \
['dynamixel-sdk>=3.7.31,<4.0.0', 'python-dotenv>=0.18.0,<0.19.0']

setup_kwargs = {
    'name': 'argus-dynamixel',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Alan Vasquez',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
