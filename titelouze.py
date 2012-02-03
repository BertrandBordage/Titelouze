import subprocess, re
from settings import *

class LilyPond:
    def launch(self, *args, **kwargs):
        command = [LILYPOND_COMMAND]
        for arg in args:
            command.append('--'+arg)
        for key in kwargs:
            command.append('--'+key+'='+kwargs[key])
        p = subprocess.Popen(args=command, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, shell=False)
        p.wait()
        return p.stdout.readlines()
    def get_version(self):
        lines = ''.join(self.launch('version'))
        try:
            return re.findall('GNU LilyPond ([0-9\.]+)', lines, flags=re.M)[0]
        except:
            raise Exception('unable to locate version number')

class Titelouze:
    def __init__(self):
        self.tags_object = re.compile(TAGS_PATTERN)
    def replace(self, filename):
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
        f = open(filename, 'w')
        f.writelines(lines)
        f.close()

if __name__ == '__main__':
    version = LilyPond().get_version()
    lines = Titelouze().replace('templates/base.ily')
    Titelouze().output('out.ly', lines)

