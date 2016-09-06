"""
Run this simple example with
`rwt <https://pypi.io/project/rwt>`_ or install the
requirements and run it directly with Python.

Once the server is running, connect to it to verify
that the CORS functionality is present::

    $ curl -v -H "Origin: http://www.mysite.org" http://localhost:8080
    * Rebuilt URL to: http://localhost:8080/
    *   Trying 127.0.0.1...
    * Connected to localhost (127.0.0.1) port 8080 (#0)
    > GET / HTTP/1.1
    > Host: localhost:8080
    > User-Agent: curl/7.43.0
    > Accept: */*
    > Origin: http://www.mysite.org
    >
    < HTTP/1.1 200 OK
    < Date: Mon, 01 Aug 2016 15:40:34 GMT
    < Vary: Origin
    < Content-Type: text/html;charset=utf-8
    < Server: CherryPy/7.1.0
    < Access-Control-Allow-Origin: http://www.mysite.org
    < Content-Length: 21
    <
    {"value": "success"}
    * Connection #0 to host localhost left intact
"""

__requires__ = [
    'cherrypy_cors',
]

import cherrypy
import cherrypy_cors


class MyResource:

    @cherrypy.expose()
    def index(self):
        return '{"value": "success"}\n'

    @classmethod
    def run(cls):
        cherrypy_cors.install()
        config = {
            '/': {
                'cors.expose.on': True,
            },
        }
        cherrypy.quickstart(cls(), config=config)


__name__ == '__main__' and MyResource.run()
