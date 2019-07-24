from platon.lexer.token_types import TokenType
from . import lexResult
import unittest


class TokenizeIdentifier(unittest.TestCase):

    def test_identifier(self):
        '''tokenizing identifiers'''
        self.assertEqual(lexResult('foo')[0], (TokenType.IDENTIFIER, 'foo'))
        self.assertEqual(lexResult('Foo')[0], (TokenType.IDENTIFIER, 'Foo'))

    def test_identifier_with_numbers(self):
        '''tokenizing identifiers with numbers'''
        self.assertEqual(lexResult('foo_123')[0], (TokenType.IDENTIFIER, 'foo_123'))
        self.assertEqual(lexResult('_123')[0], (TokenType.IDENTIFIER, '_123'))

    def test_identifier_with_underscore(self):
        '''tokenizing identifiers with underscore'''
        self.assertEqual(lexResult('foo_bar')[0], (TokenType.IDENTIFIER, 'foo_bar'))
        self.assertEqual(
            lexResult('_foo')[0],
            (TokenType.IDENTIFIER,
             '_foo'),
            'identifier can start with underscore')

    def test_identifier_startwith_number(self):
        '''identifiers starting with numbers should not be valid'''
        self.assertNotEqual(
            lexResult('1_foo'),
            (TokenType.IDENTIFIER,
             '1_foo'),
            'identifier cannot start with a number')
