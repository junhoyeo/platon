from enum import Enum, auto


class TokenType(Enum):
    BLANK = auto()
    MINUS = auto()
    PLUS = auto()
    EQUAL = auto()
    STAR = auto()
    SLASH = auto()
    DOT = auto()
    COMMA = auto()
    COLON = auto()
    SEMICOLON = auto()
    EXCLAIM = auto()
    QUESTION = auto()
    GREATER = auto()
    LESS = auto()
    BRACKET_START = auto()
    BRACKET_CLOSE = auto()
    BRACE_START = auto()
    BRACE_CLOSE = auto()
    PAREN_START = auto()
    PAREN_CLOSE = auto()

    NUMBER = auto()
    STRING = auto()

    IDENTIFIER = auto()

    EOF = auto()

    VAL = 'val'
    VAR = 'var'

    @classmethod
    def has_keyword(cls, value):
        return any(keyword.value == value for keyword in cls)
