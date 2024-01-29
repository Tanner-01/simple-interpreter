"""
l et five = 5; 
let ten = 10; 

let add = fn( x, y) {
    x + y; 
}; 

let result = add( five, ten);

"""

from tokens import *

class Lexer:
    input = None
    input_length = None
    position = None
    read_position = None
    ch = None

    def __init__(self, source):
        self.input = source
        self.input_length = len(self.input)
        self.position = -1
        self.read_position = 0

        self.read_char()

    def read_char(self):
        if self.read_position >= self.input_length:
            self.ch = None
        else:
            self.ch = self.input[self.read_position]
        
        self.position = self.read_position
        self.read_position += 1

    def next_token(self):
        tok = None

        if self.ch == "=":
            tok = Token(tokens["ASSIGN"], self.ch)
        elif self.ch == ";":
            tok = Token(tokens["SEMICOLON"], self.ch)
        elif self.ch == "(":
            tok = Token(tokens["LPAREN"], self.ch)
        elif self.ch == ")":
            tok = Token(tokens["RPAREN"], self.ch)
        elif self.ch == ",":
            tok = Token(tokens["COMMA"], self.ch)
        elif self.ch == "+":
            tok = Token(tokens["PLUS"], self.ch)
        elif self.ch == "{":
            tok = Token(tokens["LBRACE"], self.ch)
        elif self.ch == "}":
            tok = Token(tokens["RBRACE"], self.ch)
        else:
            tok = Token(tokens["EOF"], "")
        
        self.read_char()
        return tok
