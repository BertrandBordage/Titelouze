# coding: utf-8

'''
Useful functions that can't be placed somewhere else.
'''

import re, os
from settings import TITELOUZE_TAG_PATTERN
from types import MethodType

def py2scm (py):
    '''
    Converts python values into a string of the corresponding Scheme value.
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


def replace_tags(filename, parent_locals):
    '''
    Opens filename.
    Replaces template tags with the corresponding values.
    Returns the updated content of filename.
    '''
    locals().update(parent_locals)
    tags_object = re.compile(TITELOUZE_TAG_PATTERN)
    f = open(filename, 'r')
    lines = ''.join(f.readlines())
    f.close()
    tags = tags_object.split(lines)
    out = ''
    for i, tag in enumerate(tags):
        if i % 2:
            try:
                attrs = re.split('\.', tag)
                var = locals()[attrs[0]]
                for attr in attrs[1:]:
                    var = getattr(var, attr)
                if type(var) is MethodType:
                    var = var()
                out += unicode(var)
            except:
                raise UnboundLocalError('unbound variable "%s"' % tag)
        else:
            out += tag
    return out


def write_to_file(filename, lines):
    '''
    Saves "lines" in the file named "filename".
    '''
    dir = os.path.dirname(filename)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    f = open(filename, 'w')
    f.writelines(lines)
    f.close()

