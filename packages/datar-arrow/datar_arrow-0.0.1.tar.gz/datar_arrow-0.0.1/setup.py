# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datar_arrow', 'datar_arrow.api']

package_data = \
{'': ['*']}

install_requires = \
['datar>=0.13,<0.14', 'pyarrow>=11,<12']

entry_points = \
{'datar': ['arrow = datar_arrow:plugin']}

setup_kwargs = {
    'name': 'datar-arrow',
    'version': '0.0.1',
    'description': 'The pyarrow backend for datar',
    'long_description': '# datar-arrow\n\nThe pyarrow backend for [datar][1].\n\nNote that only `base` APIs are implemented.\n\n## Installation\n\n```bash\npip install -U datar-arrow\n# or\npip install -U datar[arrow]\n```\n\n## Usage\n\n```python\nfrom datar.base import ceiling\n\n# without it\nceiling(1.2)  # NotImplementedByCurrentBackendError\n\n# with it\nceiling(1.2)  # 2\n```\n\n[1]: https://github.com/pwwang/datar\n',
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
