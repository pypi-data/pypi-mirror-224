# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['myevery', 'myevery.server']

package_data = \
{'': ['*'], 'myevery': ['static/css/*', 'static/img/*']}

install_requires = \
['fastapi>=0.101.0,<0.102.0',
 'fire>=0.5.0,<0.6.0',
 'langchain-experimental>=0.0.8,<0.0.9',
 'langchain>=0.0.258,<0.0.259',
 'loguru>=0.7.0,<0.8.0',
 'openai>=0.27.8,<0.28.0',
 'uvicorn>=0.23.2,<0.24.0']

entry_points = \
{'console_scripts': ['myevery = myevery.__main__:entrypoint']}

setup_kwargs = {
    'name': 'myevery',
    'version': '0.0.11',
    'description': 'A package to easily create and expose FastAPI services.',
    'long_description': '# myevery',
    'author': 'B. Truong',
    'author_email': 'myevery@mail.com',
    'maintainer': 'B. Truong',
    'maintainer_email': 'myevery@mail.com',
    'url': 'https://github.com/myevery-ai/myevery',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
