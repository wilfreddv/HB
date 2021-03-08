from setuptools import setup
import os

HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = 'pyutil'
VERSION = '0.1'
URL = 'https://github.com/wilfred-kun/HB'


with open('README') as f:
    README = f.read()


setup(name=PACKAGE_NAME,
      version=VERSION,
      url=URL,
      description='Collection of code',
      long_description=README,
      long_description_content_type="text/markdown",
      author='wilfred-kun',
      python_requires='>=3.6',
      entry_points={'console_scripts':
            [
                'selector = pyutil.selector:main'
            ]
        }
    )
