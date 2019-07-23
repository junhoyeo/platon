from platon.lexer import Lexer

if __name__ == '__main__':
    code = '1+2'
    lexer = Lexer(code)
    tokens = lexer.lex()
    print(*tokens, sep='\n')
