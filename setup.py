from setuptools import setup
from distutils.core import setup


from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

from distutils.core import setup
setup(
  name = 'gpt-cli-bot',
  packages = ['gpt_cli_bot'],
  version = '0.1',
  license='MIT',
  description = 'Your Command Line ChatGPT',
  author = 'Ephraim Mensah',
  author_email = 'ephraimmensah99@gmail.com',
  url = 'https://github.com/greatnessmensah/gptclibot',
  download_url = 'https://github.com/greatnessmensah/gptclibot/archive/v_01.tar.gz',
  keywords = ['CLI', 'Command Line Interface', 'Python', 'ChatGPT', 'PyPi'],
  install_requires=[
        'aiohttp',
        'aiosignal',
        'async-timeout',
        'attrs',
        'autopep8',
        'certifi',
        'charset-normalizer',
        'click',
        'click-shell',
        'exceptiongroup',
        'frozenlist',
        'idna',
        'iniconfig',
        'Markdown',
        'markdown-it-py',
        'mdurl',
        'multidict',
        'openai',
        'packaging',
        'pluggy',
        'pycodestyle',
        'Pygments',
        'pytest',
        'requests',
        'rich',
        'tomli',
        'tqdm',
        'urllib3',
        'yarl',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)