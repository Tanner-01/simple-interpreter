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

    # Delimiters
    COMMA = ",",
    SEMICOLON = ";",

    LPAREN = "(",
    RPAREN = ")",
    LBRACE = "{",
    RBRACE = "}",

    # Keywords
    FUNCTION = "FUNCTION",
    LET = "LET"
)

keyword_map = dict(
    fn = "FUNCTION",
    let = "LET"
)

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