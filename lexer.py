"""
l et five = 5; 
let ten = 10; 

let add = fn( x, y) {
    x + y; 
}; 

let result = add( five, ten);

"""

class Lexer:
    input = None
    input_length = None
    position = None
    read_position = None
    ch = None

    def __init__(self, source):
        self.input = source
        self.input_length = len(input)
        self.position = 0
        self.read_position = 1

    def read_char(self):
        if self.read_position >= self.input_length:
            self.ch = None
        else:
            self.ch = self.input[self.read_position]
        
        self.position = self.read_position
        self.read_position += 1