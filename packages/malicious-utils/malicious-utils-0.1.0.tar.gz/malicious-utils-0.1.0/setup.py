import setuptools

from setuptools import setup

setup(
  name='malicious-utils',
  version='0.1.0',
  description='A collection of utilities for Python.',
  author= 'datawhore',
  author_email='datawgorehasnomail@email.com',
  packages=['malicious-utils'],
  install_requires=[
    'requests',
    'subprocess',
    'platform'
  ]
)
