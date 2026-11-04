#this will be the entry point of the program.
#reads a file and calls functions in other files.
import sys
from lexer import start_lexical_analyzer
from token_handlers import print_tokens
from symbol_table import build_symbol_table, print_symbol_table

def read_file():
    filename = sys.argv[1] #example command: python3 main.py sample.clite. filename will equal sample.clite

    #open file with read only permissions, source is a string with the file's content
    with open(filename, "r") as file:
        source = file.read()
    return source

def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: python main.py <filename>")
            return

        source = read_file()
        tokens = start_lexical_analyzer(source)

        print_tokens()

        build_symbol_table(tokens)
        print_symbol_table()

        print("\nLexical analysis completed successfully.")

    except (OSError, ValueError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()

