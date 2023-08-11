# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bootloader',
 'bootloader.utils',
 'bootloader.utils.cli',
 'bootloader.utils.maya']

package_data = \
{'': ['*']}

install_requires = \
['perseus-core-library>=1.19.4,<2.0.0',
 'perseus-getenv-library>=1.0.4,<2.0.0',
 'pygifsicle>=1.0.7,<2.0.0']

entry_points = \
{'console_scripts': ['maya-convert = bootloader.utils.cli.converter:main']}

setup_kwargs = {
    'name': 'bootloader-maya-utils-library',
    'version': '1.0.0',
    'description': 'Bootloader Maya Utilities Library',
    'long_description': "# Bootloader Maya Utilities Python Library\nPython library and Command-line Interface (CLI) to convert Maya animation files to animated GIF file, and other useful features.\n\nThis library requires both [Autodesk Maya](https://www.autodesk.com/products/maya/overview) and [gifsicle](https://www.lcdf.org/gifsicle/) to be installed.\n\n_Note: You shouldn't need to have a license for Maya to use this library._\n",
    'author': 'Daniel CAUNE',
    'author_email': 'daniel.caune@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bootloader-studio/bootloader-maya-utils-python-library',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
