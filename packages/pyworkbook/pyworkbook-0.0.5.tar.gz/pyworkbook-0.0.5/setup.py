# coding=utf-8
from setuptools import setup, find_packages

# with open("jupyter_workbook/README.md", "r") as f:
#     long_description = f.read()

VERSION = '0.0.5'
DESCRIPTION = 'Erweiterung für Jupyter Notebooks für den Informatik Unterricht'
long_description = DESCRIPTION

# Setting up
setup(
    name="pyworkbook",
    version=VERSION,
    author="Stefan Hickl",
    author_email="<kontakt@stefanhickl.de>",
    license="MIT",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    # url="github-url",
    install_requires=['Flask>=2.3.2', 'ipython>=8.9.0', 'ipywidgets>=8.1.0'],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    keywords=['python', 'jupyter', 'school'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Education",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)