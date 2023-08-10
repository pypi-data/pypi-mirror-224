# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['txtadv',
 'txtadv.color',
 'txtadv.commands',
 'txtadv.file',
 'txtadv.location',
 'txtadv.messaging',
 'txtadv.wip.multiplayer']

package_data = \
{'': ['*'], 'txtadv': ['saves/*']}

setup_kwargs = {
    'name': 'txtadv',
    'version': '1.0b3',
    'description': 'A feature-rich text adventure library! Easy to code in and relativly intuitive, perfect for beginners!',
    'long_description': "# txtadv\n\ntxtadv is a feature-rich text adventure library! Easy to code in and relativly intuitive, perfect for beginners! Just install the library, with no dependencies other then the built-in libraries, for all computers.\n\nDocumentation is on it's way, I just wanted to get something out!",
    'author': 'sdft',
    'author_email': 'averse.abfun@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/txtadv',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
