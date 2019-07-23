from typing import List
from .token import Token
from .token_types import TokenType

def isdigit(char: str):
    if char == None:
        return False
    return char.isdigit()

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

        elif char.isdigit():
            while isdigit(self.peek()):
                self.next()

            if self.peek == '.':
                self.next()

                while isdigit(self.peek()):
                    self.next()

            self.tokens.append(
                Token(
                    TokenType.NUMBER,
                    float(self.source[self.start: self.current])
                )
            )
        
        elif char == ' ':
            pass

        else:
            exit(1)

    def next(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def peek(self) -> str:
        if self.current >= len(self.source):
            return None
        return self.source[self.current]
