from node import Node

head1 = None                    # [], pusta lista
head1 = Node(3, None)          # [3]
head1 = Node(2, head1)          # [2, 3]
head1 = Node(4, head1)          # [4, 2, 3]

head2 = None                    # [], pusta lista
head2 = Node(7, None)          # [7]
head2 = Node(5, head2)          # [5, 7]
head2 = Node(8, head2)          # [8, 5, 7]

def merge(head1, head2):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    else:
        while True:
            if head1.next != None:
                head1.next = head2
                break
            else:
                head1 = head1.next
        return head1

def find_max(node):
    if node == None:
        raise ValueError("Lista pusta")
    else:
        maxNode == node
        while node:
            if node.data > maxNode.data:
                maxNode = node
        return maxNode
        

def find_min(node):
    if node == None:
        raise ValueError("Lista pusta")
    else:
        minNode == node
        while node:
            if node.data < minNode.data:
                minNode = node
        return minNode

head3 = merge(head1, head2)
head4 = merge(head2, head1)

print head3.next.next.next.__str__()
print head4.next.next.next.__str__()

minNode = find_min(head3)
maxNode = find_max(head3)

print "Min: " + minNode.__str__()
print "Max: " + maxNode.__str__()
        
