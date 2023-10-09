import sys
from sly import Lexer, Parser

class NolangLexer(Lexer):
    tokens = {ID}
    ignore = ' \t'

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def error(self, t):
        print(f"illegal character '{t.value[0]}'")
        self.index += 1

class NolangParser(Parser):
    tokens = NolangLexer.tokens

    def __init__(self):
        self.names = {}

    @_('ID')
    def statement(self, p):
        pass

    def error(self, p):
        if p:
            print(f"syntax error at '{p.value}'")
        else:
            print("syntax error at EOF")

if __name__ == '__main__':
    lexer = NolangLexer()
    parser = NolangParser()

    while True:
        try:
            data = input('nolang:~$ ')
        except EOFError:
            break
        if not data:
            continue
        parser.parse(lexer.tokenize(data))