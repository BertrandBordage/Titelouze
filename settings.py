# coding: utf-8

'''
Global variables.
Some (especially pathes) are more likely to be changed than others.
'''

TITELOUZE_TAG_PATTERN = '{{[ ]*(\S+)[ ]*}}'
LILYPOND_PATH = ''
LILYPOND_COMMAND = LILYPOND_PATH + 'lilypond'
LILYPOND_VERSION_PATTERN = 'GNU LilyPond ([0-9\.]+)'
TEMPLATE_PATH = 'templates/'
TEMPLATE_EXTENSION = '.ily'
INDENT_UNIT = 2
COMMENT_TAG = '% '
SEQUENTIAL_MUSIC_TAGS = ('{', '}',)
SIMULTANEOUS_MUSIC_TAGS = ('<<', '>>',)
