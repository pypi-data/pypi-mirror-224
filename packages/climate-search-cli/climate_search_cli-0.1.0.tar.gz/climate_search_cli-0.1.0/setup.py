# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cs', 'cs.load']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.6,<9.0.0',
 'numpy==1.24.4',
 'pandas>=2.0.3,<3.0.0',
 'scikit-learn>=1.3.0,<2.0.0',
 'sqlalchemy>=2.0.19,<3.0.0']

entry_points = \
{'console_scripts': ['cs = cs.cli:entrypoint']}

setup_kwargs = {
    'name': 'climate-search-cli',
    'version': '0.1.0',
    'description': 'A python program that can be run from the command line, and used to search climate policy documents.',
    'long_description': "# climate-search-cli\nA python program that can be run from the command line, and used to search climate policy documents.\n\n## Task Overview\n\nCreated as an interview technical challenge. The task is to create a cli tool that can be used to search summaries of climate documents. \n\nThe cli needed to have the following functionality:\n\n- Load & validate documents into a database at the command line\n- Query the documents returning a sequence of document objects\n- Display the documents and some statistics about them as output\n- Order by relevance using a relevancy score\n\n## Evaluation Criteria\n\nThe following are the items that are being evaluated:\n\n- Readability\n- Maintainability\n- Functionality\n- Efficiency\n- Modularity\n- Commenting and documentation\n- Testing Strategy\n\n\n## Overview\n\nRun poetry to install dependencies, (see below for other ways of running):\n```\npoetry install\npoetry shell\n```\n\nData can be loaded via:\n```\ncs load\n```\n\nThis will also output errors to the same directory, and load the data into a database. A custom file can alsi be loaded using the --localpath argument. \n\nData can then by queried by passing keywords with the retrieve command:\n\n```\ncs retrieve -k green -k energy\n```\n\nThis will display the policies that match. Results can also be sorted with:\n\n```\ncs retrieve -k forests --sort\n```\n\n\n## Time taken\n\nI worked intermittently on this over the course of a couple of days. I think the total time actively working on the solution was about 6 hours. (Not including time spent reading the brief, researching and planning). I could keep going, but I went over the suggested timeframe, so leaving it here. Some key items I'd like to improve include error handling and the relevency algorithm.\n\n## alternate ways of running\n\n### Docker\n\nThis can also be run via docker:\n\n```\ndocker build -t climate-search-cli:latest .\n```\n\n```\ndocker run climate-search-cli:latest load\ndocker run climate-search-cli:latest retrieve -k cycling -k health --sort\n```\n",
    'author': 'fred oloughlin',
    'author_email': 'fred@oloughl.in',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
