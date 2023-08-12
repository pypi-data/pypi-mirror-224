# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spaces', 'spaces.gpu']

package_data = \
{'': ['*']}

install_requires = \
['gradio>=3.2,<4.0',
 'psutil>=2,<6',
 'requests>=2.19,<3.0',
 'typing-extensions>=4,<5']

setup_kwargs = {
    'name': 'spaces',
    'version': '0.12b2',
    'description': 'Utilities for Hugging Face Spaces',
    'long_description': '# Hugging Face Spaces\n\n## Installation\n\n`pip install spaces`\n',
    'author': 'Charles Bensimon',
    'author_email': 'charles@huggingface.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://huggingface.co',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
