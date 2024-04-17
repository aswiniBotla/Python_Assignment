class LSystem:
    def __init__(self, variables, axiom, rules):
        self.variables = variables
        self.axiom = axiom
        self.rules = rules

    def produce(self, n):
        current_string = self.axiom
        for _ in range(n):
            next_string = ''
            for char in current_string:
                if char in self.variables:
                    next_string += self.rules[char]
                else:
                    next_string += char
            current_string = next_string
        return current_string

# Testing the code with Cantor fractal L-system
variables = {'A', 'B'}
axiom = 'A'
rules = {'A': 'ABA', 'B': 'BBB'}

cantor_fractal = LSystem(variables, axiom, rules)
result = cantor_fractal.produce(3)
print("L-system string:", result)
