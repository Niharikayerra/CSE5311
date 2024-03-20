class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, max_nodes):
        self.max_nodes = max_nodes
        self.nodes = [None] * max_nodes
        self.head = None
        self.free_list = list(range(max_nodes))

    def get_free_node(self, data):
        if not self.free_list:
            print("Out of memory")
            return None
        index = self.free_list.pop(0)
        self.nodes[index] = Node(data)
        return index

    def release_node(self, index):
        self.nodes[index] = None
        self.free_list.append(index)

    def add(self, data):
        index = self.get_free_node(data)
        if index is None:
            return
        if self.head is None:
            self.head = index
        else:
            last = self.nodes[self.head]
            while last.next is not None:
                last = self.nodes[last.next]
            last.next = index

    def find(self, data):
        current = self.head
        while current is not None:
            if self.nodes[current].data == data:
                return True
            current = self.nodes[current].next
        return False

    def remove(self, data):
        if self.head is None:
            return
        if self.nodes[self.head].data == data:
            self.release_node(self.head)
            self.head = self.nodes[self.head].next
            return
        prev = self.head
        current = self.nodes[self.head].next
        while current is not None:
            if self.nodes[current].data == data:
                self.nodes[prev].next = self.nodes[current].next
                self.release_node(current)
                return
            prev = current
            current = self.nodes[current].next

    def show(self):
        current = self.head
        while current is not None:
            print(self.nodes[current].data, end=" -> ")
            current = self.nodes[current].next
        print("None")
# Example:
linked_list = SinglyLinkedList(10)

linked_list.add(4)
linked_list.add(9)
linked_list.add(6)

print("Linked list:")
linked_list.show()



linked_list.remove(9)
print("Linked list after deleting 9:")
linked_list.show()