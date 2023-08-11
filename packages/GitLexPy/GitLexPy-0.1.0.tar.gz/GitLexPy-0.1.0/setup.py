from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
  long_description = fh.read()

setup(
  name='GitLexPy',
  version='0.1.0',
  author='Ryan Jordan',
  author_email='ryan@ryanjordan.me',
  description='A Python package for generating commit messages using OpenAI',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/krjordan/GitLexPy',
  packages=find_packages(),
  install_requires=[
    'gitpython',
    'openai',
    'argparse'
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
  ],
  python_requires='>=3.6',
  entry_points={
    'console_scripts': ['gitlexpy=gitlexpy:main']
  }
)