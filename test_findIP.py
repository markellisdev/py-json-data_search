# Third-party imports...
from nose.tools import assert_true, assert_is_not_none, assert_equal
import unittest, requests
from requests.models import Response

# Standard library imports...
from unittest.mock import Mock, patch

#Local imports
from findIP import IPAddress


# """
# Initial test to see that actual response is returned
# """
# def test_request_response():
#     # Send a request to the API server and store the response.
#     response = IPAddress.getResponse(IPAddress.url)

#     # If the request is sent successfully, then I expect a response to be returned.
#     assert_is_not_none(response)

"""
Test to see that IP is properly validated
"""

def test_for_valid_IP():
    # Valid IP Address
    ip = '2.56.32.0'

    # Function will return true if IP is valid.
    assert_equal(IPAddress.validateIP(ip), True)

"""
Test to see that dict is returned
"""

def test_for_converting_json_to_dict():
    # Test dictionary resembling actual return
    testDictionary = {"ipv4": ["2.56.32.0\\/22", "2.56.164.0\\/22"]}

    # Mock response object to test with
    the_response = Response()
    the_response.code = "expired"
    the_response.error_type = "expired"
    the_response.status_code = 400
    the_response._content = b'{"ipv4": ["2.56.32.0\\/22", "2.56.164.0\\/22"]}'

    # Assert that dictionary type is returned, compared with testDictionary above
    assert_equal(type(IPAddress.convertResponseToDict(the_response)), type(testDictionary))


if __name__ == "__main__":
    unittest.main()
