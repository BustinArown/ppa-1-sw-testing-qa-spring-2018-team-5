import unittest
from email_verifier import *


class TestEmailVerifier(unittest.TestCase):

    def test_contains_at(self):
        self.assertTrue(is_valid_email('testemail@domain.com'))

if __name__ == '__main__':
    unittest.main()
