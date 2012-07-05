*********
Titelouze
*********

Bertrand Bordage © 2011-2012

This application is a framework for `LilyPond <http://lilypond.org>`_,
an open-source **music engraving** software.
Its goal is to provide an easy way to create large music books.


Requirements
============

========= =======
Name      Version
========= =======
Python_   2.7.2
LilyPond_ 2.14.2
========= =======

.. _Python: http://python.org/


Installation
============

1. Install the `Requirements`_
2. ``sudo pip install titelouze``


Using
=====

This is just a regular Python library.  Import everything using
``from titelouze import *`` and create LilyPond scores easily using our
(uncomplete) list of instruments.  Regular LilyPond contexts
(bookparts, scores, staves, ...) are also available.

To see a demonstration, launch ``./example.py`` to generate a test file called
``example.ly`` and its PDF ``example.pdf``.


Documentation
=============

There is not much to say about Titelouze, since this project is still a draft.
But this is already quite powerful for such a simple library.

I strongly recommand you read ``./example.py``.  There is a lot of comments
so it can be read as a tiny tutorial.


Future
======

For sure : a Django application to easily include scores to the database of
your Django project.

Maybe : a small user-friendly GUI.


Contributing
============

Any idea would be welcome !  So don't be shy and open an issue if you have
spotted something odd.
