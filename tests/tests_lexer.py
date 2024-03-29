import unittest
import lexer
import tokens

class TestLexer(unittest.TestCase):

    def test_next_token(self):        
        #input = "=+(){},;"

        input = """let five = 5; 
        let ten = 10; 
        let add = fn( x, y) { x + y; }; 
        let result = add( five, ten);

        !-/* 5; 
        
        5 < 10 > 5;

        if (5 < 10) { 
            return true; 
        } else { 
            return false; 
        }
        """
        print(input)
        tests = [
            tokens.Token(tokens.tokens["LET"], "let"),
            tokens.Token(tokens.tokens["IDENT"], "five"),
            tokens.Token(tokens.tokens["ASSIGN"], "="),
            tokens.Token(tokens.tokens["INT"], 5),
            tokens.Token(tokens.tokens["SEMICOLON"], ";"),
            tokens.Token(tokens.tokens["LET"], "let"),
            tokens.Token(tokens.tokens["IDENT"], "ten"),
            tokens.Token(tokens.tokens["ASSIGN"], "="),
            tokens.Token(tokens.tokens["INT"], 10),
            tokens.Token(tokens.tokens["SEMICOLON"], ";"),
            tokens.Token(tokens.tokens["LET"], "let"),
            tokens.Token(tokens.tokens["IDENT"], "add"),
            tokens.Token(tokens.tokens["ASSIGN"], "="),
            tokens.Token(tokens.tokens["FUNCTION"], "fn"),
            tokens.Token(tokens.tokens["LPAREN"], "("),
            tokens.Token(tokens.tokens["IDENT"], "x"),
            tokens.Token(tokens.tokens["COMMA"], ","),
            tokens.Token(tokens.tokens["IDENT"], "y"),
            tokens.Token(tokens.tokens["RPAREN"], ")"),
            tokens.Token(tokens.tokens["LBRACE"], "{"),
            tokens.Token(tokens.tokens["IDENT"], "x"),
            tokens.Token(tokens.tokens["PLUS"], "+"),
            tokens.Token(tokens.tokens["IDENT"], "y"),
            tokens.Token(tokens.tokens["SEMICOLON"], ";"),
            tokens.Token(tokens.tokens["RBRACE"], "}"),
            tokens.Token(tokens.tokens["SEMICOLON"], ";"),
            tokens.Token(tokens.tokens["LET"], "let"),
            tokens.Token(tokens.tokens["IDENT"], "result"),
            tokens.Token(tokens.tokens["ASSIGN"], "="),
            tokens.Token(tokens.tokens["IDENT"], "add"),
            tokens.Token(tokens.tokens["LPAREN"], "("),
            tokens.Token(tokens.tokens["IDENT"], "five"),
            tokens.Token(tokens.tokens["COMMA"], ","),
            tokens.Token(tokens.tokens["IDENT"], "ten"),
            tokens.Token(tokens.tokens["RPAREN"], ")"),
            tokens.Token(tokens.tokens["SEMICOLON"], ";"),

            tokens.Token(tokens.tokens["BANG"], "!"),
            tokens.Token(tokens.tokens["MINUS"], "-"),
            tokens.Token(tokens.tokens["SLASH"], "/"),
            tokens.Token(tokens.tokens["ASTERISK"], "*"),
            tokens.Token(tokens.tokens["INT"], 5),
            tokens.Token(tokens.tokens["SEMICOLON"], ";"),

            tokens.Token(tokens.tokens["INT"], 5),
            tokens.Token(tokens.tokens["LT"], "<"),
            tokens.Token(tokens.tokens["INT"], 10),
            tokens.Token(tokens.tokens["GT"], ">"),
            tokens.Token(tokens.tokens["INT"], 5),
            tokens.Token(tokens.tokens["SEMICOLON"], ";"),

            tokens.Token(tokens.tokens["COND_IF"], "if"),
            tokens.Token(tokens.tokens["LPAREN"], "("),
            tokens.Token(tokens.tokens["INT"], 5),
            tokens.Token(tokens.tokens["LT"], "<"),
            tokens.Token(tokens.tokens["INT"], 10),
            tokens.Token(tokens.tokens["RPAREN"], ")"),
            tokens.Token(tokens.tokens["LBRACE"], "{"),
            tokens.Token(tokens.tokens["RET"], "return"),
            tokens.Token(tokens.tokens["BOOL_TRUE"], "true"),
            tokens.Token(tokens.tokens["SEMICOLON"], ";"),
            tokens.Token(tokens.tokens["RBRACE"], "}"),
            tokens.Token(tokens.tokens["COND_ELSE"], "else"),
            tokens.Token(tokens.tokens["LBRACE"], "{"),
            tokens.Token(tokens.tokens["RET"], "return"),
            tokens.Token(tokens.tokens["BOOL_FALSE"], "false"),
            tokens.Token(tokens.tokens["SEMICOLON"], ";"),
            tokens.Token(tokens.tokens["RBRACE"], "}"),
        ]
        """
        if (5 < 10) { 
            return true; 
        } else { 
            return false; 
        }
        """
        lex = lexer.Lexer(input)

        for tok in tests:
            tkn = lex.next_token()

            self.assertEqual(tkn.token_type, tok.token_type)
            self.assertEqual(tkn.literal, tok.literal)