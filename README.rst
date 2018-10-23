Test of indentation parsing with parglare
=========================================

Running the Parser
------------------

The parser is written in Python 3.  If you want to try
running the parser yourself, first `install parglare`_.  Right now,
this parser requires a modified branch of ``parglare``, so please use
the installation instructions below to install ``parglare``.  Also
note that I had to use ``pip3`` instead of ``pip`` as specified in
``parglare`` installation instructions.

::

  pip3 install --user click
  mkdir ~/git
  cd ~/git
  git clone -b codecraftsmen https://github.com/codecraftingtools/parglare.git

Next, clone this test code repository:

::

  git clone https://github.com/jwcraftsman/pgindent.git

The parser can now be run like this:

::

  export PYTHONPATH=~/git/parglare
  cd pgindent
  python3 pgindent.py example.input

.. _install parglare: https://github.com/igordejanovic/parglare#installation
