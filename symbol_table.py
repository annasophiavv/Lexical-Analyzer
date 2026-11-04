#where the symbol table lives and its operations
symbol_table = {}

def add_symbol(name, kind, data_type, line, users):
    symbol_table[name] = {
        "Kind": kind,
        "Type": data_type,
        "Line": line,
        "Users": users
    }


# Add symbols to the symbol table
add_symbol("age", "IDENTIFIER", "int", 2, 2)
add_symbol("grade", "IDENTIFIER", "float", 3, 3)
add_symbol("total", "IDENTIFIER", "int", 4, 5)
add_symbol("Calculate", "IDENTIFIER", "int", 14, 1)
add_symbol("score", "IDENTIFIER", "int", 14, 2)
add_symbol("bonus", "IDENTIFIER", "int", 15, 2)


# Display the symbol table
print("Name        Kind         Type    Line   Users")
print("-" * 55)

for name, info in symbol_table.items():
    print(f"{name:<12} {info['Kind']:<12} {info['Type']:<7} "
          f"{info['Line']:<6} {info['Users']}")
