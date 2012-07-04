# coding: utf-8

'''
Useful functions that can't be placed somewhere else.
'''

import re
import os.path
from settings import *


def context_exists(context, name):
    return (context.__class__.__name__.lower() or context.name.lower()) == name


def py2scm(py):
    '''
    Converts python values into a string of the corresponding Scheme value.

    >>> map(py2scm, [True, False, 1, 1.0, 'abc'])
    ['##t', '##f', '#1', '#1.0', '#"abc"']
    '''
    if isinstance(py, bool):
        return '##t' if py else '##f'
    if isinstance(py, int) or isinstance(py, float):
        return '#{}'.format(py)
    if isinstance(py, str):
        return '#"{}"'.format(py)
    raise Exception('unable to convert "{}" to Scheme.'.format(py))


def isblank(str):
    '''
    Returns True if str is empty or contains spaces only.
    '''
    return all(c == ' ' for c in str)


def indent(text, amount):
    '''
    Indent text by an amount of spaces.

    >>> indent('ab\\ncd\\nef\\n', 2)
    '  ab\\n  cd\\n  ef\\n'
    '''
    lines = text if isinstance(text, list) else text.split('\n')
    return '\n'.join((l and amount or 0) * ' ' + l for l in lines)


def get_template_abspath(filename):
    t = (TEMPLATE_ABSPATH, filename + TEMPLATE_EXTENSION)
    return os.path.join(*t)


def replace_tags(filename, parent_locals):
    '''
    Opens filename.
    Replaces template tags with the corresponding values.
    Returns the updated content of filename.
    '''
    locals().update(parent_locals)
    tags_object = re.compile(TITELOUZE_TAG_PATTERN)
    f = open(get_template_abspath(filename), 'r')
    lines = f.readlines()
    f.close()
    out = ''
    for line in lines:
        tags = tags_object.split(line)
        first = tags[0]
        line_out = ''
        for i, tag in enumerate(tags):
            if i % 2:
                attrs = tag.split('.')
                var = locals()[attrs.pop(0)]
                for attr in attrs:
                    var = getattr(var, attr)
                if callable(var):
                    var = var()
                if var:
                    line_out += unicode(var)
            elif not isblank(tag):
                line_out += tag
        if isblank(first):
            out += indent(line_out, len(first))
        else:
            out += line_out
    return out


def render_properties(props, template_name):
    '''
    Render 'props' from the templates 'property' and 'template_name'
    '''
    if not props:
        return ''
    properties = ''
    for key in props:
        value = py2scm(props[key])
        properties += replace_tags('property', locals())
    return replace_tags(template_name, locals())


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
