# -*- coding: utf-8 -*-
"""Setup module for flask taxonomy."""
import os

from setuptools import setup

readme = open('README.rst').read()

DATABASE = "postgresql"
INVENIO_VERSION = "3.1.0"

install_requires = [
    'invenio[{db},base]~={version}'.format(
        db=DATABASE, version=INVENIO_VERSION),
]

tests_require = [
    'pytest>=4.6.3',
    'pytest-invenio>=1.0.2,<1.1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
]

extras_require = {
    'tests': tests_require,
}

setup_requires = [
    'pytest-runner>=2.7',
]

g = {}
with open(os.path.join('invenio_oarepo_dc', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name="invenio_oarepo_dc",
    version=version,
    url="https://github.com/oarepo/invenio-oarepo-dc",
    license="MIT",
    author="Miroslav Simek",
    author_email="miroslav.simek@vscht.cz",
    description="DCTerms support for OARepo (just selected props)",
    zip_safe=False,
    packages=['invenio_oarepo_dc'],
    entry_points={
        'invenio_search.templates': [
            'invenio_oarepo_dc = invenio_oarepo_dc.templates:get_templates',
        ],
        'invenio_jsonschemas.schemas': [
            'invenio_oarepo_dc = invenio_oarepo_dc.jsonschemas'
        ],
    },
    include_package_data=True,
    setup_requires=setup_requires,
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
    ],
)
