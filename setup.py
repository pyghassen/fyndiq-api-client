from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='fyndiq-api-client',
      version=version,
      description="A Python wrapper for Fyndiq Restful API.",
      long_description="""A Python wrapper for Fyndiq Restful API.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='api wrapper fyndiq',
      author='Ghassen Telmoudi',
      author_email='ghassen.telmoudi@gmail.com',
      url='',
      license='GNU GENERAL PUBLIC LICENSE',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
