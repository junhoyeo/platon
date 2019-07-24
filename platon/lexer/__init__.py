from typing import List
from .token import Token
from .token_types import TokenType
from .symbols import numerals, operators


def isdigit(char: str) -> bool:
    return False if not char else char.isdigit()


def isalpha(char: str) -> bool:
    return False if not char else char.isalpha() or char == '_'


class Lexer():
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def lex(self) -> List[Token]:
        while self.current < len(self.source):
            self.start = self.current
            self.tokenize()

        self.add_token(TokenType.EOF, None)
        return self.tokens

    def tokenize(self) -> None:
        char = self.next()

        for op in operators.keys():
            if char == op:
                self.add_token(operators[op], op)
                return

        if char.isdigit():
            while isdigit(self.peek()):
                self.next()
            peek = self.peek()
            if peek == '.':  # float
                self.next()
                while isdigit(self.peek()):
                    self.next()
            for n in numerals.keys():
                if peek == n:
                    self.next()
                    while True:
                        peek = self.peek()
                        if not isdigit(peek):
                            break
                        elif int(peek) not in range(numerals[n]):
                            raise SyntaxError('invalid token')
                        self.next()
                    self.add_token(
                        TokenType.NUMBER,
                        eval(self.source[self.start: self.current])
                    )
                    return
            self.add_token(
                TokenType.NUMBER,
                float(self.source[self.start: self.current])
            )

        elif isalpha(char):
            while True:
                peek = self.peek()
                if not (isalpha(peek) or isdigit(peek)):
                    break
                self.next()
            text = self.source[self.start: self.current]
            if TokenType.has_keyword(text):
                self.add_token(TokenType(text), None)
            else:
                self.add_token(TokenType.IDENTIFIER, text)

        elif char == '\n':
            self.line += 1

        else:
            print(self.tokens)
            raise SyntaxError('invalid token')

    def next(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def peek(self) -> str:
        if self.current >= len(self.source):
            return None
        return self.source[self.current]

    def add_token(self, _type, _value) -> None:
        self.tokens.append(Token(_type, _value))
