from setuptools import setup
from pathlib import Path
from hak.one.directory.filepaths.packages.get import f as get_packages
long_description = Path("./README.md").read_text()

setup(
  name='xgu',
  version='0.0.5',
  license='MIT',
  description='Semi-Automatic Git Tool',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author='@JohnRForbes',
  author_email='john.robert.forbes@gmail.com',
  url='https://github.com/JohnForbes/xgu',
  packages=[_[2:] for _ in list(get_packages('.'))],
  keywords='git',
  install_requires=[],
)
