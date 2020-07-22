from setuptools import setup, find_packages

setup(name='spreadsheet-test',
      description='Sheetgo Test',
      long_description='Just a spreadsheet and image processing test',
      packages=find_packages(exclude=["*tests*"]),
      version='1.0.0',
      install_requires=[
          'Flask==1.1.2',
          'injector==0.16.0',
          'openpyxl==3.0.4',
          'pillow==7.2.0',
          'pyjwt==1.7.1'
      ],
      extras_require={
          'dev': [
              'pycodestyle>=2.6.0',
              'pytest>=5.4.3',
              'pytest-cov>=2.10.0',
              'requests-mock>=1.8.0',
              'pytest-mock>=3.1.1',
              'pytest-sugar>=0.9.3',
              'pytest-lazy-fixture>=0.6.3',
              'flake8>=3.8.3',
          ],
      }
      )
