# coding: utf-8

'''
Python implementation of LilyPond contexts.
'''

from settings import *
from macros import *
import os


class Context(object):
    name = 'Context'
    allow_simultaneous_music = True
    instance_name = None
    mode = ''

    def __init__(self, associated=None, **kwargs):
        self.contexts = []
        self.properties = {}
        self.properties.update(kwargs)
        self.functions = []
        try:
            self.instance_name = self.properties['instrumentName'].lower()
        except KeyError:
            pass
        self.associated_instance = associated

    def __setattr__(self, attr, value):
        contexts = find_contexts(self, attr)
        if not contexts:
            return object.__setattr__(self, attr, value)
        for context in contexts:
            context.__setattr__('content', value)

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            contexts = find_contexts(self, attr)
            if len(contexts) > 1:
                raise Exception('''two or more contexts have '''
                                '''the attribute %s''' % attr)
            return contexts[0]

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
            return '= "%s"' % self.instance_name
        return ''

    def output_properties(self):
        return render_properties(self.properties, 'with')

    def output_functions(self):
        return ' '.join(self.functions)

    def open_tag(self):
        return self.tags()[0]

    def close_tag(self):
        return self.tags()[1]

    def content(self):
        if not self.contexts:
            out = replace_tags('empty-context', locals())
            return out
        if self.is_simultaneous() and not self.allow_simultaneous_music:
            group = Group()
            group.add(*self.contexts)
            return group.output()
        return ''.join((c.output() for c in self.contexts))

    def output(self):
        cl = self.__class__
        while True:
            filename = cl.__name__.lower()
            abs_filename = TEMPLATE_PATH + filename + TEMPLATE_EXTENSION
            if os.path.exists(abs_filename):
                break
            if len(cl.__bases__) > 1:
                raise Warning('''two or more base classes '''
                              '''for this class : %s''' % cl)
            cl = cl.__bases__[0]
        out = replace_tags(filename, locals())
        return out

    def __unicode__(self):
        return self.output()


class Dynamics(Context):
    name = 'Dynamics'


class Lyrics(Context):
    name = 'Lyrics'
    mode = r'\lyricmode '

    def __init__(self, *args, **kwargs):
        Context.__init__(self, *args, **kwargs)
        if self.associated_instance:
            self.properties.update(associatedVoice=self.associated_instance)


class Voice(Context):
    name = 'Voice'
    mode = r"\relative c' "


class Staff(Context):
    name = 'Staff'
    mode = r"\relative c' "


class Group(Context):
    name = 'Group'

    def __init__(self, *args, **kwargs):
        try:
            Context.__init__(self, *args, **kwargs)
        except AttributeError:
            pass

    def __setattr__(self, name, value):
        if name == 'properties':
            raise AttributeError('''"Group" is a fake context, '''
                                 '''one cannot use "%s" with it.''' % name)
        return Context.__setattr__(self, name, value)

    def content(self):
        return ''.join((c.output() for c in self.contexts))


class StaffGroup(Context):
    name = 'StaffGroup'


class ChoirStaff(Context):
    name = 'ChoirStaff'


class PianoStaff(Context):
    name = 'PianoStaff'


class StructContext(Context):
    allow_simultaneous_music = False

    def __init__(self, *args, **kwargs):
        Context.__init__(self, *args, **kwargs)
        self.header = {}

    def output_header(self):
        return render_properties(self.header, 'header')


class Score(StructContext):
    name = 'Score'


class BookPart(StructContext):
    name = 'BookPart'

    def content(self):
        return ''.join((c.output() for c in self.contexts))


class Book(StructContext):
    name = 'Book'

    def content(self):
        return ''.join((c.output() for c in self.contexts))
