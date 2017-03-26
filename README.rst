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
continuous integration (with travis_ and coveralls_), version control
(with git_, github_ and gitlab_), documentation (with sphinx_ and
readthedocs_) and a lot more.

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


..   How to uninstall?
     =================


Where to find?
==============

Primary repository:

https://github.com/all3fox/algos-py

Secondary (mirror) repository:

https://gitlab.com/all3fox/algos-py

Release procedure: change version in `setup.py`, then

.. code-block:: bash

   $ git add setup.py
   $ git commit -m "Bump version to 1.0.0"
   $ git tag v1.0.0
   $ git push origin master && git push origin --tags
   $ git push gitlab master && git push gitlab --tags
   $ python setup.py sdist
   $ twine upload ./dist/algos-py-1.0.0.tar.gz


.. _travis-ci.org: https://travis-ci.org
.. _travis: travis-ci.org_
.. _coveralls.io: https://coveralls.io
.. _coveralls: coveralls.io_
.. _nose: https://nose.readthedocs.io/en/latest/
.. _git: https://git-scm.com/
.. _github.com: https://github.com
.. _github: github.com_
.. _gitlab.com: https://gitlab.com
.. _gitlab: gitlab.com_
.. _sphinx: http://www.sphinx-doc.org/en/stable/
.. _readthedocs.org: https://readthedocs.org/
.. _readthedocs: readthedocs.org_
