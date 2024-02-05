# TOKENS

tokens = dict(
    ILLEGAL = "ILLEGAL",
    EOF = "EOF",

    # Identifiers + literals
    IDENT = "IDENT", # add, x, y
    INT = "INT",

    # Operators
    ASSIGN = "=",
    PLUS = "+",
    BANG = "!",
    MINUS = "-",
    SLASH = "/",
    ASTERISK = "*",
    LT = "<",
    GT = ">",

    # Delimiters
    COMMA = ",",
    SEMICOLON = ";",

    LPAREN = "(",
    RPAREN = ")",
    LBRACE = "{",
    RBRACE = "}",

    # Keywords
    FUNCTION = "FUNCTION",
    LET = "LET",
    COND_IF = "IF",
    COND_ELSE = "ELSE",
    BOOL_TRUE = "TRUE",
    BOOL_FALSE = "FALSE",
    RET = "RETURN",
)

keyword_map = {
    "fn": "FUNCTION",
    "let": "LET",
    "if" : "COND_IF",
    "else" : "COND_ELSE", 
    "true" : "BOOL_TRUE",
    "false" : "BOOL_FALSE",
    "return" : "RET",
}

class Token:
    token_type = None
    literal = None

    def __init__(self, token_type, literal):
        self.token_type = token_type
        self.literal = literal
    
    def lookup_identifier(self):
        if self.literal in keyword_map:
            self.token_type = tokens[keyword_map[self.literal]]
        else:
            self.token_type = tokens["IDENT"]