# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linkedin_auto_scraper', 'linkedin_auto_scraper.utils']

package_data = \
{'': ['*']}

install_requires = \
['about-time>=4.2.1,<5.0.0',
 'alive-progress>=3.1.4,<4.0.0',
 'async-generator>=1.10,<2.0',
 'attrs>=23.1.0,<24.0.0',
 'black>=23.7.0,<24.0.0',
 'certifi>=2023.7.22,<2024.0.0',
 'charset-normalizer>=3.2.0,<4.0.0',
 'click>=8.1.6,<9.0.0',
 'colorama>=0.4.6,<0.5.0',
 'commonmark>=0.9.1,<0.10.0',
 'exceptiongroup>=1.1.2,<2.0.0',
 'fake-useragent>=1.2.1,<2.0.0',
 'grapheme>=0.6.0,<0.7.0',
 'h11>=0.14.0,<0.15.0',
 'idna>=3.4,<4.0',
 'isort>=5.12.0,<6.0.0',
 'mypy-extensions>=1.0.0,<2.0.0',
 'numpy>=1.25.2,<2.0.0',
 'outcome>=1.2.0,<2.0.0',
 'packaging>=23.1,<24.0',
 'pandas>=2.0.3,<3.0.0',
 'pathspec>=0.11.2,<0.12.0',
 'platformdirs>=3.10.0,<4.0.0',
 'pydantic>=2.1.1,<3.0.0',
 'pygments>=2.16.1,<3.0.0',
 'pysocks>=1.7.1,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-dotenv>=1.0.0,<2.0.0',
 'pytz>=2023.3,<2024.0',
 'requests>=2.31.0,<3.0.0',
 'rich>=13.5.2,<14.0.0',
 'selenium>=4.11.2,<5.0.0',
 'shellingham>=1.5.0.post1,<2.0.0',
 'six>=1.16.0,<2.0.0',
 'sniffio>=1.3.0,<2.0.0',
 'sortedcontainers>=2.4.0,<3.0.0',
 'tomli>=2.0.1,<3.0.0',
 'tqdm>=4.66.0,<5.0.0',
 'trio-websocket>=0.10.3,<0.11.0',
 'trio>=0.22.2,<0.23.0',
 'typer>=0.9.0,<0.10.0',
 'typing-extensions>=4.7.1,<5.0.0',
 'urllib3>=2.0.4,<3.0.0',
 'webdriver-manager>=4.0.0,<5.0.0',
 'wsproto>=1.2.0,<2.0.0',
 'xlsxwriter>=3.1.2,<4.0.0']

entry_points = \
{'console_scripts': ['linkedin-auto-scraper = linkedin_auto_scraper.main:app']}

setup_kwargs = {
    'name': 'linkedin-auto-scraper',
    'version': '0.2.0',
    'description': 'A tool to scrape infomation of people in a particular based on their job title and location',
    'long_description': '# linkedin-auto-scraper\n',
    'author': 'kenfelix',
    'author_email': 'Kmrapper.kf@gmail.com',
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
