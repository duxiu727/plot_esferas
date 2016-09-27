# # File: setup.py
# #
# # This file is part of the plot_esferas project


"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup  # , find_packages
# To use a consistent encoding
from codecs import open
from os import path

VERSION = '0.2'
here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
  long_description = f.read()

setup(
    name='plot_esferas',

    version=VERSION,

    description='Use spheres as markers in matplotlib scatter plots',
    long_description=long_description,

    # The project's main homepage.
    url="https://github.com/fiolj/plot_esferas",

    # Author details
    author="Juan Fiol",
    author_email="juanfiol@gmail.com",

    # Choose your license
    license="GPLv3",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Users',
        'Topic :: Plotting',

        # # Pick your license as you wish (should match "license" above)
        # 'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords="matplotlib plot spheres",

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    packages=["plt_esfera"],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'plt_esfera': ['sphere.png'],
    },

)
