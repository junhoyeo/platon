from platon.lexer import Lexer
from platon.lexer.token_types import TokenType
import unittest

def filter_type(tokens):
    return [token.type for token in tokens]

def filter_value(tokens):
    return [token.value for token in tokens]

class TokenizeNumber(unittest.TestCase):

    def test_number(self):
        tokens = Lexer('1 + 2').lex()
        self.assertEqual(filter_type(tokens), [
            TokenType.NUMBER,
            TokenType.PLUS,
            TokenType.NUMBER,
            TokenType.EOF
        ])
        self.assertEqual(filter_value(tokens), [1, '+', 2, None])

    def test_multidigit_number(self):
        tokens = Lexer('1 + 11 - 55').lex()
        self.assertEqual(filter_type(tokens), [
            TokenType.NUMBER,
            TokenType.PLUS,
            TokenType.NUMBER,
            TokenType.MINUS,
            TokenType.NUMBER,
            TokenType.EOF
        ])
        self.assertEqual(filter_value(tokens), [1, '+', 11, '-', 55, None])

if __name__ == '__main__':
    unittest.main()
