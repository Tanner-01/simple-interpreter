"""
let five = 5; 
let ten = 10; 

let add = fn( x, y) {
    x + y; 
}; 

let result = add( five, ten);

"""

# TOKENS 

ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers + literals
IDENT = "IDENT" # add, x, y
INT = "INT"

# Operators
ASSIGN = "="
PLUS = "+"

# Delimiters
COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"

class Token:
    token_type = ""
    literal = ""

    def __init__(self, token_type, literal):
        self.token_type = token_type
        self.literal = literal
    
