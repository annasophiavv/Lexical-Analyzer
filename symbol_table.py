#where the symbol table lives and its operations

symbol_table = {}

def build_symbol_table(tokens):
    symbol_table.clear()

    for token_type, lexeme in tokens:
        if token_type == "IDENTIFIER":
            if lexeme not in symbol_table:
                symbol_table[lexeme] = {
                    "Kind": "IDENTIFIER",
                    "Count": 1
                }
            else:
                symbol_table[lexeme]["Count"] += 1

    return symbol_table


def print_symbol_table():
    print("\nSYMBOL TABLE")
    print("-" * 45)
    print(f"{'NAME':<20} {'KIND':<15} {'COUNT'}")
    print("-" * 45)

    for name, info in symbol_table.items():
        print(
            f"{name:<20} "
            f"{info['Kind']:<15} "
            f"{info['Count']}"
        )
