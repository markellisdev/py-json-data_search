try:
    import unittest
    from findIP import IPAddress
    print("All modules loaded successfully!")
except:
    print("Some modules were not loaded.")

class TestFunc(unittest.TestCase):
    """
    Test Case for return of valid JSON
    """

    def getresponse_returns_valid_json(self):
        self.assertIsNotNone(IPAddress.getResponse)

if __name__ == "__main__":
    unittest.main()
