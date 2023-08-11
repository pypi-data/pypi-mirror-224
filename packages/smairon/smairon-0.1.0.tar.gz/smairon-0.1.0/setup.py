# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smairon']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'smairon',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Hello',
    'author': 'Feofilaktov, Sergey',
    'author_email': 'man@smairon.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
