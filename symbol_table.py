#where the symbol table lives and its operations

symbol_table = {}

def add_symbol(name, kind, data_type, line_declared, users):
    symbol_table[name] = {
        "Kind": kind,
        "Type": data_type,
        "Line Declared": line_declared,
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
print(f"{'Name':<12} {'Kind':<12} {'Type':<8} {'Line Declared':<15} {'Users':<6}")
print("-" * 60)

for name, info in symbol_table.items():
    print(f"{name:<12} {info['Kind']:<12} {info['Type']:<8} "
          f"{info['Line Declared']:<15} {info['Users']:<6}")
