from Check_webaddress import check_web_address
import unittest

class Test(unittest.TestCase):
    def test_basic(self):
        testcase = "gmail.com"
        expected = True
        self.assertEqual(check_web_address(testcase), (expected))

unittest.main()
