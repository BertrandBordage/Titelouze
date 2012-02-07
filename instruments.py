# coding: utf-8

'''
Python implementation of musical instruments.
'''

from contexts import *

#
# Single-staff instruments
#

# Voices

class VoiceStaff(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Voice',
                               shortInstrumentName='Vo.',
                               autoBeaming=False)
    clef = 'G'

class Soprano(VoiceStaff):
    def __init__(self):
        VoiceStaff.__init__(self)
        self.properties.update(instrumentName='Soprano',
                               shortInstrumentName='S.')

class Contralto(VoiceStaff):
    def __init__(self):
        VoiceStaff.__init__(self)
        self.properties.update(instrumentName='Contralto',
                               shortInstrumentName='A.')

class Tenore(VoiceStaff):
    def __init__(self):
        VoiceStaff.__init__(self)
        self.properties.update(instrumentName='Tenore',
                               shortInstrumentName='T.')
    clef = 'G_8'

class Bass(VoiceStaff):
    def __init__(self):
        VoiceStaff.__init__(self)
        self.properties.update(instrumentName='Bass',
                               shortInstrumentName='B.')
    clef = 'G'

# Strings

class Violin(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Violin',
                               shortInstrumentName='Vl.')
    clef = 'G'

class Viola(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Viola',
                               shortInstrumentName='Va.')
    clef = 'G'

class Violoncello(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Violoncello',
                               shortInstrumentName='Vc.')
    clef = 'F'

class Contrabass(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Contrabass',
                               shortInstrumentName='Cb.')
    clef = 'F_8'

#
# Multiple staves instruments
#

# Keyboards

class Keyboard(PianoStaff):
    def __init__(self):
        PianoStaff.__init__(self)
        self.contexts = [Staff(), Dynamics(), Staff()]
        self.properties.update(instrumentName='Keyboard',
                               shortInstrumentName='K.')

class Keyboards(Keyboard):
    def __init__(self):
        Keyboard.__init__(self)
        self.properties.update(instrumentName='Keyboards',
                               shortInstrumentName='Ks.')

class Piano(Keyboard):
    def __init__(self):
        Keyboard.__init__(self)
        self.properties.update(instrumentName='Piano',
                               shortInstrumentName='Pi.')

class Harpsichord(Keyboard):
    def __init__(self):
        Keyboard.__init__(self)
        self.properties.update(instrumentName='Harpsichord',
                               shortInstrumentName='Hc.')

class Pedal(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Pedal',
                               shortInstrumentName='Pe.')
    clef = 'F'

class Organ(Group):
    def __init__(self):
        Group.__init__(self)
        self.contexts = [Keyboards(), Pedal()]
        self.properties.update(instrumentName='Organ',
                               shortInstrumentName='Or.')

