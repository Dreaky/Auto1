import requests
from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import json

@library(scope="GLOBAL", version="0.1")
class simpleRequests:

    def __init__(self):
        pass

    @keyword("A ${type} request to ${uri} with ${headers} and ${data} is made")
    def simple_request(self, type, uri, headers, data):
        r = requests.request(type, uri, data=str(data), headers=headers)
        BuiltIn().set_test_variable("$latestRC", r.status_code)
        logger.debug(f"Len of response.content is: {len(r.content)}")
        logger.console(f"Response.text is: {(r.text)}")
        if r.content:
            BuiltIn().set_test_variable("$latestResponse", r.text)
        else:
            BuiltIn().set_test_variable("$latestResponse", None)
        return r

    @keyword("A ${type} request to ${uri} with ${headers} and ${data} is successful")
    def simple_request_success(self, type, uri, headers, data):
        r = self.simple_request(type, uri, headers, data)
        assert r.status_code == 200, f"RC is: {r.status_code}, but should be: {200}\nBody: {r.text}"
        return r

    @keyword("A ${type} request with expected RC ${rc} to ${uri} with ${headers} and ${data} is made")
    def simple_request_rc(self, type, rc, uri, headers, data):
        r = self.simple_request(type, uri, headers, data)
        assert r.status_code == rc, f"RC is: {r.status_code}, but should be: {rc}\nBody: {r.text}"
        return r

    @keyword("Latest RC should be ${expected_rc}")
    def assert_response_code(self, expected_rc):
        latestRC = BuiltIn().get_variables()["${latestRC}"]
        assert latestRC == expected_rc, f"Latest RC: {latestRC} is not as expected: {expected_rc}"

    @keyword("Response ${response} should be ${expected_json}")
    def assert_response_json(self,response, expected_json):

        if expected_json is None:
            assert expected_json == response, f'Latest response should be None, but it is: {response}'
        else:
            json_reposne = json.loads(response)
            assert json_reposne == expected_json, f"Latest response: {json_reposne} is not as expected: {expected_json}"

    @keyword("Latest response text should be ${expected_string}")
    def assert_response_text(self, expected_string):
        latestResponse = BuiltIn().get_variables()["${latestResponse}"]
        assert latestResponse == expected_string, f"Latest response: {latestResponse} is not as expected: {expected_string}"
