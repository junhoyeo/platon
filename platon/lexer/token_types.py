from enum import Enum, auto

class TokenType(Enum):
    PLUS = auto()
    EQUAL = auto()

    NUMBER = auto()

    IDENTIFIER = auto()

    EOF = auto()

    VAL = 'val'
    VAR = 'var'

    @classmethod
    def has_keyword(cls, value):
        return any(keyword.value == value for keyword in cls)
