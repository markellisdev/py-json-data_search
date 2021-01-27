import unittest
from findIP import IPAddress


class TestFunc(unittest.TestCase):
    """
    Test Case for User Input function
    """
    def test_user_input_is_not_null(self):
        # self.assertIsNotNone(findIP.userInput)
        pass

    def getresponse_returns_valid_json(self):
        self.assertIsNotNone(IPAddress.getResponse(IPAddress.url))


if __name__ == "__main__":
    unittest.main()
