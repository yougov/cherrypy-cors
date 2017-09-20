.. image:: https://img.shields.io/pypi/v/cherrypy_cors.svg
   :target: https://pypi.io/project/cherrypy_cors

.. image:: https://img.shields.io/pypi/pyversions/cherrypy_cors.svg

.. image:: https://img.shields.io/pypi/dm/cherrypy_cors.svg

.. image:: https://img.shields.io/travis/yougov/cherrypy-cors/master.svg
   :target: http://travis-ci.org/yougov/cherrypy-cors

CORS support for CherryPy

License
=======

License is indicated in the project metadata (typically one or more
of the Trove classifiers). For more details, see `this explanation
<https://github.com/jaraco/skeleton/issues/1>`_.

In a nutshell
=============

In your application, either install the tool globally.

.. code-block:: python

    import cherrypy_cors
    cherrypy_cors.install()

Or add it to your application explicitly.

.. code-block:: python

    import cherrypy_cors
    app = cherrypy.tree.mount(...)
    app.toolboxes['cors'] = cherrypy_cors.tools

Then, enable it in your cherrypy config. For example, to enable it for all
static resources.

.. code-block:: python

    config = {
        '/static': {
            'tools.staticdir.on': True,
            'cors.expose.on': True,
        }
    }

See `simple-example
<https://github.com/yougov/cherrypy-cors/blob/master/simple-example.py>`_
for a runnable example.
