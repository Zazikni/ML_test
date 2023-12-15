import unittest
from string import ascii_lowercase

from caesar_encrypt import encrypt


class TestEncrypt(unittest.TestCase):
    alphabet = ' ' + ascii_lowercase
    values_for_testing = (
        (('caesar cifer', 3, alphabet), 'fdhvducflihu'),
        (('abcdef', -3, alphabet), 'yz abc'),
        (('amazing string', 6, alphabet), 'gsgeotmfyzxotm'),
        (('abracadabrakedabra', -4, alphabet), 'xynxzx xynxga xynx'),
        (('very strong password', 10, alphabet), 'eoahjbcayxqjzkbbfyan'),
        (('python is great', -10, alphabet), 'fojyedqziqxhvrj'),

    )

    def test_decrypt(self):
        for input_data, expected_text in TestEncrypt.values_for_testing:
            with self.subTest(msg=' '.join(map(str, input_data)) + ' ---> ' + expected_text):
                result = encrypt(*input_data)
                self.assertEqual(expected_text, result)
