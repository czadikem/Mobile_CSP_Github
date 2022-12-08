"""
Copyright (c) 2016-2020 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import urllib.parse
import os
from programy.services.base import ServiceQuery
from programy.services.rest.base import RESTService
from programy.services.rest.base import RESTServiceException


class GenericServiceQuery(ServiceQuery):

    @staticmethod
    def create(service):
        return GenericServiceQuery(service)

    def parse_matched(self, matched):
        self._query = ServiceQuery._get_matched_var(matched, 0, "query")

    def __init__(self, service):
        ServiceQuery.__init__(self, service)
        self._query = None

    def execute(self):
        return self._service.generic(self._query)

    def aiml_response(self, response):
        payload = response['response']['payload']
        return payload['result']


class GenericServiceException(RESTServiceException):

    def __init__(self, msg):
        RESTServiceException.__init__(self, msg)


class GenericService(RESTService):
    """
    """
    PATTERNS = [
        [r"SEARCH\s(.+)", GenericServiceQuery]
    ]

    def __init__(self, configuration):
        RESTService.__init__(self, configuration)

    def patterns(self) -> list:
        return GenericService.PATTERNS

    def get_default_aiml_file(self):
        return os.path.dirname(__file__) + os.sep + "generic.aiml"

    @staticmethod
    def get_default_conf_file():
        return os.path.dirname(__file__) + os.sep + "generic.conf"

    def _build_generic_url(self, question):
        url = self.configuration.url.format(question)
        return url

    def generic(self, question):
        url = self._build_generic_url(question)
        response = self.query('generic', url)
        return response

    def _response_to_json(self, api, response):
        return response.json()

