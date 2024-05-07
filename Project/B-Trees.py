import time
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.values = []
        self.children = []

    def split_child(self, index, child_node):
        degree = BTree.degree
        new_child = Node(is_leaf=child_node.is_leaf)
        self.children.insert(index + 1, new_child)
        self.values.insert(index, child_node.values[degree - 1])
        new_child.values = child_node.values[degree:]
        child_node.values = child_node.values[:degree - 1]
        if not child_node.is_leaf:
            new_child.children = child_node.children[degree:]
            child_node.children = child_node.children[:degree]

    def insert_non_full(self, value):
        index = len(self.values) - 1
        if self.is_leaf:
            self.values.append(None)
            while index >= 0 and value < self.values[index]:
                self.values[index + 1] = self.values[index]
                index -= 1
            self.values[index + 1] = value
        else:
            while index >= 0 and value < self.values[index]:
                index -= 1
            index += 1
            if len(self.children[index].values) == (2 * BTree.degree) - 1:
                self.split_child(index, self.children[index])
                if value > self.values[index]:
                    index += 1
            self.children[index].insert_non_full(value)

    def find_value(self, value):
        index = 0
        while index < len(self.values) and value > self.values[index]:
            index += 1
        return index

    def remove_from_non_leaf(self, index):
        value = self.values[index]
        if len(self.children[index].values) >= BTree.degree:
            pred = self.children[index].get_max()
            self.values[index] = pred
            self.children[index].delete(pred)
        elif len(self.children[index + 1].values) >= BTree.degree:
            succ = self.children[index + 1].get_min()
            self.values[index] = succ
            self.children[index + 1].delete(succ)
        else:
            self.merge_children(index)
            self.children[index].delete(value)

    def remove_from_leaf(self, index):
        self.values.pop(index)

    def get_min(self):
        if self.is_leaf:
            return self.values[0]
        return self.children[0].get_min()

    def get_max(self):
        if self.is_leaf:
            return self.values[-1]
        return self.children[-1].get_max()

    def merge_children(self, index):
        child = self.children[index]
        sibling = self.children[index + 1]
        child.values.append(self.values[index])
        child.values.extend(sibling.values)
        if not child.is_leaf:
            child.children.extend(sibling.children)
        self.values.pop(index)
        self.children.pop(index + 1)

    def borrow_from_prev(self, index):
        child = self.children[index]
        sibling = self.children[index - 1]
        child.values.insert(0, self.values[index - 1])
        if not child.is_leaf:
            child.children.insert(0, sibling.children.pop())
        self.values[index - 1] = sibling.values.pop()

    def borrow_from_next(self, index):
        child = self.children[index]
        sibling = self.children[index + 1]
        child.values.append(self.values[index])
        if not child.is_leaf:
            child.children.append(sibling.children.pop(0))
        self.values[index] = sibling.values.pop(0)

    def fill_child(self, index):
        if index != 0 and len(self.children[index - 1].values) >= BTree.degree:
            self.borrow_from_prev(index)
        elif index != len(self.values) and len(self.children[index + 1].values) >= BTree.degree:
            self.borrow_from_next(index)
        else:
            if index != len(self.values):
                self.merge_children(index)
            else:
                self.merge_children(index - 1)

    def search(self, value):
        index = self.find_value(value)
        if index < len(self.values) and self.values[index] == value:
            return True
        if self.is_leaf:
            return False
        return self.children[index].search(value)
    
    def delete(self, value):
        index = self.find_value(value)
        if index < len(self.values) and self.values[index] == value:
            if self.is_leaf:
                self.remove_from_leaf(index)
            else:
                self.remove_from_non_leaf(index)
        else:
            if self.is_leaf:
                print("Value not found")
                return
            flag = index == len(self.values)
            if len(self.children[index].values) < BTree.degree:
                self.fill_child(index)
            if flag and index > len(self.values):
                self.children[index - 1].delete(value)
            else:
                self.children[index].delete(value)

class BTree:
    def __init__(self, degree):
        self.root = Node(is_leaf=True)
        BTree.degree = degree

    def insert(self, value):
        root = self.root
        if len(root.values) == (2 * BTree.degree) - 1:
            new_root = Node(is_leaf=False)
            new_root.children.append(self.root)
            new_root.split_child(0, self.root)
            self.root = new_root
        self.root.insert_non_full(value)

    def search(self, value):
        return self.root.search(value)

    def delete(self, value):
        if not self.search(value):
            print("Value not found")
            return
        self.root.delete(value)
        if len(self.root.values) == 0:
            if len(self.root.children) > 0:
                self.root = self.root.children[0]
            else:
                self.root = Node(is_leaf=True)

class BenchmarkBTree:
    def __init__(self, degree):
        self.btree = BTree(degree)

    def generate_random_data(self, size):
        return [random.randint(1, 1000000) for _ in range(size)]

    def benchmark_deletion(self, data):
        start_time = time.time()
        for value in data:
            self.btree.delete(value)
        end_time = time.time()
        return end_time - start_time

    def benchmark_insertion(self, data):
        start_time = time.time()
        for value in data:
            self.btree.insert(value)
        end_time = time.time()
        return end_time - start_time

    def benchmark_search(self, data):
        start_time = time.time()
        for value in data:
            self.btree.search(value)
        end_time = time.time()
        return end_time - start_time

    def run_benchmarks(self, data_sizes):
        insertion_times = []
        search_times = []
        deletion_times = []

        for size in data_sizes:
            data = self.generate_random_data(size)

            search_time = self.benchmark_search(data)
            search_times.append(search_time)

            deletion_time = self.benchmark_deletion(data)
            deletion_times.append(deletion_time)

            insertion_time = self.benchmark_insertion(data)
            insertion_times.append(insertion_time)



        return insertion_times, search_times, deletion_times

def plot_results(data_sizes, insertion_times, search_times, deletion_times):
    plt.plot(data_sizes, insertion_times, label='Insertion')
    plt.plot(data_sizes, search_times, label='Search')
    plt.plot(data_sizes, deletion_times, label='Deletion')
    plt.xlabel('Data Size')
    plt.ylabel('Time (seconds)')
    plt.title('B-tree Benchmark Results')
    plt.legend()
    plt.show()

# Example usage:
custom_btree_benchmark = BenchmarkCustomBTree(3)
data_sizes = [100, 2000, 5000, 10000, 50000, 80000, 100000]  
insertion_times, search_times, deletion_times = custom_btree_benchmark.run_benchmarks(data_sizes)
plot_results(data_sizes, insertion_times, search_times, deletion_times)

