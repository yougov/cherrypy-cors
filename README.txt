cherrypy_cors
=============

CORS support for CherryPy

Usage
=====

In your application, either install the tool globally::

    import cherrypy_cors
    cherrypy_cors.install()

Or add it to your application explicitly::

    import cherrypy_cors
    app = cherrypy.tree.mount(...)
    app.toolboxes['cors'] = cherrypy_cors.tools

Then, enable it in your cherrypy config. For example, to enable it for all
static resources::

    config = {
        '/static': {
            'tools.staticdir.on': True,
            'cors.expose.on': True,
        }
    }
