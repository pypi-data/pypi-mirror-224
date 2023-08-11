# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gl']

package_data = \
{'': ['*']}

install_requires = \
['bump-pydantic>=0.6.1,<0.7.0',
 'pydantic-settings>=2.0.2,<3.0.0',
 'pydantic>=2.1.1,<3.0.0',
 'python-gitlab>=3.15.0,<4.0.0']

entry_points = \
{'console_scripts': ['gl = gl.main:main']}

setup_kwargs = {
    'name': 'gitlab-command',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Jason Viloria',
    'author_email': 'jason.viloria@optiscangroup.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
