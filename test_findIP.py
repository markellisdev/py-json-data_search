# Third-party imports...
from nose.tools import assert_true, assert_is_not_none
import unittest, requests

# Standard library imports...
from unittest.mock import Mock, patch

#Local imports
from findIP import IPAddress


@patch('findIP.IPAddress.getResponse')
def test_getting_API_response(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.status_code = 200

    # Call the service, which will send a request to the server.
    operUrl = IPAddress.getResponse()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(operUrl)


if __name__ == "__main__":
    unittest.main()
