# coding: utf-8

'''
Useful functions that can't be placed somewhere else.
'''

def py2scm (py):
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

