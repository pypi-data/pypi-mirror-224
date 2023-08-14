# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jefferson_street_api']

package_data = \
{'': ['*']}

install_requires = \
['flask>=2.3.2,<3.0.0',
 'google-cloud-bigquery>=3.11.4,<4.0.0',
 'pytest>=7.4.0,<8.0.0',
 'setuptools>=68.0.0,<69.0.0']

setup_kwargs = {
    'name': 'jefferson-street-api',
    'version': '0.1.0',
    'description': "A set of tools for building and connecting to JSt's API.",
    'long_description': '#JStreet API\n\nThis library contains building blocks for creating REST API endpoints using Python and Google Cloud Functions.\n',
    'author': 'MAhbab',
    'author_email': 'mahfuj@jeffersonst.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
