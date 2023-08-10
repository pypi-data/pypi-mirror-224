# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['outline_sdk']

package_data = \
{'': ['*']}

install_requires = \
['aio-clients>=2.0.0,<3.0.0',
 'pyrogram>=2.0.106,<3.0.0',
 'uvloop>=0.17.0,<0.18.0']

setup_kwargs = {
    'name': 'outline-sdk',
    'version': '0.1.1',
    'description': 'Async Python SDK wrapper for Outline Manager VPN',
    'long_description': '# Async outline manager sdk\n\n> Thanks for the reverse engineering project https://github.com/jadolg/outline-vpn-api\n\n# Example:\n\n```python\nfrom outline_sdk import OutlineClient\n\n# Setup the access with the API URL (Use the one provided to you after the server setup)\nclient = OutlineClient(\n    url="https://127.0.0.1:51083/xlUG4F5BBft4rSrIvDSWuw/",  # <--- `/` is required \n    cert_sha256="4EFF7BB90BCE5D4A172D338DC91B5B9975E197E39E3FA4FC42353763C4E58765"\n)\n\n# Get all access URLs on the server\nfor key in await client.get_keys():\n    print(key)\n\n# Create a new key\nnew_key = await client.create_key()\n\n# Rename it\nawait client.rename_key(1, "new_key")\n\n# Delete it\nawait client.delete_key(1)\n\n# Set a monthly data limit for a key (20MB)\nawait client.add_data_limit(1, 1000 * 1000 * 20)\n\n# Remove the data limit\nawait client.delete_data_limit(1)\n```\n\n',
    'author': 'Denis Malin',
    'author_email': 'denis@malina.page',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
