import unittest
from markdown import handleOneHash
from markdown import handleTwoHash
from markdown import handleThreeHash
from markdown import blockQuote

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def testSingleHash(self):
        self.assertEqual(handleOneHash("# Single"), "<h1>Single</h1>")

    def testDoubleHash(self):
        self.assertEqual(handleTwoHash("## Double"), "<h2>Double</h2>")

    def testThreeHash(self):
        self.assertEqual(handleThreeHash("### Triple"), "<h3>Triple</h3>")

    def testSingleHashSent(self):
        self.assertEqual(handleOneHash("# This is a test sentence"), "<h1>This is a test sentence</h1>")

    def testDoubleHashSent(self):
        self.assertEqual(handleTwoHash("## This is a test sentence"), "<h2>This is a test sentence</h2>")

    def testThreeHashSent(self):
        self.assertEqual(handleThreeHash("### This is a test sentence"), "<h3>This is a test sentence</h3>")



if __name__ == '__main__':
    unittest.main()
