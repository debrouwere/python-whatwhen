import os
from setuptools import setup, find_packages
setup(name='whatwhen',
      version='0.1.1',
      description=("A higher-level topological sort."),
      long_description=open('README.rst').read(),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'
                    ],
      keywords='topological sort toposort topsort dependencies dependency resolver',
      author='Stijn Debrouwere',
      author_email='stijn@debrouwere.org',
      download_url='http://www.github.com/debrouwere/python-whatwhen/tarball/master',
      license='ISC',
      test_suite='whatwhen.tests',
      packages=find_packages(),
      )