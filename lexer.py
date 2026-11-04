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

    while position < len(file_string) and file_string[position].isalnum():
        word += file_string[position]
        position += 1

    if word in keywords:
        tokens.append(('KEYWORD', word))
    else:
        tokens.append(('IDENTIFIER', word))
    return position

def store_num(file_string:str, position: int):
    number_as_string = file_string[position]
    position += 1

    while position < len(file_string) and (file_string[position].isdigit() or file_string[position] == '.'):
        #checking for decimals
        if file_string[position] != '.' or  number_as_string.count('.') == 0:
            number_as_string += file_string[position]
            position += 1
        else:
            raise Exception("Invalid number, can only have one period")

    tokens.append(('LITERAL', number_as_string))
    return position
    
def store_operator(file_string: str, position: int):
    operator = file_string[position]
    position += 1

    while position < len(file_string) and (file_string[position] in operators):
        operator += file_string[position]
        if len(operator) > 2:
            raise Exception("operators can't be more than 2 characters")
        position += 1

    if operator in operators:
        tokens.append(('OPERATOR', operator))
    else:
        raise Exception("This operator does not exist")
    return position
        

def store_delimiter(file_string: str, position: int):
    delimiter = file_string[position]
    position += 1
    tokens.append(('DELIMITER', delimiter))
    return position



def start_lexical_analyzer(file_string: str):
    position = 0

    while position < len(file_string):
        character = file_string[position]

        if character.isspace():
            position += 1
        elif character.isalpha():
            position = store_identifier(file_string, position)
        elif character.isdigit():
            position = store_num(file_string, position)
        elif character == '/' and file_string[position:position + 2] == '//':
            position = check_for_comment(file_string, position)
        elif character in operators:
            position = store_operator(file_string, position)
        elif character in delimiters:
            position = store_delimiter(file_string, position)
        else:
            raise Exception(f"Unexpected character {character!r} at position {position}")
