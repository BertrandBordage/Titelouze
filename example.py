#! /usr/bin/env python
# coding: utf-8

from titelouze import *
import os.path


# We initialize Titelouze.  It contains a Book and LilyPond, so that we can
# compile the PDF output without having to call LilyPond outside of Python.
t = Titelouze()
# We define the name of the output file.  Here it is automatically taken from
# the file where we are, 'example.py', so it will be 'example.ly'.
t.filename = os.path.splitext(__file__)[0] + '.ly'


# We create a Score with one Organ part inside, another Score with a Contralto
# inside, then a BookPart with a Choir inside.  Note that we don't have to
# create a Score inside the BookPart, it is implicitely added.
score1 = Score(Organ())
score1.header['title'] = 'Concerto'
score2 = Score(Contralto())
score2.header['composer'] = 'Antonio Lucio Vivaldi'
part = BookPart(Choir())
# Then we add these three elements to our Book.
t.book += score1, score2, part

# Now we enter the content of the Organ staves...
organ = score1.organ
organ.keyboards.righthand = 'a16 cis e cis ' * 10
organ.keyboards.lefthand = 'cis8 a ' * 10
organ.pedal = 'bes4 a ' * 5

# The music and lyrics for the Contralto...
contralto = score2.contralto
contralto.staff = 'd b c'
contralto.lyrics = u'ré si do'

# And what the Choir sings.
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

# Now, just to show how easily we can remove a context from another, I've
# decided to add another score to that last bookpart, but with a nasty detail.
# It will be exactly the same Choir than before, but without the Soprano.
part.add(choir - choir.soprano)
# Important note on that last line :
# 'add' is used because '+' creates a copy of the context.
# We could use :
# t.book -= part
# part += choir1 - choir1.soprano
# t.book += part
# But it's dirty and uses more code, memory, and execution time.


# And at last but not least, we generate our output 'example.ly' and compile it
# to get a beautiful score !
t.output()
