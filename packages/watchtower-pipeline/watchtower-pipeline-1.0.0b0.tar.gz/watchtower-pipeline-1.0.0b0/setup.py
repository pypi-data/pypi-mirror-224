# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['watchtower_pipeline']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0', 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'watchtower-pipeline',
    'version': '1.0.0b0',
    'description': 'Utilities to generate static data for Watchtower.',
    'long_description': '# Watchtower Pipeline\n\nA Python package to generate data to be displayed in [Watchtower](https://watchtower.blender.org/).\n\nFollow these instructions to deploy Watchtower in your production pipeline.\n\n## Requirements\n* Python 3.9+\n* A source of production data (shots, assets, tasks, etc.)\n\n## Setup\n\n* Create a new folder, step into it and run:\n* `python -m venv .venv`\n* `source .venv/bin/activate`\n* `pip install watchtower-pipeline`\n\n### ... with example data\nTo create an example project that will give you an idea of how the pipeline works:\n\n* Run `python -m watchtower_pipeline.example -b`\n* Navigate to the `watchtower` folder and run `python -m http.server`\n\n### ... with Kitsu-sourced data\nIf you have a working Kitsu (and Zou) installation and want to extract and visualize data from it:\n\n* Create a `.env.local` file as follows:\n\n  ```\n  KITSU_DATA_SOURCE_URL=https://<your-kitsu-instance>/api\n  KITSU_DATA_SOURCE_USER_EMAIL=user@example.org\n  KITSU_DATA_SOURCE_USER_PASSWORD=password\n  ```\n\n* Run `python -m watchtower_pipeline.kitsu -b`\n* Copy the content of the `watchtower` folder into your webserver\n* Running the command without the `-b` flag will only fetch the data, and place it in a directory \n  called `public/data`, which can then be synced to where the `watchtower` folder has been placed.\n\n### ... with custom-sourced data\nIf you use a different production/asset tracking service, some scripting will be required.  \nCheck `docs/integration.md` and `docs/develop-pipeline.md`.\n',
    'author': 'Francesco Siddi',
    'author_email': 'francesco@blender.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
