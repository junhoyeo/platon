from platon.lexer.token_types import TokenType
from . import lexResult
import unittest

class TokenizeNumber(unittest.TestCase):

    def test_number(self):
        '''한 자리 정수 토크나이징'''
        self.assertEqual(lexResult('0')[0], (TokenType.NUMBER, 0))
        self.assertEqual(lexResult('1')[0], (TokenType.NUMBER, 1))

    def test_multidigit_number(self):
        '''여러 자리 정수 토크나이징'''
        self.assertEqual(lexResult('10')[0], (TokenType.NUMBER, 10))
        self.assertEqual(lexResult('120')[0], (TokenType.NUMBER, 120))
        self.assertEqual(lexResult('99999')[0], (TokenType.NUMBER, 99999))
    
    def test_float_number(self):
        '''실수 파싱'''
        self.assertEqual(lexResult('0.5')[0], (TokenType.NUMBER, 0.5))
        self.assertEqual(lexResult('1.2')[0], (TokenType.NUMBER, 1.2))

    def test_numerals_bin(self):
        '''2진수 파싱'''
        self.assertEqual(lexResult('0b0')[0], (TokenType.NUMBER, 0))
        self.assertEqual(lexResult('0b101')[0], (TokenType.NUMBER, 5))
        self.assertEqual(lexResult('0b1001110')[0], (TokenType.NUMBER, 78))

    def test_numerals_oct(self):
        '''8진수 파싱'''
        self.assertEqual(lexResult('0o0')[0], (TokenType.NUMBER, 0))
        self.assertEqual(lexResult('0o7')[0], (TokenType.NUMBER, 7))
        self.assertEqual(lexResult('0o704')[0], (TokenType.NUMBER, 452))

if __name__ == '__main__':
    unittest.main()
