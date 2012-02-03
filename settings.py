# coding: utf-8

'''
Global variables.
Some (especially pathes) are more likely to be changed than others.
'''

TAGS_PATTERN = '{{ (\S+) }}'
LILYPOND_PATH = ''
LILYPOND_COMMAND = LILYPOND_PATH + 'lilypond'
LILYPOND_VERSION_PATTERN = 'GNU LilyPond ([0-9\.]+)'
INDENT_UNIT = '  '
COMMENT_TAG = '% '
SEQUENTIAL_MUSIC_TAGS = ('{', '}',)
SIMULTANEOUS_MUSIC_TAGS = ('<<', '>>',)

