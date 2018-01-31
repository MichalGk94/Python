#!/usr/bin/python
from node import Node

def min_bst(top):
    if top is None:
        raise ValueError()
	return
    res = top.data
    lres = 100
    rres = 100
    if top.left != None:
	lres = min_bst(top.left)
    if top.right != None:
	rres = min_bst(top.right)
    if lres < res:
	res = lres
    if rres < res:
	res = rres
    return res

def max_bst(top):
    if top is None:
        raise ValueError()
	return
    res = top.data
    lres = 0
    rres = 0
    if top.left != None:
	lres = max_bst(top.left)
    if top.right != None:
	rres = max_bst(top.right)
    if lres > res:
	res = lres
    if rres > res:
	res = rres
    return res

root = Node(1)
root.left = Node(5)
root.right = Node(2)
root.left.left = Node(-6)
root.left.right = Node(11)
root.right.left = Node(0)
root.right.right = Node(8)

minV = min_bst(root)
maxV = max_bst(root)

print "Minimalna wartosc w drzewie: " + str(minV)
print "Maksymalna wartosc w drzewie: " + str(maxV)




