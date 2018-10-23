"""
Actions to be taken when grammar patterns are recognized.
"""

from parglare import get_collector

action = get_collector()

@action
def file(context, nodes):
    return nodes[:-1][0]

@action
def expressions(context, nodes):
    return nodes[0]

@action
def item(context, nodes):
    return nodes[0]

@action
def block(context, nodes):
    return nodes[1]
