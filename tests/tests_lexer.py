import unittest
import lexer
import tokens

class TestLexer(unittest.TestCase):

    def test_next_token(self):
        tests = [
             tokens.Token(tokens.tokens["ASSIGN"], "="),
             tokens.Token(tokens.tokens["PLUS"], "+"),
             tokens.Token(tokens.tokens["LPAREN"], "("),
             tokens.Token(tokens.tokens["RPAREN"], ")"),
             tokens.Token(tokens.tokens["LBRACE"], "{"),
             tokens.Token(tokens.tokens["RBRACE"], "}"),
             tokens.Token(tokens.tokens["COMMA"], ","),
             tokens.Token(tokens.tokens["SEMICOLON"], ";"),
             tokens.Token(tokens.tokens["EOF"], "")
        ]
        
        lex = lexer.Lexer("=+(){},;")

        for tok in tests:
            tkn = lex.next_token()

            self.assertEqual(tkn.token_type, tok.token_type)
            self.assertEqual(tkn.literal, tok.literal)