#this is where the lexer logic will go
from token_handlers import tokens

keywords = ['bool', 'char', 'else', 'false', 'float', 'if', 'int', 'main', 'true', 'while', 'return', 'for']
operators = ['-', '!', '*', '/', '+', '<', '<=', '>', '>=', '==', '!=', '&&', '||', '=', '&', '|', '--', '++']
delimiters = ['{', '}', '(', ')', ';', ',', '[', ']']

def check_for_comment(file_string: str, position: int):
    # line comment: skip every character until the end of the line
    while position < len(file_string) and file_string[position] != '\n':
        position += 1
    return position

def check_for_block_comment(file_string: str, position: int):
    end = file_string.find('*/', position + 2)
    if end == -1:
        raise ValueError(f"Unterminated block comment at position {position}")
    return end + 2

def store_identifier(file_string:str, position: int):
    word = file_string[position]
    position += 1

    while position < len(file_string) and (file_string[position].isalnum() or file_string[position] == '_'):
        word += file_string[position]
        position += 1

    if word in keywords:
        tokens.append(('KEYWORD', word))
    else:
        tokens.append(('IDENTIFIER', word))
    return position

def store_num(file_string: str, position: int):
    start = position

    while position < len(file_string) and (
        file_string[position].isalnum() or
        file_string[position] in '._'
    ):
        position += 1

    number = file_string[start:position]

    if number.count('.') > 1 or not number.replace('.', '', 1).isdigit() or number.endswith('.'):
        raise ValueError(f"Invalid numeric literal '{number}' at position {start}")

    tokens.append(('LITERAL', number))
    return position
    
def store_operator(file_string: str, position: int):
    two_char = file_string[position:position + 2]

    if two_char in operators:
        tokens.append(('OPERATOR', two_char))
        return position + 2

    one_char = file_string[position]

    if one_char in operators:
        tokens.append(('OPERATOR', one_char))
        return position + 1

    raise ValueError(f"Invalid operator at position {position}")
        

def store_delimiter(file_string: str, position: int):
    delimiter = file_string[position]
    position += 1
    tokens.append(('DELIMITER', delimiter))
    return position

def start_lexical_analyzer(file_string: str):
    position = 0
    tokens.clear()

    while position < len(file_string):
        character = file_string[position]

        if character.isspace():
            position += 1
        elif character.isalpha() or character == '_':
            position = store_identifier(file_string, position)
        elif character.isdigit():
            position = store_num(file_string, position)
        elif file_string[position:position + 2] == '//':
            position = check_for_comment(file_string, position)
        elif file_string[position:position + 2] == '/*':
            position = check_for_block_comment(file_string, position)
        elif character in operators:
            position = store_operator(file_string, position)
        elif character in delimiters:
            position = store_delimiter(file_string, position)
        else:
            raise ValueError(
                f"Unexpected character {character!r} at position {position}"
            )

    return tokens
