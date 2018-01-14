#!/usr/bin/python

def min_bst(top):
    if top is None:
        raise ValueError()
    elif top.left is None:
        top = top.left
    return top

def max_bst(top):
    if top is None:
        raise ValueError()
    elif top.right is None:
        top = top.right
    return top


