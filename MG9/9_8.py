from nodeT import Node

def traverse_preorder(top):
    if top is None:
        raise ValueError("Puste drzewo!")
    traverse_preorder(top.left, visit)
    traverse_preorder(top.right, visit)

def bst_max(top):
    if top is None:
        raise ValueError("Puste drzewo!")
    else
        minNode = top
        traverse_preorder(top)
        


def bst_min(top): pass

