#!/usr/bin/env python3

import glob
from setuptools import setup, find_packages, Extension
import sysconfig

# Get the Python include directory
python_include_dir = sysconfig.get_path('include')

setup(
    name='lfpreviewer',
    version='0.1.1',
    description='Previewer for lfp',
    license='GPLv3',
    python_requires='>=3.6',
    install_requires=['docopt', 'attrs>=18.2.0', 'pillow'],
    include_package_data=True,
    package_data={ '': ['*.sh'] },
    packages=find_packages(),
    entry_points={ 'console_scripts': [
        'lfpreviewer=lfpreviewer.__main__:main'
    ]},
    ext_modules=[
        Extension(
            "lfpreviewer.X",
            glob.glob("lfpreviewer/X/*.c"),
            libraries=["X11", "Xext", "XRes"],
            include_dirs=[python_include_dir, "lfpreviewer/X"] # Include Python header files path
        ),
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: X11 Applications',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
