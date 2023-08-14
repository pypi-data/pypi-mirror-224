# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:26:00 2023

@author: Tareq
"""

from setuptools import setup, find_packages




VERSION = '0.0.1'
DESCRIPTION = 'Satatic Functions'


# Setting up
setup(
    name="FastStatic",
    version=VERSION,
    author="Tareq Abeda",
    author_email="<TareqAbeda@outlook.com>",
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'datetime', 'logging'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)