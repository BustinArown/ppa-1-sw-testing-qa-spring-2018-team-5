import unittest
from email_verifier import *


class TestEmailVerifier(unittest.TestCase):

    def test_empty_address(self):
        self.assertFalse(email_verifier(''))

    def test_contains_at(self):
        self.assertTrue(email_verifier('testemail@domain.com'))

    def test_leading_characters(self):
        self.assertFalse(email_verifier('@domain.com'))

    def test_first_character_non_numeric(self):
        self.assertFalse(email_verifier('1asdf@domain'))

    def test_domain_format(self):
        self.assertFalse(email_verifier('testemail@domain'))

    def test_double_periods(self):
        self.assertFalse(email_verifier('test..email@domain.com'))

    def test_allow_symbols(self):
        self.assertTrue(email_verifier('testemail!$%*+-=?^_{|}~@domain.com'))

    def test_disallowed_symbols(self):
        self.assertFalse(email_verifier('testemail"\'`'))


if __name__ == '__main__':
    unittest.main()
