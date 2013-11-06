cherrypy_cors
=============

CORS support for CherryPy

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
