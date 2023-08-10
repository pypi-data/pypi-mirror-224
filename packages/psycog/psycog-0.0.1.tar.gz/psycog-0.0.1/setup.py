# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['psycog']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'psycog',
    'version': '0.0.1',
    'description': 'A tool for performing psychophysical and cognitive experiments.',
    'long_description': "# Psychophysics and Cognition (`psycog`)\n\nThis software is for measuring psychophysical and cognitive abilities in humans. I use it\nfor my own research, but it is open source and freely available for anyone to use.\n\n## Installation\n\n### Python Package\n\n`psycog` is a Python package. You can install it using `pip`:\n\n```bash\n\npip install psycog\n\n```\n\nDue to the large number of dependencies, it is strongly recommended that you install \n`psycog` in a fresh [virtual environment](https://docs.python.org/3/tutorial/venv.html).\n\n### Standalone Executable\n\nI intend to make `psycog` available as a standalone executable in the future. This will\nallow you to run experiments without having to install Python or any dependencies, though\nthe executable will be quite large (~1GB). This is not yet available.\n\n## Usage\n\n### Command Line\n\n`psycog` is GUI-based. To run it, simply type `psycog` into the command line. This will\nopen the main menu, from which you can select the experiments you wish to run.\n\n### Python\n\nYou can also run the GUI from inside a Python REPL or script, though I'm not sure why you\nwould want to do this.\n\n```python\n\nfrom psycog import run\n\nrun()\n\n```\n",
    'author': 'Sam Mathias',
    'author_email': 'samuel.mathias@childrens.harvard.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
