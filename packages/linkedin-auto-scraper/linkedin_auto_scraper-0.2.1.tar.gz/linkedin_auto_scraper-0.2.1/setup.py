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
    'version': '0.2.1',
    'description': 'A tool to scrape infomation of people in a particular based on their job title and location',
    'long_description': '\n# LinkedIn Auto Scraper\n\nLinkedIn Auto Scraper is a command-line application designed to scrape cleaned information from LinkedIn profiles based on job titles and locations. The app offers two main commands: `login` and `scrape`. Once you\'ve logged in using the `login` command, you can perform continuous scraping without the need to log in again, thanks to the authentication caching feature.\n\n## Table of Contents\n\n-   [Installation](https://chat.openai.com/c/b42c6a84-5afc-4a4e-a9ae-23be4b649973#installation)\n-   [Usage](https://chat.openai.com/c/b42c6a84-5afc-4a4e-a9ae-23be4b649973#usage)\n    -   [Login](https://chat.openai.com/c/b42c6a84-5afc-4a4e-a9ae-23be4b649973#login)\n    -   [Scrape](https://chat.openai.com/c/b42c6a84-5afc-4a4e-a9ae-23be4b649973#scrape)\n-   [Contributing](https://chat.openai.com/c/b42c6a84-5afc-4a4e-a9ae-23be4b649973#contributing)\n-   [License](https://chat.openai.com/c/b42c6a84-5afc-4a4e-a9ae-23be4b649973#license)\n\n## Installation\n\n1.  Ensure you have Python 3.x installed.\n    \n2.  Clone this repository:\n\n-   `git clone https://github.com/your-username/linkedin-auto-scraper.git` \n    \n-   Navigate to the project directory: \n    \n-   `cd linkedin-auto-scraper` \n    \n-   Install the required dependencies  \n\n\t `pip install -r requirements.txt` \n    \n\n## Usage\n\n### Login\n\nTo use the app, you need to log in first. This step is required for authentication purposes. Run the following command:\n\nbash\n\n`linkedin-auto-scraper login` \n\nThis command lets you log in to your LinkedIn account. Follow the prompts to provide your LinkedIn credentials. Your authentication will be cached to allow continuous scraping without repeated logins.\n\n### Scrape\n\nOnce you\'re logged in, you can start scraping LinkedIn profiles based on job titles and locations. Run the following command:\n\nbash\n\n`linkedin-auto-scraper scrape` \n\nBy default, the app will search for profiles related to the HR field. You can customize the search by using the following options:\n\n-   `--search` (`-s`): Specify the search parameter (default: "hr").\n-   `--location` (`-l`): Use it to search for profiles in a specific location (default: None).\n-   `--excel`: This option is required and indicates whether to generate an Excel file with the scraped data (default: no-excel).\n\nExample usage:\n\nbash\n\n`linkedin-auto-scraper scrape --search software engineer --location San Francisco --excel` \n\nFollow the prompts to enter the desired job title and location. The app will scrape and display cleaned information from LinkedIn profiles matching your criteria.\n\n## Contributing\n\nContributions are welcome! If you\'d like to contribute to the project, please follow these steps:\n\n1.  Fork the repository.\n2.  Create a new branch for your feature/bugfix: `git checkout -b feature-name`\n3.  Commit your changes: `git commit -m "Description of changes"`\n4.  Push to the branch: `git push origin feature-name`\n5.  Create a pull request.\n\n## License\n\nThis project is licensed under the [MIT License]\n',
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
