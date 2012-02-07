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
    instance_name = 'voice'
    clef = 'G'

class Soprano(VoiceStaff):
    def __init__(self):
        VoiceStaff.__init__(self)
        self.properties.update(instrumentName='Soprano',
                               shortInstrumentName='S.')
    instance_name = 'soprano'

class Contralto(VoiceStaff):
    def __init__(self):
        VoiceStaff.__init__(self)
        self.properties.update(instrumentName='Contralto',
                               shortInstrumentName='A.')
    instance_name = 'contralto'

class Tenore(VoiceStaff):
    def __init__(self):
        VoiceStaff.__init__(self)
        self.properties.update(instrumentName='Tenore',
                               shortInstrumentName='T.')
    clef = 'G_8'
    instance_name = 'tenore'

class Bass(VoiceStaff):
    def __init__(self):
        VoiceStaff.__init__(self)
        self.properties.update(instrumentName='Bass',
                               shortInstrumentName='B.')
    clef = 'F'
    instance_name = 'bass'

# Strings

class Violin(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Violin',
                               shortInstrumentName='Vl.')
    clef = 'G'
    instance_name = 'violin'

class Viola(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Viola',
                               shortInstrumentName='Va.')
    clef = 'G'
    instance_name = 'viola'

class Violoncello(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Violoncello',
                               shortInstrumentName='Vc.')
    clef = 'F'
    instance_name = 'violoncello'

class Contrabass(Staff):
    def __init__(self):
        Staff.__init__(self)
        self.properties.update(instrumentName='Contrabass',
                               shortInstrumentName='Cb.')
    clef = 'F_8'
    instance_name = 'contrabass'

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
    clef = 'F'
    instance_name = 'pedal'

class Organ(Group):
    def __init__(self):
        Group.__init__(self)
        self.contexts = [Keyboards(), Pedal()]
    instance_name = 'organ'

