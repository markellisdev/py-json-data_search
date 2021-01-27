# Third-party imports...
from nose.tools import assert_true, assert_is_not_none
import unittest, requests

# Standard library imports...
from unittest.mock import Mock, patch

#Local imports
from findIP import IPAddress


"""
Initial test to see that actual response is returned
"""
# def test_request_response():
#     # Send a request to the API server and store the response.
#     response = IPAddress.getResponse(IPAddress.url)

#     # If the request is sent successfully, then I expect a response to be returned.
#     assert_is_not_none(response)

"""
Not yet working mock because need access requests.get direct
"""

@patch('findIP.requests.get')
def test_getting_API_response(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.status_code = 200

    # Call the service, which will send a request to the server.
    operUrl = IPAddress.getResponse('https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix')

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(operUrl)


if __name__ == "__main__":
    unittest.main()
