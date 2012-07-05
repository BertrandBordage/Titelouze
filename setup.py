#! /usr/bin/env python
# coding: utf-8

from distutils.core import setup

setup(
    name='Titelouze',
    version='0.1.2',
    author='Bertrand Bordage',
    author_email='bordage.bertrand@gmail.com',
    url='https://github.com/BertrandBordage/Titelouze',
    packages=('titelouze',),
    package_data={'titelouze': ['templates/*.ily']},
    license='Creative Commons Attribution Non-Commercial Share Alike',
    description='Framework to easily build LilyPond books.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: Free for non-commercial use',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Artistic Software',
    ],
)
