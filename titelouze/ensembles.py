# coding: utf-8

'''
Implementation of musical ensembles, such as a choir or an orchestra.
'''

from contexts import *
from instruments import *


class Choir(ChoirStaff):
    def __init__(self, *args, **kwargs):
        super(Choir, self).__init__(*args, **kwargs)
        self.add(Soprano(), Contralto(), Tenore(), Bass())
    instance_name = 'choir'
