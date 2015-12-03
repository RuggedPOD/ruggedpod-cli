# RuggedPOD management API
#
# Copyright (C) 2015 Guillaume Giamarchi <guillaume.guillaume@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import json

import requests
import xmltodict


class RuggedPODClient:
    """
    RuggedPOD API client
    """
    def __init__(self, url, username, password, debug=False):
        self.url = url
        self.username = username
        self.password = password
        self.debug = debug
        self.cookies = {}
        self.auth_cookie_name = "X-Auth-Token"

    def action(self, action, blade_id=None):
        if self.auth_cookie_name not in self.cookies:
            self._authenticate()
        pattern = "%s/%s"
        if blade_id:
            pattern += "?bladeId=%s" % blade_id
        response = self._do_request('GET', pattern % (self.url, action), cookies=self.cookies)

        data = self.to_dict(xmltodict.parse(response.text))

        data = data[data.keys()[0]]
        if not blade_id:
            data = data[data.keys()[0]]

        return data

    def _authenticate(self):
        r = self._do_request('POST', "%s/token?username=%s&password=%s" % (self.url, self.username, self.password))
        self.cookies[self.auth_cookie_name] = r.cookies[self.auth_cookie_name]

    def _do_request(self, method, url, cookies=None):
        requests.packages.urllib3.disable_warnings()
        try:
            if self.debug:
                self._stderr('-' * 78)
                self._stderr('Request  | Method      | %s' % method)
                self._stderr('Request  | URL         | %s' % url)
            response = requests.request(method, url, verify=False, timeout=10, cookies=cookies)
        except requests.exceptions.RequestException as error:
            print 'Error: Unable to connect.'
            print 'Detail: %s' % error
            raise SystemExit(1)
        if self.debug:
            self._stderr('-' * 78)
            self._stderr('Response | Status code | %s' % response.status_code)
            self._stderr('Response | Headers     | %s' % response.headers)
            if response.text:
                self._stderr('Response | Body: %s' % response.text)
        return response

    @staticmethod
    def to_dict(ordered_dict):
        return json.loads(json.dumps(ordered_dict))

    @staticmethod
    def _stderr(text):
        sys.stderr.write("[DEBUG] %s\n" % text)
