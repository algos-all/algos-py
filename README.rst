Package algos-py
################

.. image:: https://img.shields.io/travis/all3fox/algos-py.svg
   :target: https://travis-ci.org/all3fox/algos-py
.. image:: https://img.shields.io/coveralls/all3fox/algos-py.svg
   :target: https://coveralls.io/github/all3fox/algos-py
.. image:: https://img.shields.io/pypi/v/algos-py.svg
   :target: https://pypi.python.org/pypi/algos-py/
.. image:: https://img.shields.io/github/license/all3fox/algos-py.svg
   :target: https://choosealicense.com/licenses/mit/

What is algos-py?
=================

The algos-py package contains implementations of some classic computer
science algorithms. My primary goal is to understand those algorithms
and the best way to do that is to code them myself.

Along the way I practice test driven development (with nose_),
continuos integration (with travis_ and coveralls_), version control
(with git_ and github_), documentation (with sphinx_ and readthedocs_)
and a lot more.

..
   What algorithms are ready?
   ==========================

   TODO

..
   How to install?
   ===============

   Installing from github
   ----------------------

   TODO

   Installing from pip
   -------------------

   TODO

How to test?
============

To run all of the unit-tests:

.. code-block:: bash

   $ nosetests

To run unit-tests for a specific module:

.. code-block:: bash

   $ nosetests ./tests/test_heap.py

To run all the unit-tests and produce a coverage report:

.. code-block:: bash

   $ nosetests --with-coverage --cover-package=src

..
   How to uninstall?
   =================

.. _travis-ci.org: https://travis-ci.org
.. _travis: travis-ci.org_
.. _coveralls.io: https://coveralls.io
.. _coveralls: coveralls.io_
.. _nose: https://nose.readthedocs.io/en/latest/
.. _git: https://git-scm.com/
.. _github.com: https://github.com
.. _github: github.com_
.. _sphinx: http://www.sphinx-doc.org/en/stable/
.. _readthedocs.org: https://readthedocs.org/
.. _readthedocs: readthedocs.org_
