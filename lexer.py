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
    
    def read_identifier(self):
        identifier = ""

        while self.is_letter(self.ch):
            identifier += self.ch
            self.read_char()

        return identifier
    
    def is_letter(self, ch):
        return 'a' <= ch and ch <= 'z' or 'A' <= ch and ch <= 'Z' or ch == '_'
    
    def read_integer(self):
        digits = ""

        while self.ch.isdigit():
            digits += self.ch
            self.read_char()

        return int(digits)

    def skip_whitespace(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.read_char()

    def next_token(self):
        tok = None

        self.skip_whitespace()

        ps = "CH: " + self.ch

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
        elif self.ch == "!":
            tok = Token(tokens["BANG"], self.ch)
        elif self.ch == "-":
            tok = Token(tokens["MINUS"], self.ch)
        elif self.ch == "/":
            tok = Token(tokens["SLASH"], self.ch)
        elif self.ch == "*":
            tok = Token(tokens["ASTERISK"], self.ch)
        elif self.ch == "<":
            tok = Token(tokens["LT"], self.ch)
        elif self.ch == ">":
            tok = Token(tokens["GT"], self.ch)
        elif self.ch == "if":
            tok = Token(tokens["COND_IF"], self.ch)
        elif self.ch == "else":
            tok = Token(tokens["COND_ELSE"], self.ch)
        elif self.ch == "true":
            tok = Token(tokens["BOOL_TRUE"], self.ch)
        elif self.ch == "false":
            tok = Token(tokens["BOOL_FALSE"], self.ch)
        elif self.ch == "return":
            tok = Token(tokens["RET"], self.ch)
        elif self.ch == None or self.ch == "":
            tok = Token(tokens["EOF"], "")
        elif self.is_letter(self.ch):
            tok = Token(None, self.read_identifier())
            tok.lookup_identifier()
            ps += ", T: " + tok.token_type + ", L: " + str(tok.literal)
            print(ps)
            return tok
        elif self.ch.isdigit():
            tok = Token(tokens["INT"], self.read_integer())
            ps += ", T: " + tok.token_type + ", L: " + str(tok.literal)
            print(ps)
            return tok
        else:
            tok = Token(tokens["ILLEGAL"], "ILLEGAL")
        
        ps += ", T: " + tok.token_type + ", L: " + str(tok.literal)
        print(ps)

        self.read_char()

        return tok