#!/usr/bin/env python
import unittest
from check_luhn import luhn_checksum


class LuhnTests(unittest.TestCase):
    """Test class to test luhn_checksum """

    def setUp(self):
        """Tests set up"""
        pass

    def tearDown(self):
        pass

    def test_list_of_elements(self):
        """Test Luhn_checksum with test creditcard numbers"""

        self.assertTrue(luhn_checksum(4532015112830366))
        self.assertTrue(luhn_checksum(6011514433546201))
        self.assertTrue(luhn_checksum(6771549495586802))

if __name__ == '__main__':
    unittest.main()