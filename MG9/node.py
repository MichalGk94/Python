class Node:
    """Klasa reprezentujaca wezel drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
	self.visited = False

    def __str__(self):
        return str(self.data)
