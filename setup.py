from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Implementation of the ELO Algorithm'
LONG_DESCRIPTION = 'A Python implementation of the ELO algorithm developed by PCLA'

# Setting up
setup(
    name="pcla-elo",
    url='https://pcla.wiki/',
    version=VERSION,
    author="Michael Mogessie",
    author_email="mogessie@upenn.edu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],

    keywords=['python', 'elo'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
