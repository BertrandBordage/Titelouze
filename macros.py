# coding: utf-8

'''
Useful functions that can't be placed somewhere else.
'''

import re
import os
from settings import *
from types import FunctionType,        MethodType, \
           BuiltinFunctionType, BuiltinMethodType


def context_exists(context, name):
    return (context.__class__.__name__.lower() or context.name.lower()) == name


def find_contexts(obj, name):
    if 'contexts' in obj.__dict__:
        contexts = filter(lambda c: context_exists(c, name), obj.contexts)
        return contexts


def py2scm(py):
    '''
    Converts python values into a string of the corresponding Scheme value.

    >>> map(py2scm, [True, False, 1, 1.0, 'abc'])
    ['##t', '##f', '#1', '#1.0', '#"abc"']
    '''
    if isinstance(py, bool):
        if py:
            return '##t'
        else:
            return '##f'
    if isinstance(py, int) or isinstance(py, float):
        return '#%s' % py
    if isinstance(py, str):
        return '#"%s"' % py
    raise Exception('unable to convert "%s" to Scheme.' % py)


def indent(text, amount):
    '''
    Indent text by an amount of spaces.

    >>> indent('ab\\ncd\\nef\\n', 2)
    '  ab\\n  cd\\n  ef\\n'
    '''
    lines = text if isinstance(text, list) else text.split('\n')
    return '\n'.join((amount * ' ' + l if l else '' for l in lines))


def replace_tags(filename, parent_locals):
    '''
    Opens filename.
    Replaces template tags with the corresponding values.
    Returns the updated content of filename.
    '''
    locals().update(parent_locals)
    tags_object = re.compile(TITELOUZE_TAG_PATTERN)
    abs_filename = TEMPLATE_PATH + filename + TEMPLATE_EXTENSION
    f = open(abs_filename, 'r')
    lines = f.readlines()
    f.close()
    out = []
    for line in lines:
        tags = tags_object.split(line)
        first = tags[0]
        line_out = ''
        for i, tag in enumerate(tags):
            if i % 2:
                attrs = re.split('\.', tag)
                var = locals()[attrs[0]]
                for attr in attrs[1:]:
                    var = getattr(var, attr)
                if type(var) in (FunctionType,        MethodType,
                          BuiltinFunctionType, BuiltinMethodType):
                    var = var()
                if var:
                    line_out += unicode(var)
            elif not (i == 0 and tag == len(first) * ' '):
                line_out += tag
        if first == len(first) * ' ':
            out.append(indent(line_out, len(first)))
        else:
            out.append(line_out)
    return ''.join(out)


def render_properties(props, template_name):
    '''
    Render 'props' from the templates 'property' and 'template_name'
    '''
    if props:
        properties = ''
        for key in props:
            value = py2scm(props[key])
            properties += replace_tags('property', locals())
        return replace_tags(template_name, locals())
    return ''


def remove_empty_lines(text):
    '''
    Remove every empty newline.

    >>> remove_empty_lines('ab\\nde\\n\\nfg\\n')
    'ab\\nde\\nfg'
    '''
    return '\n'.join(filter(bool, text.split('\n')))


def write_to_file(filename, text):
    '''
    Saves 'text' in the file named 'filename'.
    '''
    dir = os.path.dirname(filename)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    f = open(filename, 'w')
    f.write(text.encode('utf-8'))
    f.close()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
