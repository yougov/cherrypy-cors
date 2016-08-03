import cherrypy
from cherrypy.test import helper

import cherrypy_cors

class CORSServerTests(helper.CPWebCase):

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
