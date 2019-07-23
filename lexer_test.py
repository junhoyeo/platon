from platon.lexer import Lexer

if __name__ == '__main__':
    while 1:
        code = input('> ')
        lexer = Lexer(code)
        tokens = lexer.lex()
        print(*tokens, sep='\n')
