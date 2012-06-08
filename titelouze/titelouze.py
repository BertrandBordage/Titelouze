# coding: utf-8

'''
Titelouze
Bertrand Bordage © 2011-2012

This application is a framework for LilyPond, a music engraving program.
Its goal is to provide an easy way to create large music books.
'''

import subprocess
import sys
import re
from settings import *
from macros import *
from contexts import Book


class LilyPond:
    def __init__(self, path=LILYPOND_PATH, binary=LILYPOND_BINARY):
        self.path = path
        self.binary = binary
        self.command = path + binary

    def launch(self, filename, *args, **kwargs):
        '''
        Launches LilyPond with raw args and kwargs passed as "--[key]=[value]".
        Returns the output.
        launch([...], verbose=True) will flush the output to stdout.
        '''
        verbose = kwargs.pop('verbose', False)
        command = [self.command]
        command.extend(args)
        command.extend('--{}={}'.format(k, kwargs[k]) for k in kwargs)
        command.append(filename)
        p = subprocess.Popen(args=command, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, shell=False)
        lines = []
        for line in iter(p.stdout.readline, ''):
            if verbose:
                sys.stdout.write(line)
                sys.stdout.flush()
            lines.append(line)
        p.wait()
        return ''.join(lines)

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
    filename = 'out.ly'

    def __init__(self):
        self.lilypond_version = self.lilypond.get_version()
        self.book = Book()

    def launch_lilypond(self, *args, **kwargs):
        self.lilypond.launch(self.filename, *args, **kwargs)

    def compile_pdf(self, *args, **kwargs):
        self.launch_lilypond(*args, **kwargs)

    def compile_png(self, *args, **kwargs):
        kwargs['format'] = 'png'
        self.launch_lilypond(*args, **kwargs)

    def compile_preview(self, *args, **kwargs):
        kwargs['define-default'] = 'preview'
        self.launch_lilypond(*args, **kwargs)

    def output(self):
        text = replace_tags('base', locals())
        text = remove_empty_lines(text)
        write_to_file(self.filename, text)
        self.compile_pdf(verbose=True)
