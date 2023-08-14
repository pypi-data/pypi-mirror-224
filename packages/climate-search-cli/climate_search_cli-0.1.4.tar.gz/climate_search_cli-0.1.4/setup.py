# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cs']

package_data = \
{'': ['*'], 'cs': ['data/*']}

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
    'version': '0.1.4',
    'description': 'A python program that can be run from the command line, and used to search climate policy documents.',
    'long_description': "# climate-search-cli\nA python program that can be run from the command line, and used to search climate policy documents.\n\n## Task Overview\n\nCreated as an interview technical challenge. The task is to create a cli tool that can be used to search summaries of climate documents. \n\nThe cli needed to have the following functionality:\n\n- Load & validate documents into a database at the command line\n- Query the documents returning a sequence of document objects\n- Display the documents and some statistics about them as output\n- Order by relevance using a relevancy score\n\n## Evaluation Criteria\n\nThe following are the items that are being evaluated:\n\n- Readability\n- Maintainability\n- Functionality\n- Efficiency\n- Modularity\n- Commenting and documentation\n- Testing Strategy\n\n## Run\n\nRun poetry to install dependencies, (see below for other ways of running):\n\n```\npoetry install\npoetry shell\n```\n\nData can be loaded via:\n\n```\ncs load\n```\n\nThis will also output errors to the same directory, and load the data into a database. A custom file can also be loaded using the --localpath argument. \n\nData can then be queried by passing keywords with the retrieve command:\n\n```\ncs retrieve -k green -k energy\n```\n\nThis will display the policies that match. Results can also be sorted with:\n\n```\ncs retrieve -k forests --sort\n```\n\nThe test directory contains both unit and integration tests, these can be run with pytest:\n\n```\npytest\n```\n\n## Solution Overview\n\nI decided to use click as the cli tool for this project. As well as sqlite as a backend, both of these are simple and portable, although if I could start again, I'd be keen to use a database that had support for arrays. Transformations and schema definitions where done in pandas for convenience, I originally started going down the path of having multiple tables in the database, but decided this was over optimising for what was needed with the given timeframe. Having just one table meant pandas was a straightoferward option for defining the table. The search relevency implementation is just a quick tfidf algorithm on the results.\n\n## Time taken\n\nI worked intermittently on this over the course of a couple of days. I think the total time actively working on the solution was about 6 hours. (Not including time spent reading the brief, researching and planning). I could keep going, but I went over the suggested timeframe, so I'm leaving it here. Some key items I'd like to improve include error handling and the relevancy algorithm.\n\n## alternate ways of running\n\n### Docker\n\nThis can also be run via docker:\n\n```\ndocker build -t climate-search-cli:latest .\n```\n\n```\ndocker run climate-search-cli:latest load\ndocker run climate-search-cli:latest retrieve -k cycling -k health --sort\n```\n\n### pypi\n\nAlso [available on pypi](https://pypi.org/project/climate-search-cli/):\n\n```\npip install climate-search-cli\n```\n",
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
