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
        super(VoiceStaff, self).__init__(*args, **kwargs)
        self.add(Staff(instrumentName='Voice',
                       shortInstrumentName='Vo.',
                       autoBeaming=False),
                 Lyrics('voice'))


class Soprano(Group):
    def __init__(self, *args, **kwargs):
        super(Soprano, self).__init__(*args, **kwargs)
        staff = Staff(instrumentName='Soprano',
                      shortInstrumentName='S.',
                      autoBeaming=False)
        staff.mode = r"\relative c''"
        self.add(staff, Lyrics('soprano'))


class Contralto(Group):
    def __init__(self, *args, **kwargs):
        super(Contralto, self).__init__(*args, **kwargs)
        self.add(Staff(instrumentName='Contralto',
                       shortInstrumentName='A.',
                       autoBeaming=False),
                 Lyrics('contralto'))


class Tenore(Group):
    def __init__(self, *args, **kwargs):
        super(Tenore, self).__init__(*args, **kwargs)
        staff = Staff(instrumentName='Tenore',
                      shortInstrumentName='T.',
                      autoBeaming=False)
        staff.functions.append(r'\clef "G_8"')
        self.add(staff, Lyrics('tenore'))


class Bass(Group):
    def __init__(self, *args, **kwargs):
        super(Bass, self).__init__(*args, **kwargs)
        staff = Staff(instrumentName='Bass',
                      shortInstrumentName='B.',
                      autoBeaming=False)
        staff.mode = r"\relative c"
        staff.functions.append(r'\clef F')
        self.add(staff, Lyrics('bass'))


# Strings

class Violin(Staff):
    def __init__(self, *args, **kwargs):
        super(Violin, self).__init__(*args, **kwargs)
        self.properties.update(instrumentName='Violin',
                               shortInstrumentName='Vl.')
    instance_name = 'violin'


class Viola(Staff):
    def __init__(self, *args, **kwargs):
        super(Viola, self).__init__(*args, **kwargs)
        self.properties.update(instrumentName='Viola',
                               shortInstrumentName='Va.')
        self.functions.append(r'\clef alto')
    instance_name = 'viola'


class Violoncello(Staff):
    def __init__(self, *args, **kwargs):
        super(Violoncello, self).__init__(*args, **kwargs)
        self.properties.update(instrumentName='Violoncello',
                               shortInstrumentName='Vc.')
        self.functions.append(r'\clef F')
    instance_name = 'violoncello'


class Contrabass(Staff):
    def __init__(self, *args, **kwargs):
        super(Contrabass, self).__init__(*args, **kwargs)
        self.properties.update(instrumentName='Contrabass',
                               shortInstrumentName='Cb.')
        self.functions.append(r'\clef F_8')
    instance_name = 'contrabass'


#
# Multiple staves instruments
#

# Keyboards

class RightHand(Staff):
    pass


class LeftHand(Staff):
    def __init__(self, *args, **kwargs):
        super(LeftHand, self).__init__(*args, **kwargs)
        self.functions.append(r'\clef F')


class Keyboard(PianoStaff):
    def __init__(self, *args, **kwargs):
        super(Keyboard, self).__init__(*args, **kwargs)
        self.add(RightHand(), Dynamics(), LeftHand())
        self.properties.update(instrumentName='Keyboard',
                               shortInstrumentName='K.')
    instance_name = 'keyboard'


class Keyboards(Keyboard):
    def __init__(self, *args, **kwargs):
        super(Keyboards, self).__init__(*args, **kwargs)
        self.properties.update(instrumentName='Keyboards',
                               shortInstrumentName='Ks.')
    instance_name = 'keyboards'


class Piano(Keyboard):
    def __init__(self, *args, **kwargs):
        super(Piano, self).__init__(*args, **kwargs)
        self.properties.update(instrumentName='Piano',
                               shortInstrumentName='Pi.')
    instance_name = 'piano'


class Harpsichord(Keyboard):
    def __init__(self, *args, **kwargs):
        super(Harpsichord, self).__init__(*args, **kwargs)
        self.properties.update(instrumentName='Harpsichord',
                               shortInstrumentName='Hc.')
    instance_name = 'harpsichord'


class Pedal(Staff):
    def __init__(self, *args, **kwargs):
        super(Pedal, self).__init__(*args, **kwargs)
        self.properties.update(instrumentName='Pedal',
                               shortInstrumentName='Pe.')
        self.functions.append(r'\clef F')
    instance_name = 'pedal'


class Organ(Group):
    def __init__(self, *args, **kwargs):
        super(Organ, self).__init__(*args, **kwargs)
        self.add(Keyboards(), Pedal())
    instance_name = 'organ'
