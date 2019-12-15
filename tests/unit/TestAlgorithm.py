import unittest
from generateKeyboardDirections import *


class TestAlgorithm(unittest.TestCase):

    def test_get_character_index(self):
        data = ['a', 'b', 'c']

        for i in range(len(data)):
            if i == 0:
                result = get_character_index(data[i])
                self.assertEqual(result, [0, 0], "Should be [0, 1]")
            if i == 1:
                result = get_character_index(data[i])
                self.assertEqual(result, [0, 1], "Should be [0, 1]")
            if i == 2:
                result = get_character_index(data[i])
                self.assertEqual(result, [0, 2], "Should be [0, 2]")

            i += 1

    def test_enter_text(self):
        text = 'hint1'
        result = enter_text(text)
        expected_result = [
            'down', 'select', 'right', 'select', 'right', 'right', 'right', 'right', 'right', 
            'select', 'down', 'left', 'select', 'up', 'up', 'right', 'right', 'select']
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
