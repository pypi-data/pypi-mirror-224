# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['second_python_package']

package_data = \
{'': ['*']}

install_requires = \
['cython>=3.0.0,<4.0.0', 'flake8>=6.1.0,<7.0.0', 'termcolor>=2.3.0,<3.0.0']

entry_points = \
{'console_scripts': ['harmony = second_python_package.harmony:main']}

setup_kwargs = {
    'name': 'pubpypack-harmony-tpotjj',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Joris Jansen',
    'author_email': 'joris97jansen@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}
from build_cython import *
build(setup_kwargs)

setup(**setup_kwargs)
