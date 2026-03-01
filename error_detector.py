import ast

code = """
import os
import sys
from math import sqrt, pow

unused_variable = 50
used_variable = 10

def BadFunctionName():
    x = 5
    return x

def very_long_function():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t = 20
    u = 21
    v = 22
    w = 23
    x = 24
    y = 25
    z = 26
    aa = 27
    bb = 28
    cc = 29
    dd = 30
    ee = 31
    ff = 32
    gg = 33
    hh = 34
    ii = 35
    jj = 36
    kk = 37
    ll = 38
    mm = 39
    nn = 40
    oo = 41
    return a

class myclass:
    pass

print(used_variable)
"""

class AIReviewer(ast.NodeVisitor):
    def __init__(self):
        self.defined = set()  # Things created (Imports and Store)
        self.used = set()     # Things read (Load)
        self.score = 100

    def visit_Import(self, node):
        for alias in node.names:
            print(alias)
            print(alias.name)
        self.defined.add(alias.name)
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.defined.add(alias.name)
        self.generic_visit(node)

    def  visit_FunctionDef(self,node):
      if isinstance(node, ast.FunctionDef):

        if hasattr(node,"end_lineno"):
            length = node.end_lineno - node.lineno + 1

            if length > 40:
                print(f"Line {node.lineno}: '{node.name}'Function is too long ({length} lines).")
                self.score-=10
                self.generic_visit(node)
                 
             

# Variable 

    def visit_Name(self, node):
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

#In this file.now have to add the infinite loop logic and all the descriptions with the unused