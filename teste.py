import random

class Grammar:
    def __init__(self, variables, terminals, productions, start_symbol):
        self.variables = variables
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def get_productions(self, variable):
        return self.productions.get(variable, [])

class Derivation:
    def __init__(self, grammar):
        self.grammar = grammar
        self.seen_derivations = set()

    def generate_chain(self, symbol, mode='quick'):
        if symbol in self.grammar.terminals:
            return symbol
        
        # Get all productions for the given symbol
        productions = self.grammar.get_productions(symbol)
        if not productions:
            return ''
        
        # Choose a production randomly if mode is quick
        if mode == 'quick':
            production = random.choice(productions)
            derivation = self.apply_production(symbol, production)
            return derivation
        
        # Mode detailed: explore all derivations
        derivation = []
        for production in productions:
            result = self.apply_production(symbol, production)
            if result not in self.seen_derivations:
                self.seen_derivations.add(result)
                derivation.append(result)
        
        return derivation

    def apply_production(self, symbol, production):
        result = []
        for part in production.split():
            if part == 'epsilon':
                continue
            result.append(part)
        return ''.join(result)

def read_grammar_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
        
    variables = content[0].strip().split(':')[1].split(',')
    start_symbol = content[1].strip().split(':')[1].strip()
    terminals = content[2].strip().split(':')[1].split(',')
    
    productions = {}
    for line in content[4:]:
        if line.strip():
            left, right = line.split(':')
            left = left.strip()
            right = right.strip()
            if left not in productions:
                productions[left] = []
            productions[left].append(right)
    
    return Grammar(variables, terminals, productions, start_symbol)

def main():
    file_path = 'gramatica.txt'  # Path to the grammar file
    grammar = read_grammar_from_file(file_path)
    derivation = Derivation(grammar)

    while True:
        mode = input("Choose mode (quick/detailed): ").strip().lower()
        if mode not in ['quick', 'detailed']:
            print("Invalid mode! Please choose 'quick' or 'detailed'.")
            continue
        
        chain = derivation.generate_chain(grammar.start_symbol, mode)
        print(f"Generated chain: {chain}")

if __name__ == "__main__":
    main()
