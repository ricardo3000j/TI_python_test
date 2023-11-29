import unittest
import main


class TestMainApp(unittest.TestCase):
    """Test case for main app"""
    def test_main_app(self):
        output = main.app()
        expected_result = [2, 4, 2]
        self.assertEqual(output, expected_result)


if __name__ == "__main__":
    unittest.main()
