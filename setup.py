from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import setup


version = '1.0.0'

setup(
    author='Tim Martin',
    author_email='tim.martin@vertical-knowledge.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'awshucks = awshucks:awshucks'
        ]
    },
    name='awshucks',
    py_modules=['awshucks'],
    version=version,
)
