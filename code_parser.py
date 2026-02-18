import ast

def parse_code_to_tree(code: str):
    """
    Parse Python code into an Abstract Syntax Tree (AST)
    and print it in a tree-like structure.
    """
    try:
        # Parse the code into an AST
        tree = ast.parse(code)

        # Pretty-print the AST with indentation
        print(ast.dump(tree, indent=4))
    except SyntaxError as e:
        print(f"Syntax error while parsing: {e}")

# Example usage:
example_code = """
a = 10 + 20
b = a * 2

def greet(name)
    print("Hello,", name)

for i in range(3):
    greet("User " + str(i))
"""

parse_code_to_tree(example_code)