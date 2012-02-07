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
    properties = {'instrumentName': 'Voice',
                  'shortInstrumentName': 'Vo.',
                  'autoBeaming': False}
    clef = 'G'

class Soprano(VoiceStaff):
    properties = {'instrumentName': 'Soprano',
                  'shortInstrumentName': 'S.'}

class Contralto(VoiceStaff):
    properties = {'instrumentName': 'Contralto',
                  'shortInstrumentName': 'A.'}

class Tenore(VoiceStaff):
    properties = {'instrumentName': 'Tenore',
                  'shortInstrumentName': 'T.'}
    clef = 'G_8'

class Bass(VoiceStaff):
    properties = {'instrumentName': 'Bass',
                  'shortInstrumentName': 'B.'}
    clef = 'G'

# Strings

class Violin(Staff):
    properties = {'instrumentName': 'Violin',
                  'shortInstrumentName': 'Vl.'}
    clef = 'G'

class Viola(Staff):
    properties = {'instrumentName': 'Viola',
                  'shortInstrumentName': 'Va.'}
    clef = 'G'

class Violoncello(Staff):
    properties = {'instrumentName': 'Violoncello',
                  'shortInstrumentName': 'Vc.'}
    clef = 'F'

class Contrabass(Staff):
    properties = {'instrumentName': 'Contrabass',
                  'shortInstrumentName': 'Cb.'}
    clef = 'F_8'

#
# Multiple staves instruments
#

class Keyboard(PianoStaff):
    def __init__(self):
        PianoStaff.__init__(self)
        self.contexts = [Staff(), Dynamics(), Staff()]
    properties = {'instrumentName': 'Keyboard',
                  'shortInstrumentName': 'K.'}

class Keyboards(Keyboard):
    properties = {'instrumentName': 'Keyboards',
                  'shortInstrumentName': 'Ks.'}

class Piano(Keyboard):
    properties = {'instrumentName': 'Piano',
                  'shortInstrumentName': 'Pi.'}

class Pedal(Staff):
    properties = {'instrumentName': 'Pedal',
                  'shortInstrumentName': 'Pe.'}
    clef = 'F'

class Organ(Group):
    def __init__(self):
        Group.__init__(self)
        self.contexts = [Keyboards(), Pedal()]
    properties = {'instrumentName': 'Organ',
                  'shortInstrumentName': 'Or.'}

