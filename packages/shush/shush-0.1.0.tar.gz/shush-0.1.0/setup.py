# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['shush']
setup_kwargs = {
    'name': 'shush',
    'version': '0.1.0',
    'description': 'Subprocesses in the style of shell scripts.',
    'long_description': None,
    'author': 'John Freeman',
    'author_email': 'jfreeman08@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
