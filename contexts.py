# coding: utf-8

'''
Python implementation of LilyPond contexts.
'''

from settings import *

class Context:
    def __init__(self):
        self.contexts = []
        self.message = COMMENT_TAG + 'Write here the content of this %s.' % self.name.lower() + '\n'
    name = 'Context'
    has_new = True
    allow_simultaneous_music = True
    ambiguous = False
    def add(self, context):
        self.contexts.append(context)
    def is_simultaneous(self):
        return len(self.contexts) > 1
    def tags(self):
        if self.allow_simultaneous_music and self.is_simultaneous():
            return SIMULTANEOUS_MUSIC_TAGS
        return SEQUENTIAL_MUSIC_TAGS
    def open_tag(self, indent=0):
        out = INDENT_UNIT * indent + '\\'
        if self.has_new:
            out += 'new ' + self.name
        else:
            out += self.name.lower()
        out += ' '
        out += self.tags()[0]
        out += '\n'
        new_indent = indent
        if self.ambiguous:
            new_indent += 1
            out += INDENT_UNIT * (new_indent) + SIMULTANEOUS_MUSIC_TAGS[0] + '\n'
        if not self.contexts:
            out += INDENT_UNIT * (new_indent+1) + self.message
        return out
    def close_tag(self, indent=0):
        out = ''
        if self.ambiguous:
            out += INDENT_UNIT * (indent+1) + SIMULTANEOUS_MUSIC_TAGS[1] + '\n'
        out += INDENT_UNIT * indent
        out += self.tags()[1]
        out += '\n'
        return out
    def output(self, indent=0):
        out = self.open_tag(indent)
        new_indent = indent + 1
        if self.ambiguous:
            new_indent += 1
        if indent < 5:
           for context in self.contexts:
               out += context.output(new_indent)
           out += self.close_tag(indent)
        return out

class Voice(Context):
    name = 'Voice'

class Staff(Context):
    name = 'Staff'

class StaffGroup(Context):
    name = 'StaffGroup'

class PianoStaff(Context):
    name = 'PianoStaff'

class Score(Context):
    name = 'Score'
    has_new = False
    allow_simultaneous_music = False
    ambiguous = True

class BookPart(Context):
    name = 'BookPart'
    has_new = False
    allow_simultaneous_music = False

class Book(Context):
    name = 'Book'
    has_new = False
    allow_simultaneous_music = False

