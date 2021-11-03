Usage
=====

.. _installation:

Installation
------------

To use edaSQL, first install it using pip:

.. code-block:: console

   (.venv) $ pip install edaSQL

Importing the Package and Iniate the eda object
----------------
>>> import edaSQL
>>> edasql = edaSQL.SQL()

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

