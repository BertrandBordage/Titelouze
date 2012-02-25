# coding: utf-8

'''
Titelouze
Bertrand Bordage © 2011

This application is a framework for LilyPond, a music engraving program.
Its goal is to provide an easy way to create large music books.
'''

import subprocess, sys, re, os
from settings import *
from macros import *
from contexts import *
from instruments import *

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
    book = Book()
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
    def output(self):
        lines = replace_tags(TEMPLATE_PATH+'base.ily', locals())
        write_to_file('out.ly', lines)
        self.compile_pdf(verbose=True)

if __name__ == '__main__':
    lilypond = LilyPond()
    t = Titelouze()
    score = Score()
    t.book.add(score)
    score.add(Organ())
    score.add(Contralto())
    t.output()

