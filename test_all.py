import re

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
            'Origin': 'https://example.com',
        }.items())
        self.getPage('/', headers=headers)
        self.assertBody('hello')
        self.assertHeader('Access-Control-Allow-Origin', 'https://example.com')


class CORSSimpleServerTests(CORSRequests, helper.CPWebCase):

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


class CORSSimpleDecoratorTests(CORSRequests, helper.CPWebCase):

    @staticmethod
    def setup_server():
        class Root:

            @cherrypy.expose
            @cherrypy_cors.tools.expose()
            def index(self):
                return "hello"

        cherrypy.tree.mount(Root())

        cherrypy_cors.install()


class OriginRequests(object):
    trusted_origin = 'https://example.com'
    untrusted_origin = 'http://attacker.com'

    def test_bare_request(self):
        self.getPage('/')
        self.assertBody('hello')
        self.assertNoHeader('Access-Control-Allow-Origin')

    def test_matching_origin_request(self):
        headers = list({
            'Origin': self.trusted_origin,
        }.items())
        self.getPage('/', headers=headers)
        self.assertBody('hello')
        self.assertHeader('Access-Control-Allow-Origin', self.trusted_origin)

    def test_non_matching_origin_request(self):
        headers = list({
            'Origin': self.untrusted_origin,
        }.items())
        self.getPage('/', headers=headers)
        self.assertBody('hello')
        self.assertNoHeader('Access-Control-Allow-Origin')

    def test_preflight_request(self):
        headers = list({
            'Origin': self.trusted_origin,
        }.items())
        self.getPage('/', method='OPTIONS', headers=headers)
        self.assertBody('hello')
        self.assertHeader('Access-Control-Allow-Origin', self.trusted_origin)

    def test_non_matching_preflight_request(self):
        headers = list({
            'Origin': self.untrusted_origin,
        }.items())
        self.getPage('/', method='OPTIONS', headers=headers)
        self.assertBody('hello')
        self.assertNoHeader('Access-Control-Allow-Origin')


class CORSOriginServerTests(OriginRequests, helper.CPWebCase):

    @staticmethod
    def setup_server():
        class Root:

            @cherrypy.expose
            def index(self):
                return "hello"

        origins = 'http://example.com', 'https://example.com'
        config = {
            '/': {
                'cors.expose.on': True,
                'cors.expose.origins': origins,
                'cors.preflight.origins': origins,
            },
        }
        cherrypy.tree.mount(Root(), config=config)

        cherrypy_cors.install()


class CORSOriginRegexTests(OriginRequests, helper.CPWebCase):
    trusted_origin = 'https://svr5.example.com'
    untrusted_origin = 'http://example.com'

    @staticmethod
    def setup_server():
        class Root:

            @cherrypy.expose
            def index(self):
                return "hello"

        pattern = re.compile(r'(http|https)://svr[1-9]\.example\.com')
        config = {
            '/': {
                'cors.expose.on': True,
                'cors.expose.origins': [pattern],
                'cors.preflight.origins': [pattern],
            },
        }
        cherrypy.tree.mount(Root(), config=config)

        cherrypy_cors.install()
