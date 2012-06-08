# coding: utf-8

'''
Global variables.
Some (especially pathes) are more likely to be changed than others.
'''

import os.path

TITELOUZE_TAG_PATTERN = r'{{[ ]*(\S+)[ ]*}}'
LILYPOND_PATH = ''
LILYPOND_BINARY = 'lilypond'
LILYPOND_VERSION_PATTERN = 'GNU LilyPond ([0-9\.]+)'
TEMPLATE_PATH = 'templates/'
TEMPLATE_ABSPATH = os.path.join(os.path.dirname(__file__), TEMPLATE_PATH)
TEMPLATE_EXTENSION = '.ily'
COMMENT_TAG = '% '
SEQUENTIAL_MUSIC_TAGS = ('{', '}',)
SIMULTANEOUS_MUSIC_TAGS = ('<<', '>>',)
