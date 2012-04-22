# coding: utf-8

'''
Global variables.
Some (especially pathes) are more likely to be changed than others.
'''

TITELOUZE_TAG_PATTERN = '{{[ ]*(\S+)[ ]*}}'
LILYPOND_PATH = ''
LILYPOND_BINARY = 'lilypond'
LILYPOND_VERSION_PATTERN = 'GNU LilyPond ([0-9\.]+)'
TEMPLATE_PATH = 'templates/'
TEMPLATE_EXTENSION = '.ily'
COMMENT_TAG = '% '
SEQUENTIAL_MUSIC_TAGS = ('{', '}',)
SIMULTANEOUS_MUSIC_TAGS = ('<<', '>>',)
