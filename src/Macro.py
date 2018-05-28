import ply.lex as lex
import ply.yacc as yacc

class Macro:

    def __init__(self, ident, reglist, body):
        self.ID = ident
        self.reglist = reglist
        self.body = body
