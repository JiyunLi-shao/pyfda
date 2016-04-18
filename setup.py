# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
#from pyfdax import __version__

# @todo: WIP see https://packaging.python.org/en/latest/index.html


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

version_nr = {}
with open("version.py") as fp:
    exec(fp.read(), version_nr)

setup(
    name = 'pyfda',
    # see PEP440 for versioning information
    version = version_nr['__version__'],
    description = ('pyFDA is a tool for designing and analysing discrete time '
                 'filters written in python with a graphical user interface.'),
    long_description = long_description,
    keywords = ["digital", "discrete time", "filter design", "IIR", "FIR", "GUI"],
    url = 'https://github.com/chipmuenk/pyFDA',
    author = 'Christian Muenker',
    author_email = '',
    license = 'Apache',
    # automatically find top-level package and sub-packages input_widgets, 
    # plot_widgets etc.:
    packages = find_packages(exclude=('contrib', 'docs', 'test')),
    package_data = {'pyfda': ['images/icons/*']},
    data_files = [('pyfda',['pyfda/pyfda_log.conf']),
        ('pyfda/filter_design', ['pyfda/filter_design/filter_list.txt'])],
    # link the executable pyfdax to running the python function main() in the
    # pyfdax module:
    entry_points = {
        'console_scripts': [
            'pyfdax = pyfda.pyfdax:main',
        ]
    }
)


"""
On non-Windows platforms (using "setup.py install", "setup.py develop", 
or by using EasyInstall), a "pyfdax" script will be installed that imports 
"main" from pyfdax.py. main() is called with no arguments, and the
return value is passed to sys.exit(), so an errorlevel or message to print 
to stderr could be provided (not implemented yet).

On Windows, a set of pyfdax.exe and pyfda_gui.exe launchers are created, 
alongside a set of pyfdax.py and pyfda_gui.pyw files. The .exe wrappers find 
and execute the right version of Python to run the .py or .pyw file.
"""
# http://locallyoptimal.com/blog/2014/03/14/executable-python-scripts-via-entry-points/

