import ast

code = """
import os
import sys
from datetime import datetime, timedelta
score = 100\nprint(score)
"""

class AIReviewer(ast.NodeVisitor):
    def __init__(self):
        self.defined = set()  # Things created (Imports and Store)
        self.used = set()     # Things read (Load)

    def visit_import(self, node):
        for alias in node.names:
            self.defined.add(alias.name)
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node):
        for alias in node.module:
            self.defined.add(alias.name)
        self.generic_visit(node)

# Variable 

    def visit_name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.defined.add(node.id)        
        elif isinstance(node.ctx, ast.Load):
            self.used.add(node.id)        
        self.generic_visit(node)

# 4. The Final Report
    def report_unused(self):
        # We subtract 'used' from 'defined'
        # We also ignore 'print' because it's a built-in function, not our variable
        unused = self.defined - self.used
        
        print("--- AI REVIEW REPORT ---")
        for item in unused:
            print(f"⚠️ UNUSED ITEM FOUND: {item}")

# Execution
tree = ast.parse(code)
reviewer = AIReviewer()
reviewer.visit(tree)
reviewer.report_unused()