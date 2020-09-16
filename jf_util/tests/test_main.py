from unittest import TestCase

from jf_util import pprint_helper

class TestMain(TestCase):
    def test_pprint(self):
        fake_dict = {
            'a': {
                'b': 'c'
            }
        }
        out = pprint_helper(fake_dict)
        same_dict = out == "a: \n\tb: c\n"
        self.assertTrue(same_dict)