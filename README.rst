=====================================================================
 Hexagonal Architecture example in Python using Flask and SqlAlchemy
=====================================================================

------------------------
 Installation and Usage
------------------------

With Python 3.7+, pipenv, and Postgres installed, run the following:

.. highlight:: bash
.. code-block::

    $ git clone https://github.com/ajgrover/hexagonal-architecture-python.git
    $ cd hexagonal-architecture-python
    $ ./setup.sh
    $ pipenv run hex db create
    $ pipenv run hex db migrate
    $ pipenv run hex server

To run the tests:

.. code-block::

    $ pipenv run hex db create test
    $ pipenv run hex db migrate test
    $ pipenv run hex check tests