#!/usr/bin/env python3

"""
Parse input files and print the AST.
"""

import sys
import parglare.parser
from parglare import Parser, Grammar

class Context(parglare.parser.Context):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.extra = ['']

grammar = Grammar.from_file('grammar.pg')
parser = Parser(grammar)
results = parser.parse_file(sys.argv[1], context=Context())
print(results)
