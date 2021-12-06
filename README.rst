Package algos-py
################

.. image:: https://github.com/algos-all/algos-py/actions/workflows/python-app.yml/badge.svg
   :target: https://github.com/algos-all/algos-py/actions/workflows/python-app.yml
.. image:: https://ci.appveyor.com/api/projects/status/j5ireye9mly39f9m/branch/main?svg=true
   :target: https://ci.appveyor.com/project/algos-all/algos-py
.. image:: https://coveralls.io/repos/github/algos-all/algos-py/badge.svg?branch=main
   :target: https://coveralls.io/github/algos-all/algos-py?branch=main
.. image:: https://img.shields.io/codecov/c/github/algos-all/algos-py/main.svg
   :target: https://codecov.io/gh/algos-all/algos-py
.. image:: https://pyup.io/repos/github/algos-all/algos-py/shield.svg
   :target: https://pyup.io/repos/github/algos-all/algos-py

|

.. image:: https://img.shields.io/pypi/format/algos-py.svg
   :target: https://pypi.python.org/pypi/algos-py/
.. image:: https://img.shields.io/pypi/v/algos-py.svg
   :target: https://pypi.python.org/pypi/algos-py/
.. image:: https://img.shields.io/github/license/algos-all/algos-py.svg
   :target: https://choosealicense.com/licenses/mit/

What is algos-py?
=================

This package contains implementations of some classic computer
science algorithms. My main goal is to understand these algorithms
and the best way to do that is to implement them myself.

Along the way I practice test driven development (with pytest_),
continuous integration (with travis_ and appveyor_), coverage
tracking (with coveralls_ and codecov_), version control (with git_,
github_ and gitlab_), documentation (with sphinx_ and readthedocs_)
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

   $ pytest -n 2

To run unit-tests for a specific module:

.. code-block:: bash

   $ pytest ./tests/test_heap.py

To run all the unit-tests and produce a coverage report:

.. code-block:: bash

   $ pytest -n 2 --cov=src

..   How to uninstall?
     =================


Where to find?
==============

Primary repository:

https://github.com/algos-all/algos-py

Secondary (mirror) repository:

https://gitlab.com/alisianoi/algos-py

Release procedure:

.. code-block:: bash

   $ python setup.py check --restructuredtext
   $ # change version in setup.py
   $ git add setup.py
   $ git commit -m "Bump version to 1.0.0"
   $ git tag v1.0.0
   $ git push github main && git push github --tags
   $ git push gitlab main && git push gitlab --tags
   $ pip install --upgrade wheel
   $ python setup.py bdist_wheel
   $ pip install --upgrade twine
   $ twine upload ./dist/algos_py-1.0.0-py3-none-any.whl


.. _travis-ci.org: https://travis-ci.org/alisianoi/algos-py
.. _travis: travis-ci.org_
.. _appveyor.com: https://ci.appveyor.com/project/alisianoi/algos-py
.. _appveyor: appveyor.com_
.. _coveralls.io: https://coveralls.io/github/alisianoi/algos-py
.. _coveralls: coveralls.io_
.. _codecov.io: https://codecov.io/gh/alisianoi/algos-py
.. _codecov: codecov.io_
.. _nose: https://nose.readthedocs.io/en/latest/
.. _pytest: https://docs.pytest.org/en/latest/
.. _git: https://git-scm.com/
.. _github.com: https://github.com
.. _github: github.com_
.. _gitlab.com: https://gitlab.com
.. _gitlab: gitlab.com_
.. _sphinx: http://www.sphinx-doc.org/en/stable/
.. _readthedocs.org: https://readthedocs.org/
.. _readthedocs: readthedocs.org_
