.. _ref-installation:

============
Installation
============

1. Install from GitHub_ (PyPI will be available later) ::

       pip install git+https://github.com/jibaku/django-textprocessor.git#egg=textprocessor

2. Add 'textprocessor' to your ``INSTALLED_APPS`` ::

       INSTALLED_APPS = (
           'textprocessor',
       )

3. Install the dependancies using ``required.txt`` from the root of the project
   if you are using a checkout. Either it's handled by setup.py. Currently the
   following dependancies are needed :

 * `markdown <https://pypi.python.org/pypi/Markdown>`_

4. Enjoy.

.. _GitHub: https://github.com/jibaku/django-textprocessor

