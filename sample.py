def generate_l_system_string(axiom, rules, n):
    current_string = axiom
    for _ in range(n):
        next_string = ''
        for char in current_string:
            if char in rules:
                next_string += rules[char]
            else:
                next_string += char
        current_string = next_string
    return current_string

# Define the L-system rules
axiom = 'A'
rules = {'A': 'AB', 'B': 'A'}

# Generate and print the L-system strings for each 'n' value

for n in range(6):  # n = 0 to 5
    l_system_string = generate_l_system_string(axiom, rules, n)
    print(f"n = {n} : S={l_system_string}")
