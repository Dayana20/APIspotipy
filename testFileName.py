import unittest
from filename import *


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(setting_up(1, 1), 1)

    def test_function2(self):
        self.assertEqual(calling(None), 1)


if __name__ == '__main__':
    unittest.main()
