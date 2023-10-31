import unittest
from python_alpha import add

class TestSuiteA(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 2), 12)

if __name__ == '__main__':
    unittest.main()
