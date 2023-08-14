import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'regexpro'
AUTHOR = 'Saurav'
AUTHOR_EMAIL = 'pysaurav@gmail.com'
URL = 'https://github.com/pysaurav/regexpro'
LICENSE = 'MIT License'
DESCRIPTION = 'Prebuilt regex validators'
LONG_DESCRIPTION = ''

INSTALL_REQUIRES = []

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      keywords=['prebuilt validator', 'regex validator'],
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      classifiers=[
              "Programming Language :: Python :: 3",
              "License :: OSI Approved :: MIT License",
              "Operating System :: OS Independent",
          ],
      )
