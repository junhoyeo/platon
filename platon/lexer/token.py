from .token_types import TokenType

class Token():
    def __init__(self, _type: TokenType, _value):
        self.type = _type
        self.value = _value

    def __repr__(self):
        return 'Token({}, {})'.format(self.type, self.value)
