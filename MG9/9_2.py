#!/usr/bin/python

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def merge(node1, node2):
    w = node1
    if w.next is not None:
         w = w.next
    w.next = node2
    return node1

