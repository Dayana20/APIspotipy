import unittest
import spotipy
from filename import setting_up, calling


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(setting_up(1), 0)

    def test_function2(self):
        self.assertEqual(calling(2 , 1), 3)
        self.assertEqual(calling(2.1 , 1.2), 3.3)

if __name__ == '__main__':
    unittest.main()