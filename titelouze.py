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

class LilyPond:
    def launch(self, *args, **kwargs):
        '''
        Launches LilyPond with raw args and kwargs passed as "--key=value".
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
    def __init__(self):
        self.tags_object = re.compile(TITELOUZE_TAG_PATTERN)
    def replace_tags(self, filename):
        '''
        Replaces template tags with the corresponding values.
        '''
        f = open(filename, 'r')
        lines = ''.join(f.readlines())
        f.close()
        tags = self.tags_object.split(lines)
        out = ''
        for i, tag in enumerate(tags):
            if i % 2:
                try:
                    out += globals()[tag]
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
    titelouze = Titelouze()
    version = lilypond.get_version()
    lines = titelouze.replace_tags('templates/base.ily')
    book = Book()
    bookpart = BookPart()
    book.add(bookpart)
    score = Score()
    book.add(score)
    score.add(Staff())
    score.add(Staff())
    lines += book.output()
    titelouze.output('out.ly', lines)
    lilypond.launch('out.ly', verbose=True)

