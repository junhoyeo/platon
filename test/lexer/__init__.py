from platon.lexer import Lexer

def lexResult(code):
    tokens = Lexer(code).lex()
    return [(token.type, token.value) for token in tokens]
