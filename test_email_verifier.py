import unittest
from email_verifier import *


class TestEmailVerifier(unittest.TestCase):

    def test_empty_address(self):
        self.assertFalse(is_valid_email(''))

    def test_contains_at(self):
        self.assertTrue(is_valid_email('testemail@domain.com'))

    def test_leading_characters(self):
        self.assertFalse(is_valid_email('@domain.com'))

    def test_first_character_non_numeric(self):
        self.assertFalse(is_valid_email('1asdf@domain'))

    def test_domain_format(self):
        self.assertFalse(is_valid_email('testemail@domain'))

    def test_double_periods(self):
        self.assertFalse(is_valid_email('test..email@domain.com'))

    def test_allow_symbols(self):
        self.assertTrue(is_valid_email('testemail!$%*+-=?^_{|}~@domain.com'))

    def test_disallowed_symbols(self):
        self.assertFalse(is_valid_email('testemail"\'`'))


if __name__ == '__main__':
    unittest.main()
