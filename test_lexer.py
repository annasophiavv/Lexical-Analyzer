#used to tests

import unittest
from lexer import start_lexical_analyzer


class TestLexer(unittest.TestCase):

    def scan(self, source):
        return start_lexical_analyzer(source).copy()

    def test_keywords(self):
        result = self.scan("int float bool char if else while for return true false main")
        self.assertTrue(all(t[0] == "KEYWORD" for t in result))

    def test_identifiers(self):
        result = self.scan("count total_count _value")
        self.assertEqual(result, [
            ("IDENTIFIER", "count"),
            ("IDENTIFIER", "total_count"),
            ("IDENTIFIER", "_value")
        ])

    def test_integer_literals(self):
        result = self.scan("10 0 123")
        self.assertEqual(result, [
            ("LITERAL", "10"),
            ("LITERAL", "0"),
            ("LITERAL", "123")
        ])

    def test_decimal_literals(self):
        result = self.scan("3.14 10.50")
        self.assertEqual(result, [
            ("LITERAL", "3.14"),
            ("LITERAL", "10.50")
        ])

    def test_arithmetic_operators(self):
        result = self.scan("+ - * / ++ --")
        self.assertEqual([t[1] for t in result],
                         ["+", "-", "*", "/", "++", "--"])

    def test_comparison_operators(self):
        result = self.scan("< <= > >= == !=")
        self.assertEqual([t[1] for t in result],
                         ["<", "<=", ">", ">=", "==", "!="])

    def test_logical_operators(self):
        result = self.scan("&& || !")
        self.assertEqual([t[1] for t in result],
                         ["&&", "||", "!"])

    def test_delimiters(self):
        result = self.scan("{ } ( ) ; , [ ]")
        self.assertTrue(all(t[0] == "DELIMITER" for t in result))

    def test_line_comments(self):
        result = self.scan("int x; // comment\nfloat y;")
        self.assertNotIn(("IDENTIFIER", "comment"), result)
        self.assertIn(("KEYWORD", "float"), result)

    def test_block_comments(self):
        result = self.scan("int x; /* block comment */ float y;")
        self.assertNotIn(("IDENTIFIER", "block"), result)
        self.assertIn(("KEYWORD", "float"), result)

    def test_invalid_character(self):
        with self.assertRaises(ValueError):
            self.scan("int x = @;")

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            self.scan("int x = 12.3.4;")

    def test_unterminated_comment(self):
        with self.assertRaises(ValueError):
            self.scan("int x; /* unfinished comment")

    def test_operator_separation_and_reset(self):
        result = self.scan("a+-b")
        self.assertEqual(result, [
            ("IDENTIFIER", "a"),
            ("OPERATOR", "+"),
            ("OPERATOR", "-"),
            ("IDENTIFIER", "b")
        ])

        second_result = self.scan("int x;")
        self.assertEqual(second_result, [
            ("KEYWORD", "int"),
            ("IDENTIFIER", "x"),
            ("DELIMITER", ";")
        ])


if __name__ == "__main__":
    unittest.main()
