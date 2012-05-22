# coding: utf-8

'''
Python implementation of musical instruments.
'''

from contexts import *

#
# Single-staff instruments
#

# Voices


class VoiceStaff(Group):
    def __init__(self, *args, **kwargs):
        Group.__init__(self, *args, **kwargs)
        self.add(Staff(instrumentName='Voice',
                       shortInstrumentName='Vo.',
                       autoBeaming=False),
                 Lyrics('voice'))


class Soprano(Group):
    def __init__(self, *args, **kwargs):
        Group.__init__(self, *args, **kwargs)
        self.add(Staff(instrumentName='Soprano',
                       shortInstrumentName='S.',
                       autoBeaming=False),
                 Lyrics('soprano'))


class Contralto(Group):
    def __init__(self, *args, **kwargs):
        Group.__init__(self, *args, **kwargs)
        self.add(Staff(instrumentName='Contralto',
                       shortInstrumentName='A.',
                       autoBeaming=False),
                 Lyrics('contralto'))


class Tenore(Group):
    def __init__(self, *args, **kwargs):
        Group.__init__(self, *args, **kwargs)
        self.add(Staff(instrumentName='Tenore',
                       shortInstrumentName='T.',
                       autoBeaming=False),
                 Lyrics('tenore'))
        self.functions.append('\clef G_8')


class Bass(Group):
    def __init__(self, *args, **kwargs):
        Group.__init__(self, *args, **kwargs)
        self.add(Staff(instrumentName='Bass',
                       shortInstrumentName='B.',
                       autoBeaming=False),
                 Lyrics('bass'))
        self.functions.append('\clef F')


# Strings

class Violin(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Violin',
                               shortInstrumentName='Vl.')
    instance_name = 'violin'


class Viola(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Viola',
                               shortInstrumentName='Va.')
        self.functions.append('\clef alto')
    instance_name = 'viola'


class Violoncello(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Violoncello',
                               shortInstrumentName='Vc.')
        self.functions.append('\clef F')
    instance_name = 'violoncello'


class Contrabass(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Contrabass',
                               shortInstrumentName='Cb.')
        self.functions.append('\clef F_8')
    instance_name = 'contrabass'


#
# Multiple staves instruments
#

# Keyboards

class RightHand(Staff):
    pass


class LeftHand(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.functions.append('\clef F')


class Keyboard(PianoStaff):
    def __init__(self):
        PianoStaff.__init__(self)
        self.add(RightHand(), Dynamics(), LeftHand())
        self.properties.update(instrumentName='Keyboard',
                               shortInstrumentName='K.')
    instance_name = 'keyboard'


class Keyboards(Keyboard):
    def __init__(self):
        Keyboard.__init__(self)
        self.properties.update(instrumentName='Keyboards',
                               shortInstrumentName='Ks.')
    instance_name = 'keyboards'


class Piano(Keyboard):
    def __init__(self):
        Keyboard.__init__(self)
        self.properties.update(instrumentName='Piano',
                               shortInstrumentName='Pi.')
    instance_name = 'piano'


class Harpsichord(Keyboard):
    def __init__(self):
        Keyboard.__init__(self)
        self.properties.update(instrumentName='Harpsichord',
                               shortInstrumentName='Hc.')
    instance_name = 'harpsichord'


class Pedal(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Pedal',
                               shortInstrumentName='Pe.')
        self.functions.append('\clef F')
    instance_name = 'pedal'


class Organ(Group):
    def __init__(self):
        Group.__init__(self)
        self.add(Keyboards(), Pedal())
    instance_name = 'organ'
