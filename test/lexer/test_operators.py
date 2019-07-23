from platon.lexer.token_types import TokenType
from . import lexResult
import unittest

class TokenizeOperator(unittest.TestCase):
    
    def test_blank(self):
        '''tokenizing blank char'''
        self.assertEqual(lexResult(' ')[0], (TokenType.BLANK, ' '),
            'parse blank to blank')

    def test_minus(self):
        '''tokenizing minus operator'''
        self.assertEqual(lexResult('-')[0], (TokenType.MINUS, '-'),
            'parse - to -')

    def test_plus(self):
        '''tokenizing plus operator'''
        self.assertEqual(lexResult('+')[0], (TokenType.PLUS, '+'),
            'parse + to +')

    def test_equal(self):
        '''tokenizing equal operator'''
        self.assertEqual(lexResult('=')[0], (TokenType.EQUAL, '='),
            'parse = to =')
