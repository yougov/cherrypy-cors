import cherrypy
from cherrypy.lib import set_vary_header

# FIXME: written in a hurry for the cumulus sprint
# TODO: docs and tests
# TODO: extract into cherrypy-cors

CORS_ALLOW_METHODS = 'Access-Control-Allow-Methods'
CORS_ALLOW_ORIGIN = 'Access-Control-Allow-Origin'
CORS_ALLOW_CREDENTIALS = 'Access-Control-Allow-Credentials'
CORS_EXPOSE_HEADERS = 'Access-Control-Expose-Headers'
CORS_REQUEST_METHOD = 'Access-Control-Request-Method'
CORS_REQUEST_HEADERS = 'Access-Control-Request-Headers'
CORS_MAX_AGE = 'Access-Control-Max-Age'
CORS_ALLOW_HEADERS = 'Access-Control-Allow-Headers'

tools = cherrypy._cptools.Toolbox("cors")


class CORS(object):
    def __init__(self, req_headers, resp_headers):
        self.req_headers = req_headers
        self.resp_headers = resp_headers

    def expose(self, allow_credentials, expose_headers):
        if self._is_valid_origin():
            self._add_origin_and_credentials_headers(allow_credentials)
            self._add_expose_headers(expose_headers)

    def preflight(self, allowed_methods, allowed_headers, allow_credentials,
                  max_age):
        if self._is_valid_preflight_request(allowed_headers, allowed_methods):
            self._add_origin_and_credentials_headers(allow_credentials)
            self._add_prefligt_headers(allowed_methods, max_age)

    @property
    def origin(self):
        return self.req_headers.get('Origin')

    def _is_valid_origin(self):
        # FIXME: handle whitelisting
        return self.origin is not None

    def _add_origin_and_credentials_headers(self, allow_credentials):
        self.resp_headers[CORS_ALLOW_ORIGIN] = self.origin
        if allow_credentials:
            self.resp_headers[CORS_ALLOW_CREDENTIALS] = 'true'

    def _add_expose_headers(self, expose_headers):
        if expose_headers:
            self.resp_headers[CORS_EXPOSE_HEADERS] = expose_headers

    @property
    def requested_method(self):
        return self.req_headers.get(CORS_REQUEST_METHOD)

    @property
    def requested_headers(self):
        return self.req_headers.get(CORS_REQUEST_HEADERS)

    def _is_valid_preflight_request(self, allowed_headers, allowed_methods):
        valid = True
        if not self._is_valid_origin():
            valid = False
        elif not self.requested_method:
            valid = False
        elif self.requested_method not in allowed_methods:
            valid = False
        elif self.requested_headers:
            if allowed_headers:
                for header in self.requested_headers.split(','):
                    header = header.strip()
                    if header not in allowed_headers:
                        valid = False
                        break
        return valid

    def _add_prefligt_headers(self, allowed_methods, max_age):
        rh = self.resp_headers
        rh[CORS_ALLOW_METHODS] = ', '.join(allowed_methods)
        if max_age:
            rh[CORS_MAX_AGE] = max_age
        if self.requested_headers:
            rh[CORS_ALLOW_HEADERS] = self.requested_headers


def _get_cors():
    return CORS(
        cherrypy.serving.request.headers,
        cherrypy.serving.response.headers
    )


def _safe_caching_headers():
    set_vary_header(cherrypy.serving.response, "Origin")


def expose(allow_credentials=False, expose_headers=None):
    _get_cors().expose(allow_credentials, expose_headers)
    _safe_caching_headers()


def preflight(allowed_methods, allowed_headers=None, allow_credentials=False,
              max_age=None):
    _get_cors().preflight(
        allowed_methods, allowed_headers, allow_credentials, max_age)
    _safe_caching_headers()


tools.expose = cherrypy.Tool('before_handler', expose)
tools.preflight = cherrypy.Tool('before_handler', preflight)

def install():
    """
    Install the toolbox such that it's available in all applications.
    """
    cherrypy._cptree.Application.toolboxes.update(cors=tools)
