try:
    import unittest
    import findIP
    print("All modules loaded successfully!")
except:
    print("Some modules were not loaded.")

class TestFunc(unittest.TestCase):
    """
    Test Case for User Input function
    """
    def test_user_input_is_not_null(self):
        self.assertIsNotNone(findIP.userInput)

if __name__ == "__main__":
    unittest.main()
