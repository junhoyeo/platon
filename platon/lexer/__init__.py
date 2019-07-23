from typing import List
from .token import Token
from .token_types import TokenType

class Lexer():
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
    
    def lex(self) -> List[Token]:
        while self.current < len(self.source):
            self.start = self.current
            self.tokenize()
        
        self.tokens.append(Token(TokenType.EOF, None))
        return self.tokens
    
    def tokenize(self):
        char = self.next()

        if char == '+':
            self.tokens.append(Token(TokenType.PLUS, '+'))

        if char.isdigit():
            peek = self.peek()
            while peek and peek.isdigit() or peek == '.':
                self.next()

            self.tokens.append(
                Token(
                    TokenType.NUMBER,
                    float(self.source[self.start: self.current])
                )
            )

    def next(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def peek(self) -> str:
        if self.current >= len(self.source):
            return None
        return self.source[self.current]
