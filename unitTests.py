import unittest
from main import json_method


class TestJsonMethod(unittest.TestCase):
    # pure_JSON.json ---> correct file
    def test_sunny_road(self):
        self.assertFalse(json_method(), msg='Value should be False')

    # test_JSON_5.json ---> 3 asteriks in Resources file
    def test_rainy_road(self):
        self.assertTrue(json_method(), msg='Value should be True')

    # last method is basically for every other type of edge cases (can't really test them,
    # script is in loop until user chooses correct file):

    # test_JSON_2.json ---> missing PolicyDocument (required)
    # test_JSON_3.txt ---> txt file
    # test_JSON_4.txt ---> empty JSON file
    # test_JSON_6.txt ---> missing Resources

    def test_last(self):
        self.assertFalse(json_method(), msg='Value should be False')

if __name__ == '__main__':
    unittest.main()
