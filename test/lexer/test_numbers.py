from platon.lexer.token_types import TokenType
from . import lexResult
import unittest


class TokenizeNumber(unittest.TestCase):

    def test_numbers(self):
        '''tokenizing single-digit numbers'''
        self.assertEqual(lexResult('0')[0], (TokenType.NUMBER, 0),
                         'parse 0 to 0')
        self.assertEqual(lexResult('1')[0], (TokenType.NUMBER, 1),
                         'parse 1 to 1')

    def test_multidigit_numbers(self):
        '''tokenizing of multi-digit numbers'''
        self.assertEqual(lexResult('10')[0], (TokenType.NUMBER, 10),
                         'parse 10 to 10')
        self.assertEqual(lexResult('120')[0], (TokenType.NUMBER, 120),
                         'parse 120 to 120')
        self.assertEqual(lexResult('99999')[0], (TokenType.NUMBER, 99999),
                         'parse 99999 to 99999')

    def test_float_numbers(self):
        '''parsing floats'''
        self.assertEqual(lexResult('0.5')[0], (TokenType.NUMBER, 0.5),
                         'parse 0.5 to 0.5')
        self.assertEqual(lexResult('1.2')[0], (TokenType.NUMBER, 1.2),
                         'parse 1.2 to 1.2')

    def test_binary_numerals(self):
        '''parsing binary'''
        self.assertEqual(lexResult('0b0')[0], (TokenType.NUMBER, 0),
                         'parse 0b0 to 0')
        self.assertEqual(lexResult('0b101')[0], (TokenType.NUMBER, 5),
                         'parse 0b101 to 5')
        self.assertEqual(lexResult('0b1001110')[0], (TokenType.NUMBER, 78),
                         'parse 0b1001110 to 78')

    def test_octal_numerals(self):
        '''parsing octal'''
        self.assertEqual(lexResult('0o0')[0], (TokenType.NUMBER, 0),
                         'parse 0o0 to 0')
        self.assertEqual(lexResult('0o7')[0], (TokenType.NUMBER, 7),
                         'parse 0o7 to 7')
        self.assertEqual(lexResult('0o704')[0], (TokenType.NUMBER, 452),
                         'parse 0o704 to 452')


if __name__ == '__main__':
    unittest.main()
