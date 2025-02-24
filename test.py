import unittest
import subprocess


class Test01(unittest.TestCase):
    def test_standard_ten_lines(self):
        '''
        Here we will test the basic functioning of the script, printing the first ten lines of the file
        '''

        result = subprocess.check_output(["python3", "script.py", "example.txt"], text=True)
        data = f"Line 15: This is the fifteenth line.\nLine 16: This is the sixteenth line.\nLine 17: This is the seventeenth line.\nLine 18: This is the eighteenth line.\nLine 19: This is the nineteenth line.\nLine 20: This is the twentieth line.\nLine 21: This is the twenty-first line.\nLine 22: This is the twenty-second line.\nLine 23: This is the twenty-third line.\nLine 24: This is the twenty-fourth line."
        self.assertEqual(result, data)


class Test02(unittest.TestCase):
    def test_num_lines(self):
        '''
        Here we will test the basic functioning of the script, printing the first ten lines of the file
        '''

        result = subprocess.check_output(["python3", "script.py", "-n", "5", "example.txt"], text=True)
        data = f"Line 20: This is the twentieth line.\nLine 21: This is the twenty-first line.\nLine 22: This is the twenty-second line.\nLine 23: This is the twenty-third line.\nLine 24: This is the twenty-fourth line."
        self.assertEqual(result, data)


class Test03(unittest.TestCase):
    def test_num_lines_with_header(self):
        '''
        Here we will test the basic functioning of the script, printing the first ten lines of the file
        '''

        result = subprocess.check_output(["python3", "script.py", "+15", "example.txt"], text=True)
        data = f"Line 16: This is the sixteenth line.\nLine 17: This is the seventeenth line.\nLine 18: This is the eighteenth line.\nLine 19: This is the nineteenth line.\nLine 20: This is the twentieth line.\nLine 21: This is the twenty-first line.\nLine 22: This is the twenty-second line.\nLine 23: This is the twenty-third line.\nLine 24: This is the twenty-fourth line."
        self.assertEqual(result, data)