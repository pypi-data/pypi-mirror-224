from setuptools import setup, find_packages

VERSION = '0.0.9'
DESCRIPTION = 'Utility functions/wrapper for psycopg2 python package'
LONG_DESCRIPTION = 'Python package that extends basic functionality for interacting with PostgreSQL databases. ' \
                   'It\'s built on top of the psycopg2 library, providing an easier and more streamlined interface.'

# Setting up
setup(
    name="psycopg2_utility_functions",
    version=VERSION,
    author="qxh5696",
    author_email="qxh5696@g.rit.edu",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=['psycopg2-binary'],
    keywords=['python', 'database', 'postgresql', 'psql'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
