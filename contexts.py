# coding: utf-8

'''
Python implementation of LilyPond contexts.
'''

from settings import *
from macros import *
import os, re

class Context:
    def __init__(self, associated='', **kwargs):
        self.contexts = []
        self.properties = {}
        self.properties.update(kwargs)
        self.functions = []
        try:
            self.instance_name = self.properties['instrumentName'].lower()
        except:
            pass
        self.associated_instance = associated
    name = 'Context'
    allow_simultaneous_music = True
    instance_name = None
    mode = "\\relative c' "
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    def add(self, *contexts):
        self.contexts.extend(contexts)
    def is_simultaneous(self):
        return len(self.contexts) > 1
    def tags(self):
        if self.is_simultaneous():
            return SIMULTANEOUS_MUSIC_TAGS
        return SEQUENTIAL_MUSIC_TAGS
    def output_instance(self):
        if self.instance_name:
            return ' = "%s"' % self.instance_name
        return ''
    def output_properties(self):
        if self.properties:
            properties = ''
            props = self.properties
            for key in props:
                value = py2scm(props[key])
                properties += replace_tags('with-property', locals())
            properties = indent(properties)
            return indent(replace_tags('with-properties', locals()))
        return ''
    def output_functions(self):
        return ' '.join(self.functions)
    def open_tag(self):
        return self.tags()[0]
    def close_tag(self):
        return self.tags()[1]
    def content(self):
        if not self.contexts:
            out = replace_tags('empty-context', locals())
            return indent(out)
        if self.is_simultaneous() and not self.allow_simultaneous_music:
            group = Group()
            for context in self.contexts:
                group.add(context)
            return group.output()
        return '\n'.join([context.output() for context in self.contexts])
    def output(self):
        cl = self.__class__
        while True:
            filename = cl.__name__.lower()
            if os.path.exists(TEMPLATE_PATH+filename+TEMPLATE_EXTENSION):
                break
            if len(cl.__bases__) > 1:
                raise Warning('Two or more base classes for this class : %s' % cl)
            cl = cl.__bases__[0]
        out = replace_tags(filename, locals())
        return indent(out)
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
    mode = ''
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
    mode = ''

class ChoirStaff(Context):
    name = 'ChoirStaff'
    mode = ''

class PianoStaff(Context):
    name = 'PianoStaff'
    mode = ''

class StructContext(Context):
    allow_simultaneous_music = False
    def __init__(self, *args, **kwargs):
        Context.__init__(self, *args, **kwargs)
        self.header = {}
    def headers(self):
        l = []
        for key in self.header:
            l.append('%s = %s' % (key, py2scm(self.header[key])))
        return indent(l)
    def output_header(self):
        if self.header:
            out = replace_tags('header', locals())
            return indent(out)

class Score(StructContext):
    name = 'Score'

class BookPart(StructContext):
    name = 'BookPart'
    def content(self):
        out = []
        for context in self.contexts:
            out.append(context.output())
        return '\n'.join(out)

class Book(StructContext):
    name = 'Book'
    def content(self):
        out = []
        for context in self.contexts:
            out.append(context.output())
        return '\n'.join(out)
