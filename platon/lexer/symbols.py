from .token_types import TokenType

numerals = {
    'b': 2,
    'o': 8,
}

operators = {
    ' ': TokenType.BLANK,
    '-': TokenType.MINUS,
    '+': TokenType.PLUS,
    '=': TokenType.EQUAL,
    '*': TokenType.STAR,
    '/': TokenType.SLASH,
    '.': TokenType.DOT,
    ',': TokenType.COMMA,
    ':': TokenType.COLON,
    ';': TokenType.SEMICOLON,
    '!': TokenType.EXCLAIM,
    '?': TokenType.QUESTION,
    '>': TokenType.GREATER,
    '<': TokenType.LESS,
    '[': TokenType.BRACKET_START,
    ']': TokenType.BRACKET_CLOSE,
    '{': TokenType.BRACE_START,
    '}': TokenType.BRACE_CLOSE,
    '(': TokenType.PAREN_START,
    ')': TokenType.PAREN_CLOSE,
}
