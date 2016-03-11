import unittest

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_3_2(self):
        self.assertEqual(3*2, 6)


if __name__ == '__main__':
    unittest.main()
