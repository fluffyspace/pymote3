Running tests
=============
To execute tests install nose ``pip install nose`` and run it inside pymote3 
directory. All tests should be found recursively scanning directories.
To run all tests run this from root pymote3 directory::

    nosetests -v

To run selected test module::

    nosetests -v pymote3.tests.test_algorithm
    
    
Tests coverage
--------------
For tests coverage install `Coverage <http://nedbatchelder.com/code/coverage/cmd.html>`_ package and run it::

    pip install coverage
    coverage run --source=pymote3 setup.py nosetests
    
`Configuration file <http://nedbatchelder.com/code/coverage/config.html#config>`_ is in ``.coveragerc``.

Make report in console or html::

    coverage report -m
    coverage html

For integration with `coveralls <https://coveralls.io>`_ refer to `coverall readme <https://github.com/coagulant/coveralls-python/blob/master/README.rst>`_.
