import ply.lex as lex
import ply.yacc as yacc

class Program:

    def __init__(self, file_url):
        self.file = open(file_url, mode='r')

    def tokenize():
        pass

    def parse_tree():
        pass

    def replace_macro():
        pass

    def evaluate():
        pass

    def run():
        self.tokenize()
        self.parse_tree()
        self.replace_macro()
        self.evaluate()
