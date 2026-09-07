import unittest

from lesson_05.account import *

class TestAccount(unittest.TestCase):
    def test_strip_space(self):
        self.assertEqual(clean_name(" sVeta "), "Sveta")

