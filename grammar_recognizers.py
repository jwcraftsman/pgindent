"""
Custom recognizers for grammar terminals.
"""

import re
from parglare import get_collector

recognizer = get_collector()

new_line_and_possible_indent_re = re.compile(r"\n *")

def match_new_line_and_possible_indent(input, pos):
    match = new_line_and_possible_indent_re.match(input, pos)
    if match is None:
        return None
    return input[pos:match.end()]

@recognizer
def align(context, input, pos):
   new_line_and_possible_indent = match_new_line_and_possible_indent(
       input, pos)
   if new_line_and_possible_indent is not None:
       new_indent = new_line_and_possible_indent[1:]
       if new_indent == context.extra[-1]:
           return new_line_and_possible_indent

@recognizer
def indent(context, input, pos):
    new_line_and_possible_indent = match_new_line_and_possible_indent(
        input, pos)
    if new_line_and_possible_indent is not None:
        new_indent = new_line_and_possible_indent[1:]
        if len(new_indent) > len(context.extra[-1]):
            return new_line_and_possible_indent

@recognizer
def unindent(context, input, pos):
    new_line_and_possible_indent = match_new_line_and_possible_indent(
        input, pos)
    if new_line_and_possible_indent is not None:
        new_indent = new_line_and_possible_indent[1:]
        if len(new_indent) < len(context.extra[-1]):
            if len(new_indent) <= len(context.extra[-1]):
                return ""
