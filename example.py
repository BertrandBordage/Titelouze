#! /usr/bin/env python
# coding: utf-8

from titelouze import *
from ensembles import *

t = Titelouze()
t.filename = 'example.ly'
score1 = Score()
score1.header['title'] = 'Concerto'
score2 = Score()
score2.header['composer'] = 'Antonio Lucio Vivaldi'
t.book.add(score1, score2)
organ = Organ()
organ.keyboards.righthand = 'a16 cis e cis ' * 10
organ.keyboards.lefthand = 'cis8 a ' * 10
organ.pedal = 'bes4 a ' * 5
score1.add(organ)
contralto = Contralto()
contralto.staff = 'd b c'
contralto.lyrics = u'ré si do'
score2.add(contralto)
part = BookPart()
t.book.add(part)
choir = Choir()
part.add(choir)
choir.soprano.staff = 'cis8 ' * 32
choir.soprano.lyrics = 'hi -- hi ' * 16
choir.contralto.staff = 'a8 ' * 32
choir.contralto.lyrics = 'he -- he ' * 16
choir.tenore.staff.mode = r'\relative c'
choir.tenore.staff = 'e8 ' * 32
choir.tenore.lyrics = 'ho -- ho ' * 16
choir.bass.staff = 'a8 ' * 32
choir.bass.lyrics = 'ha -- ha ' * 16
t.output()
