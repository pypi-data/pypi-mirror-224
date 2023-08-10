# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['psycog']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'psycog',
    'version': '0.0.0',
    'description': '',
    'long_description': '',
    'author': 'Sam Mathias',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
