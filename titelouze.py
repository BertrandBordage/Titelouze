# coding: utf-8

'''
Titelouze
Bertrand Bordage © 2011

This application is a framework for LilyPond, a music engraving program.
Its goal is to provide an easy way to create large music books.
'''

import subprocess, sys, re, os
from settings import *
from contexts import *
from instruments import *
from types import MethodType

class LilyPond:
    def launch(self, filename, *args, **kwargs):
        '''
        Launches LilyPond with raw args and kwargs passed as "--[key]=[value]".
        Returns the output.
        launch([...], verbose=True) will flush the output to stdout.
        '''
        verbose = kwargs.get('verbose', False)
        if 'verbose' in kwargs:
            del kwargs['verbose']
        command = [LILYPOND_COMMAND]
        for arg in args:
            command.append(arg)
        for key in kwargs:
            command.append('--'+key+'='+kwargs[key])
        command.append(filename)
        p = subprocess.Popen(args=command, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, shell=False)
        lines = ''
        for line in iter(p.stdout.readline, ""):
            if verbose:
                sys.stdout.write(line)
                sys.stdout.flush()
            lines += line
        p.wait()
        return lines
    def get_version(self):
        '''
        Returns LilyPond version number.
        '''
        lines = self.launch('-v')
        try:
            return re.findall(LILYPOND_VERSION_PATTERN, lines)[0]
        except:
            raise Exception('unable to locate version number')

class Titelouze:
    lilypond = LilyPond()
    tags_object = re.compile(TITELOUZE_TAG_PATTERN)
    def __init__(self):
        self.lilypond_version = lilypond.get_version()
    def launch_lilypond(self, filename='out.ly', *args, **kwargs):
        self.lilypond.launch(filename, *args, **kwargs)
    def compile_pdf(self, *args, **kwargs):
        self.launch_lilypond(*args, **kwargs)
    def compile_png(self, *args, **kwargs):
        kwargs['format'] = 'png'
        self.launch_lilypond(*args, **kwargs)
    def compile_preview(self, *args, **kwargs):
        kwargs['define-default'] = 'preview'
        self.launch_lilypond(*args, **kwargs)
    def replace_tags(self, filename):
        '''
        Opens filename.
        Replaces template tags with the corresponding values.
        Returns the updated content of filename.
        '''
        f = open(filename, 'r')
        lines = ''.join(f.readlines())
        f.close()
        tags = self.tags_object.split(lines)
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
    def output(self, filename, lines):
        '''
        Saves "lines" in the file named "filename".
        '''
        dir = os.path.dirname(filename)
        if dir and not os.path.exists(dir):
            os.makedirs(dir)
        f = open(filename, 'w')
        f.writelines(lines)
        f.close()

if __name__ == '__main__':
    lilypond = LilyPond()
    t = Titelouze()
    t.book = Book()
    score = Score()
    t.book.add(score)
    score.add(Organ())
    score.add(Contralto())
    lines = t.replace_tags('templates/base.ily')
    t.output('out.ly', lines)
    t.compile_pdf(verbose=True)
    t.compile_png()

