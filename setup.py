# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flipboard']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'pyperclip>=1.8.1,<2.0.0', 'xmlformatter>=0.2.2,<0.3.0']

entry_points = \
{'console_scripts': ['flipboard = flipboard.cli:cli']}

setup_kwargs = {
    'name': 'flipboard',
    'version': '0.1.0',
    'description': 'Apply transformations to text on the clipboard',
    'long_description': '# flipboard\n\nWIP project\n\nCLI lib for applying useful transformations to text on the clipboard\n',
    'author': 'chris48s',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chris48s/flipboard',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
