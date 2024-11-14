# file_tests.py

import unittest
from unittest.mock import patch
import sys
import io
from file import main

class TestFileProgram(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file
        with open("test_input.txt", "w") as f:
            f.write("1.5 2.3\n")
            f.write("4.1 5.2\n")
            f.write("7.2\n")  # Missing one value
            f.write("eight 3.4\n")  # Non-numeric value
            f.write("9.0 10.5\n")

    def tearDown(self):
        # Remove the temporary test file after tests
        import os
        os.remove("test_input.txt")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch.object(sys, 'argv', ['file.py', 'test_input.txt'])
    def test_file_program(self, mock_stdout):
        main()
        output = mock_stdout.getvalue()

        # Check for expected outputs and error messages
        self.assertIn("Sum on line 1: 3.8", output)
        self.assertIn("Sum on line 2: 9.3", output)
        self.assertIn("Error on line 3: Expected 2 values, but got 1.", output)
        self.assertIn("Error on line 4: Non-numeric values encountered.", output)
        self.assertIn("Sum on line 5: 19.5", output)

if __name__ == "__main__":
    unittest.main()
