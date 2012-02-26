# coding: utf-8

'''
Python implementation of LilyPond contexts.
'''

from settings import *
from macros import *
import os, re

class Context:
    indent = 0
    def __init__(self, associated='', **kwargs):
        self.contexts = []
        self.properties = {}
        self.properties.update(kwargs)
        try:
            self.instance_name = self.properties['instrumentName'].lower()
        except:
            pass
        self.associated_instance = associated
    name = 'Context'
    allow_simultaneous_music = True
    instance_name = None
    mode = ''
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    def add(self, *contexts):
        for context in contexts:
            context.indent = 1
        self.contexts.extend(contexts)
    def is_simultaneous(self):
        return len(self.contexts) > 1
    def tags(self):
        if self.is_simultaneous():
            return SIMULTANEOUS_MUSIC_TAGS
        return SEQUENTIAL_MUSIC_TAGS
    def output_properties(self):
        if self.properties:
            indent = self.indent
            out = '\\with {\n'
            props = self.properties
            for key in props:
                out += INDENT_UNIT
                value = py2scm(props[key])
                out += '%s = %s\n' % (key, value)
            out += '}'
            return out
        return ''
    def output_instance(self):
        if self.instance_name:
            return ' = "%s"' % self.instance_name
        return ''
    def open_tag(self, indent=0):
        return self.tags()[0]
    def close_tag(self, indent=0):
        return self.tags()[1]
    def content(self):
        if not self.contexts:
            return replace_tags(TEMPLATE_PATH+'empty-context'+TEMPLATE_EXTENSION, locals())
        if self.is_simultaneous() and not self.allow_simultaneous_music:
            group = Group()
            group.indent = self.indent
            for context in self.contexts:
                group.add(context)
            return group.output()
        out = []
        for context in self.contexts:
            out.append(context.output())
        return '\n'.join(out)
    def output(self):
        path = TEMPLATE_PATH
        cl = self.__class__
        while True:
            filename = cl.__name__.lower() + TEMPLATE_EXTENSION
            if os.path.exists(path+filename):
                break
            if len(cl.__bases__) > 1:
                raise Warning('Two or more base classes for this class : %s' % cl)
            cl = cl.__bases__[0]
        out = replace_tags(path+filename, locals())
        ind = '\n' + INDENT_UNIT * self.indent
        lines = filter(bool, re.split('\s?\n', out))
        out = ind[1:] + ind.join(lines) # indent & remove trailing whitespaces
        return out
    def __unicode__(self):
        return self.output()

class Dynamics(Context):
    name = 'Dynamics'

class Lyrics(Context):
    def __init__(self, *args, **kwargs):
        Context.__init__(self, *args, **kwargs)
        if self.associated_instance:
            self.properties.update(associatedVoice=self.associated_instance)
    name = 'Lyrics'
    mode = '\lyricmode '

class Voice(Context):
    name = 'Voice'

class Staff(Context):
    name = 'Staff'

class Group(Context):
    def __init__(self, *args, **kwargs):
        try:
            Context.__init__(self, *args, **kwargs)
        except AttributeError:
            pass
    name = 'Group'
    def __setattr__(self, name, value):
        if name == 'properties':
            raise AttributeError('"Group" is a fake context.  One cannot use "%s" with it.' % name)
        return Context.__setattr__(self, name, value)
    def content(self):
        out = []
        for context in self.contexts:
            out.append(context.output())
        return '\n'.join(out)

class StaffGroup(Context):
    name = 'StaffGroup'

class ChoirStaff(Context):
    name = 'ChoirStaff'

class PianoStaff(Context):
    name = 'PianoStaff'

class StructContext(Context):
    allow_simultaneous_music = False

class Score(StructContext):
    name = 'Score'

class BookPart(StructContext):
    name = 'BookPart'

class Book(StructContext):
    name = 'Book'

