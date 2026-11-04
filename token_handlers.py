#used for operators, numbers, comments, and errors
tokens = []

def print_tokens():
    for (token_category, value) in tokens:
        print(f"{token_category}: {value}")