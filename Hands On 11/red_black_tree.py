class Node:
    def __init__(self, value, color='RED'):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.NULL_NODE = Node(0)
        self.root = self.NULL_NODE
    def insert(self, value):
        new_node = Node(value)
        new_node.parent = None
        new_node.left_child = self.NULL_NODE
        new_node.right_child = self.NULL_NODE
        new_node.color = 'RED'
        parent = None
        current = self.root
        while current != self.NULL_NODE:
            parent = current
            if new_node.value < current.value:
                current = current.left_child
            else:
                current = current.right_child
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left_child = new_node
        else:
            parent.right_child = new_node
        if new_node.parent is None:
            new_node.color = 'BLACK'
            return
        if new_node.parent.parent is None:
            return
        self.fix_insert(new_node)

    def fix_insert(self, k):
        while k != self.root and k.parent.color == 'RED':
            if k.parent == k.parent.parent.right_child:
                u = k.parent.parent.left_child
                if u.color == 'RED':
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left_child:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right_child
                if u.color == 'RED':
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.right_child:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'BLACK'
   
    def left_rotate(self, x):
        y = x.right_child
        x.right_child = y.left_child
        if y.left_child != self.NULL_NODE:
            y.left_child.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left_child:
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.left_child = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left_child
        x.left_child = y.right_child
        if y.right_child != self.NULL_NODE:
            y.right_child.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right_child:
            x.parent.right_child = y
        else:
            x.parent.left_child = y
        y.right_child = x
        x.parent = y

    def delete(self, value):
        self._delete_node(self.search(value))
    def _delete_node(self, node):
        if node == self.NULL_NODE:
            return
        y = node
        original_color = y.color
        if node.left_child == self.NULL_NODE:
            x = node.right_child
            self._transplant(node, node.right_child)
        elif node.right_child == self.NULL_NODE:
            x = node.left_child
            self._transplant(node, node.left_child)
        else:
            y = self.minimum(node.right_child)
            original_color = y.color
            x = y.right_child
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right_child)
                y.right_child = node.right_child
                y.right_child.parent = y
            self._transplant(node, y)
            y.left_child = node.left_child
            y.left_child.parent = y
            y.color = node.color
        if original_color == 'BLACK':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left_child:
                s = x.parent.right_child
                if s.color == 'RED':
                    s.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(x.parent)
                    s = x.parent.right_child
                if s.left_child.color == 'BLACK' and s.right_child.color == 'BLACK':
                    s.color = 'RED'
                    x = x.parent
                else:
                    if s.right_child.color == 'BLACK':
                        s.left_child.color = 'BLACK'
                        s.color = 'RED'
                        self.right_rotate(s)
                        s = x.parent.right_child
                    s.color = x.parent.color
                    x.parent.color = 'BLACK'
                    s.right_child.color = 'BLACK'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left_child
                if s.color == 'RED':
                    s.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.right_rotate(x.parent)
                    s = x.parent.left_child
                if s.right_child.color == 'BLACK' and s.left_child.color == 'BLACK':
                    s.color = 'RED'
                    x = x.parent
                else:
                    if s.left_child.color == 'BLACK':
                        s.right_child.color = 'BLACK'
                        s.color = 'RED'
                        self.left_rotate(s)
                        s = x.parent.left_child
                    s.color = x.parent.color
                    x.parent.color = 'BLACK'
                    s.left_child.color = 'BLACK'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'BLACK'

    def minimum(self, node):
        while node.left_child != self.NULL_NODE:
            node = node.left_child
        return node
    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left_child:
            u.parent.left_child = v
        else:
            u.parent.right_child = v
        v.parent = u.parent

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node == self.NULL_NODE or value == node.value:
            return node
        if value < node.value:
            return self._search(node.left_child, value)
        return self._search(node.right_child, value)

    def inorder_traversal(self, node):
        if node != self.NULL_NODE:
            self.inorder_traversal(node.left_child)
            print(node.value, end=" ")
            self.inorder_traversal(node.right_child)

    def display(self):
        self._display(self.root)

    def _display(self, node, level=0, prefix="Root:"):
        if node != self.NULL_NODE:
            print("   " * level + prefix, node.value, node.color)
            self._display(node.left_child, level + 1, "L:")
            self._display(node.right_child, level + 1, "R:")


# Example usage:
if __name__ == "__main__":
    rb_tree = RedBlackTree()

    # Insertion
    values_to_insert = [18, 4, 7, 20, 9, 26, 31, 13]
    for value in values_to_insert:
        rb_tree.insert(value)
    print("Red-Black Tree after insertion:")
    rb_tree.display()

    # Search
    search_values = [7, 11, 22, 9, 26, 200]
    for value in search_values:
        if rb_tree.search(value) != rb_tree.NULL_NODE:
            print(f"{value} is found in the tree.")
        else:
            print(f"{value} is not found in the tree.")

    # Deletion
    values_to_delete = [4, 9, 31]
    for value in values_to_delete:
        rb_tree.delete(value)
    print("\nRed-Black Tree after deletion:")
    rb_tree.display()
