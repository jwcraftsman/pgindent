"""
Side-effect actions to be taken when grammar patterns are recognized.
"""

from parglare import get_collector

side_action = get_collector()

@side_action
def indent(context, node):
    context.extra.append(node[1:])

@side_action
def unindent(context, node):
    context.extra.pop()
