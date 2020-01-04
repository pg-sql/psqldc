from setuptools import find_packages
from setuptools import setup

setup(
    name='postgresql-dc',
    license='BSD-3-Clause',
    description='PostgreSQL Database Changelog',
    long_description='....',
    author='Christophe CHAUVET',
    author_email='christophe.chauvet@gmail.com',
    url='https://github.com/pg-sql/psqldc',
    packages=['psqldc'],
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'psycopg2',
        'lxml',
    ],
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    python_requires='>=3.5',
    use_scm_version=True,
    setup_requires=[
        'pytest-runner',
        'setuptools_scm'
    ],
)