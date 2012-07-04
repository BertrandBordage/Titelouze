# coding: utf-8

'''
Python implementation of LilyPond contexts.
'''

from settings import *
from macros import *
from copy import copy, deepcopy
import os


class Context(object):
    name = 'Context'
    allow_simultaneous_music = True
    instance_name = None
    mode = ''

    def __init__(self, *contexts, **kwargs):
        self.contexts = list(contexts)
        self.associated_instance = kwargs.pop('associated', None)
        self.__properties = kwargs
        self.functions = []
        try:
            self.instance_name = self.properties['instrumentName'].lower()
        except KeyError:
            pass

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        self.__properties = value

    @properties.deleter
    def properties(self):
        del self.__properties

    def __setattr__(self, attr, value):
        contexts = self.find_contexts(attr)
        if not contexts:
            return super(Context, self).__setattr__(attr, value)
        for context in contexts:
            context.content = value

    def __getattribute__(self, attr):
        try:
            return super(Context, self).__getattribute__(attr)
        except AttributeError, e:
            contexts = self.find_contexts(attr)
            if not contexts:
                raise e
            if len(contexts) > 1:
                raise Exception('{} contains two or more contexts '
                                'called {}'.format(self.name, attr))
            return contexts[0]

    def copy(self):
        object = copy(self)
        object.contexts = copy(self.contexts)
        try:
            object.properties = copy(self.properties)
        except AttributeError:
            pass
        return object

    def deepcopy(self):
        return deepcopy(self)

    def add(self, *contexts):
        self.contexts.extend(contexts)

    def remove(self, *contexts):
        # TODO: Remove inside nested contexts.
        try:
            self.contexts.remove(*contexts)
        except ValueError:
            raise ValueError('{} not in {}'.format(contexts, self.name))

    def __add__(self, other):
        object = self.copy()
        try:
            object.add(*other)
        except TypeError:
            object.add(other)
        return object

    def __sub__(self, other):
        object = self.copy()
        try:
            object.remove(*other)
        except TypeError:
            object.remove(other)
        return object

    def find_contexts(self, name):
        if hasattr(self, 'contexts'):
            contexts = filter(lambda c: context_exists(c, name), self.contexts)
            return contexts

    def is_simultaneous(self):
        return len(self.contexts) > 1

    def tags(self):
        if self.is_simultaneous():
            return SIMULTANEOUS_MUSIC_TAGS
        return SEQUENTIAL_MUSIC_TAGS

    def output_instance(self):
        if self.instance_name:
            return '= "{}"'.format(self.instance_name)
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
            return Group(*self.contexts).output()
        return ''.join(c.output() for c in self.contexts)

    def output(self):
        cl = self.__class__
        while True:
            filename = cl.__name__.lower()
            if os.path.exists(get_template_abspath(filename)):
                break
            if len(cl.__bases__) > 1:
                raise Warning('two or more base classes '
                              'for this class : {}'.format(cl))
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
        super(Lyrics, self).__init__(*args, **kwargs)
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
        super(Group, self).__init__(*args, **kwargs)

    @Context.properties.setter
    def properties(self, value):
        raise AttributeError('"Group" is a fake context, one '
                             'cannot set its "properties".')

    def content(self):
        return ''.join(c.output() for c in self.contexts)


class StaffGroup(Context):
    name = 'StaffGroup'


class ChoirStaff(Context):
    name = 'ChoirStaff'


class PianoStaff(Context):
    name = 'PianoStaff'


class StructContext(Context):
    allow_simultaneous_music = False

    def __init__(self, *args, **kwargs):
        super(StructContext, self).__init__(*args, **kwargs)
        self.header = {}

    def output_header(self):
        return render_properties(self.header, 'header')


class Score(StructContext):
    name = 'Score'


class BookPart(StructContext):
    name = 'BookPart'

    def content(self):
        return ''.join(c.output() for c in self.contexts)


class Book(StructContext):
    name = 'Book'

    def content(self):
        return ''.join(c.output() for c in self.contexts)
