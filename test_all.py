import cherrypy
from cherrypy.test import helper

import cherrypy_cors


class CORSRequests(object):
    def test_bare_request(self):
        self.getPage('/')
        self.assertBody('hello')
        self.assertNoHeader('Access-Control-Allow-Origin')

    def test_CORS_request(self):
        headers = list({
            'Origin': 'example.com',
        }.items())
        self.getPage('/', headers=headers)
        self.assertBody('hello')
        self.assertHeader('Access-Control-Allow-Origin', 'example.com')


class CORSServerTests(CORSRequests, helper.CPWebCase):

    @staticmethod
    def setup_server():
        class Root:

            @cherrypy.expose
            def index(self):
                return "hello"

        config = {
            '/': {
                'cors.expose.on': True,
            },
        }
        cherrypy.tree.mount(Root(), config=config)

        cherrypy_cors.install()


class CORSDecoratorTests(CORSRequests, helper.CPWebCase):

    @staticmethod
    def setup_server():
        class Root:

            @cherrypy.expose
            @cherrypy_cors.tools.expose()
            def index(self):
                return "hello"

        cherrypy.tree.mount(Root())

        cherrypy_cors.install()
