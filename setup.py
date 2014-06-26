import os
from setuptools import setup, find_packages
version = '0.1'
README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read()
setup(name='whatwhen',
      version=version,
      description=("A higher-level topological sort."),
      long_description=long_description,
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'
                    ],
      keywords='topological sort toposort topsort dependencies dependency resolver',
      author='Stijn Debrouwere',
      author_email='stijn@stdout.be',
      download_url='http://www.github.com/newslynx/python-whatwhen/tarball/master',
      license='MIT',
      test_suite='whatwhen.tests',
      packages=find_packages(),
      )