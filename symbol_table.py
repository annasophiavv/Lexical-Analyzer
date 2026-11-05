#where the symbol table lives and its operations
import re

symbol_table = {}


def build_symbol_table(tokens, file_string):
    symbol_table.clear()

    declarations = {}

    # Find variable declarations and their line numbers.
    for line_number, line in enumerate(
        file_string.splitlines(), start=1
    ):
        # Remove comments.
        line = re.sub(r'//.*', '', line)
        line = re.sub(r'/\*.*?\*/', '', line)

        # Identify variable declarations.
        pattern = r'\b(int|float|char|bool)\s+([A-Za-z_]\w*)'

        for match in re.finditer(pattern, line):
            variable_type = match.group(1)
            variable_name = match.group(2)

            declarations[variable_name] = {
                "Type": variable_type,
                "Line Declared": line_number
            }

    # Count each identifier.
    for token_type, lexeme in tokens:
        if token_type == "IDENTIFIER":

            if lexeme not in symbol_table:
                symbol_table[lexeme] = {
                    "Kind": "IDENTIFIER",
                    "Type": declarations.get(
                        lexeme, {}
                    ).get("Type"),
                    "Line Declared": declarations.get(
                        lexeme, {}
                    ).get("Line Declared"),
                    "Count": 1
                }

            else:
                symbol_table[lexeme]["Count"] += 1

    return symbol_table


def print_symbol_table():
    print("\nSYMBOL TABLE")
    print("-" * 85)

    print(
        f"{'NAME':<15} {'KIND':<15} {'TYPE':<15} "
        f"{'LINE DECLARED':<20} {'COUNT'}"
    )

    print("-" * 85)

    for name, info in symbol_table.items():
        print(
            f"{name:<15}"
            f"{info['Kind']:<15}"
            f"{info['Type'] or '':<15}"
            f"{info['Line Declared'] or '':<20}"
            f"{info['Count']}"
        )
