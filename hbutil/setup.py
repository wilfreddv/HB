from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = 'hbutil'
VERSION = '0.1'
URL = 'https://github.com/wilfreddv/HB'


with open('README.md') as f:
    README = f.read()


setup(name=PACKAGE_NAME,
      version=VERSION,
      url=URL,
      description='Collection of code',
      long_description=README,
      long_description_content_type="text/markdown",
      author='wilfreddv',
      packages=find_packages(exclude=[]),
      python_requires='>=3.6',
      entry_points={'console_scripts':
            [
                'selector = hbutil.selector:main'
            ]
        }
    )
