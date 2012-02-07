# coding: utf-8

'''
Python implementation of LilyPond contexts.
'''

from settings import *
from macros import *

class Context:
    def __init__(self):
        self.contexts = []
        self.properties = {}
        self.message = COMMENT_TAG + 'Write here the content of this %s.' % self.name.lower() + '\n'
    name = 'Context'
    has_new = True
    allow_simultaneous_music = True
    instance_name = None
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    def add(self, context):
        self.contexts.append(context)
    def is_simultaneous(self):
        return len(self.contexts) > 1
    def tags(self):
        if self.allow_simultaneous_music and self.is_simultaneous():
            return SIMULTANEOUS_MUSIC_TAGS
        return SEQUENTIAL_MUSIC_TAGS
    def output_properties(self, indent=0):
        try:
            out = ''
            c = self.name
            props = self.properties
            for key in props:
                out += INDENT_UNIT * indent
                value = py2scm(props[key])
                out += '\\set %s.%s = %s\n' % (c, key, value)
            return out
        except:
            return ''
    def open_tag(self, indent=0):
        out = INDENT_UNIT * indent + '\\'
        if self.has_new:
            out += 'new ' + self.name
            if self.instance_name:
                out += ' = "%s"' % self.instance_name
        else:
            out += self.name.lower()
        out += ' '
        out += self.tags()[0]
        out += '\n'
        new_indent = indent + 1
        out += self.output_properties(new_indent)
        if not self.contexts:
            out += INDENT_UNIT * (new_indent) + self.message
        return out, new_indent
    def close_tag(self, indent=0):
        out = INDENT_UNIT * indent
        out += self.tags()[1]
        out += '\n'
        return out
    def output(self, indent=0):
        out, new_indent = self.open_tag(indent)
        for context in self.contexts:
            out += context.output(new_indent)
        out += self.close_tag(indent)
        return out

class Dynamics(Context):
    name = 'Dynamics'

class Voice(Context):
    name = 'Voice'

class Staff(Context):
    name = 'Staff'

class Group(Context):
    def __init__(self):
        try:
            Context.__init__(self)
        except AttributeError:
            pass
    name = 'Group'
    def __setattr__(self, name, value):
        if name == 'properties':
            raise AttributeError('"Group" is a fake context.  One cannot use "%s" with it.' % name)
        return Context.__setattr__(self, name, value)
    def open_tag(self, indent):
        return INDENT_UNIT * indent + SIMULTANEOUS_MUSIC_TAGS[0] + '\n', indent
    def close_tag(self, indent):
        return INDENT_UNIT * indent + SIMULTANEOUS_MUSIC_TAGS[1] + '\n'

class StaffGroup(Context):
    name = 'StaffGroup'

class ChoirStaff(Context):
    name = 'ChoirStaff'

class PianoStaff(Context):
    name = 'PianoStaff'

class Score(Context):
    name = 'Score'
    has_new = False
    allow_simultaneous_music = False
    def open_tag(self, indent=0):
        out, indent = Context.open_tag(self, indent)
        if self.is_simultaneous():
            indent += 1
            new_tag = Group().open_tag(indent)
            out += new_tag[0]
            indent = new_tag[1]
        return out, indent
    def close_tag(self, indent=0):
        out = ''
        if self.is_simultaneous():
            out += Group().close_tag(indent+1)
        out += Context.close_tag(self, indent)
        return out

class BookPart(Context):
    name = 'BookPart'
    has_new = False
    allow_simultaneous_music = False

class Book(Context):
    name = 'Book'
    has_new = False
    allow_simultaneous_music = False

