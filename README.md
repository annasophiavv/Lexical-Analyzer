# Lexical-Analyzer

A small lexer for a C-like language called **Clite**. It reads a `.clite` file and
breaks it into tokens.

## How it works

`main.py` reads the file, then calls `start_lexical_analyzer` in `lexer.py`. The lexer
walks the source one character at a time and decides what to do with each one:

- `store_identifier` — keywords and variable names
- `store_num` — integer and decimal literals
- `store_operator` / `store_delimiter` — symbols like `==`, `+`, `{`, `;`
- `check_for_comment` — skips `//` and `/* ... */` comments

Tokens are kept in a list in `token_handlers.py` and printed with `print_tokens()`.
`symbol_table.py` then scans the tokens to record each variable's type, line, and count.

Run it with `python3 main.py sample.clite` and test it with `python3 -m unittest`.
