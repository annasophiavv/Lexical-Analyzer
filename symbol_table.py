#where the symbol table lives and its operations

from token_handlers import tokens

symbol_table = {}

def build_symbol_table(tokens):
    symbol_table.clear()

    for token_type, lexeme in tokens:
        if token_type == "IDENTIFIER":
            if lexeme not in symbol_table:
                symbol_table[lexeme] = {
                    "Kind": "IDENTIFIER",
                    "Type": None,
                    "Line Declared": None,
                    "Count": 1
                }
            else:
                symbol_table[lexeme]["Count"] += 1

    return symbol_table


def print_symbol_table():
    print("\nSYMBOL TABLE")
    print("-" * 85)
    print(f"{'NAME':<15} {'KIND':<15} {'TYPE':<15} {'LINE DECLARED':<20} {'COUNT'}")
    print("-" * 85)

    for name, info in symbol_table.items():
        print(
            f"{name:<15}"
            f"{info['Kind']:<15}"
            f"{info['Type'] or '':<15}"
            f"{info['Line Declared'] or '':<20}"
            f"{info['Count']}"
        )


build_symbol_table(tokens)
print_symbol_table()
