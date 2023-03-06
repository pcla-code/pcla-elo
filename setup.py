from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Implementation of the ELO Algorithm'
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="pcla-elo",
    url='https://pcla.wiki/',
    version=VERSION,
    author="Michael Mogessie",
    author_email="mogessie@upenn.edu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
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
