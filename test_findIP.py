# Third-party imports...
from nose.tools import assert_true, assert_is_not_none, assert_equal
import unittest, requests

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
Simple test to confirm there is return value. Will be improved next
"""

@patch('findIP.requests.get')
def test_getting_API_response(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.status_code = 400

    # Call the service, which will send a request to the server.
    operUrl = IPAddress.getResponse('url')

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(operUrl)

"""
Test to see that IP is properly validated
"""

def test_for_valid_IP():
    # Valid IP Address
    ip = '2.56.32.0'

    # Function will return true if IP is valid.
    assert_equal(IPAddress.validateIP(ip), True)


if __name__ == "__main__":
    unittest.main()
