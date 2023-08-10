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
    'version': '0.1.0',
    'description': 'Async Python SDK wrapper for Outline Manager VPN',
    'long_description': '# Async outline manager sdk\n\n> Thanks for the reverse engineering project https://github.com/jadolg/outline-vpn-api\n\n# Example:\n\n```python\nfrom outline_manager_sdk import OutlineVPN\n\n# Setup the access with the API URL (Use the one provided to you after the server setup)\nclient = OutlineVPN(api_url="https://127.0.0.1:51083/xlUG4F5BBft4rSrIvDSWuw",\n                    cert_sha256="4EFF7BB90BCE5D4A172D338DC91B5B9975E197E39E3FA4FC42353763C4E58765")\n\n# Get all access URLs on the server\nfor key in client.get_keys():\n    print(key.access_url)\n\n# Create a new key\nnew_key = client.create_key()\n\n# Rename it\nclient.rename_key(new_key.key_id, "new_key")\n\n# Delete it\nclient.delete_key(new_key.key_id)\n\n# Set a monthly data limit for a key (20MB)\nclient.add_data_limit(new_key.key_id, 1000 * 1000 * 20)\n\n# Remove the data limit\nclient.delete_data_limit(new_key.key_id)\n```\n\n',
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
