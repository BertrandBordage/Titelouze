#! /usr/bin/env python
# coding: utf-8

from distutils.core import setup

setup(
    name='Titelouze',
    version='0.1',
    author='Bertrand Bordage',
    author_email='bordage.bertrand@gmail.com',
    packages=('titelouze',),
    package_data={'titelouze': ['templates/*.ily']},
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Framework to easily build LilyPond books.',
    long_description=open('README.rst').read(),
)
