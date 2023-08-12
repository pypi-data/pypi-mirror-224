# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seabird_processing']

package_data = \
{'': ['*']}

install_requires = \
['pydantic-settings>=2.0.2,<3.0.0', 'pydantic>=2.1.1,<3.0.0']

setup_kwargs = {
    'name': 'seabird-processing',
    'version': '0.2.0',
    'description': 'Python interface for calling Seabird CTD processing commands',
    'long_description': '# Seabird-Processing\n\nPython bindings for executing Seabird SBE processing tools.\n\n## Description\n\nThis library contains an API for executing seabird SBE processing modules on Seabird\ndata files (hex and cnv). The modules all accept text as input which allows for more\nconvenient access to the command line functions which would normally require a file path\nas input. Under the hood, this library simply saves temporary files which are then\nprocessed through SBE, read into memory, and returned as in-memory text.\n\n## Installation\n\n### Pre-requisites\n\nAn installation of\nthe [Seabird Processing Suite](http://www.seabird.com/software/software) is required to\nrun these modules since they simply provide an abstraction of the command line tools\nprovided by Seabird.\n\n### Install with pip\n\nTo install this tool in your current python environment do:\n\n```pip install seabird-processing```\n\nConfigure the tool with the location of your Seabird Processing Suite installation by\nsetting the `SBE_BIN_DIR` environment variable. For example, if you installed the\nsoftware to `C:\\Program Files (x86)\\Seabird\\SBEDataProcessing-Win32` then you would set\nthe environment\nvariable `SBE_BIN_DIR=C:\\Program Files (x86)\\Seabird\\SBEDataProcessing-Win32\\`.\nBy default, it is assumed that the software is installed\nto `C:\\Program Files (x86)\\Seabird\\SBEDataProcessing-Win32`.\n\n## Usage\n\nThere are two ways to use this library. The first is to use individual functions which\ncorrespond one-to-one with the SBE processing modules. The second is to use\nthe `Pipeline`\nclass which allows you to chain together multiple processing modules.\n\n### Command line functions\n\n```python\nfrom seabird_processing import dat_cnv, filter_\n\nxmlcon = \'./xmlcon/19-7467.xmlcon\'\n\ncnvfile = dat_cnv(\'./seabird_data_file.hex\', \'./output/dir\', xmlcon, \'./psa/DatCnv.psa\')\n# "filter" is a reserved keyword, so this function is called "filter_"\nfiltered = filter_(cnvfile, \'./output/dir\', xmlcon, \'./psa/AlignCTD.psa\')\n# ...\n```\n\n### Batch processing\n\n```python\nfrom seabird_processing import Batch, configs\n\nxmlcon = \'./path/to/xmlcon/12-3456.xmlcon\'\n\n# Create a pipeline with some config files\nbatch = Batch([\n    configs.DatCnvConfig(\n        # `output_file_suffix` is optional\n        output_dir="./datcnv", output_file_suffix="_datcnv",\n        xmlcon=xmlcon, psa=\'./path/to/DatCnv.psa\'),\n    configs.FilterConfig(\n        output_dir="./filter", output_file_suffix="_filter",\n        xmlcon=xmlcon, psa=\'./path/to/Filter.psa\'),\n    configs.AlignCTDConfig(\n        output_dir="./alignctd", output_file_suffix="_alignctd",\n        xmlcon=xmlcon, psa=\'./path/to/AlignCTD.psa\'),\n    configs.CellTMConfig(\n        output_dir="./celltm", output_file_suffix="_celltm",\n        xmlcon=xmlcon, psa=\'./path/to/CellTM.psa\'),\n    configs.LoopEditConfig(\n        output_dir="./loopedit", output_file_suffix="_loopedit",\n        xmlcon=xmlcon, psa=\'./path/to/LoopEdit.psa\'),\n    configs.DeriveConfig(\n        output_dir="./derive", output_file_suffix="_derive",\n        xmlcon=xmlcon, psa=\'./path/to/Derive.psa\'),\n    configs.DeriveTEOS10Config(\n        output_dir="./deriveteos10", output_file_suffix="_deriveteos10",\n        xmlcon=xmlcon, psa=\'./path/to/DeriveTEOS_10.psa\'),\n    configs.BinAvgConfig(\n        output_dir="./binavg", output_file_suffix="_binavg",\n        xmlcon=xmlcon, psa=\'./path/to/BinAvg.psa\'),\n])\n\nbatch.run("./*.hex")\n\n# You may also run an individual Config object\nconverter = configs.DatCnvConfig(\n    output_dir="./datcnv", output_file_suffix="_datcnv",\n    xmlcon=xmlcon, psa=\'./path/to/DatCnv.psa\'\n)\nconverter.run("./some/file.hex")\n```\n\n### Copyright and Licensing Information\n\nSee [LICENSE](./LICENSE) for details.\n\n### Bugs / Feature requests\n\nPlease file bug reports and feature requests on GitHub. We also welcome pull requests\nto add functionality or fix bugs!\n',
    'author': 'Taylor Denouden',
    'author_email': 'taylor.denouden@hakai.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
