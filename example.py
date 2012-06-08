#! /usr/bin/env python
# coding: utf-8

from titelouze import *
import os.path

t = Titelouze()
t.filename = os.path.splitext(__file__)[0] + '.ly'

score1 = Score(Organ())
score1.header['title'] = 'Concerto'
score2 = Score(Contralto())
score2.header['composer'] = 'Antonio Lucio Vivaldi'
part = BookPart(Choir())
t.book += score1, score2, part

organ = score1.organ
organ.keyboards.righthand = 'a16 cis e cis ' * 10
organ.keyboards.lefthand = 'cis8 a ' * 10
organ.pedal = 'bes4 a ' * 5

contralto = score2.contralto
contralto.staff = 'd b c'
contralto.lyrics = u'ré si do'

choir = part.choir
choir.soprano.staff = 'cis8 ' * 32
choir.soprano.lyrics = 'hi -- hi ' * 16
choir.contralto.staff = 'a8 ' * 32
choir.contralto.lyrics = 'he -- he ' * 16
choir.tenore.staff.mode = r'\relative c'
choir.tenore.staff = 'e8 ' * 32
choir.tenore.lyrics = 'ho -- ho ' * 16
choir.bass.staff = 'a8 ' * 32
choir.bass.lyrics = 'ha -- ha ' * 16

# 'add' is used because '+' creates a copy of the context.
# We could use :
# t.book -= part
# part += choir1 - choir1.soprano
# t.book += part
# But it's dirty and uses more code, memory, and execution time.
part.add(choir - choir.soprano)

t.output()
