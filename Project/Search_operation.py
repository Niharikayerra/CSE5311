import time
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []

    def search(self, key):
        index = 0
        while index < len(self.keys) and key > self.keys[index]:
            index += 1
        if index < len(self.keys) and key == self.keys[index]:
            return True
        if self.is_leaf:
            return False
        return self.children[index].search(key)

class Tree:
    def __init__(self, t):
        self.root = Node(is_leaf=True)
        Tree.degree = t

class BenchmarkTree:
    def __init__(self, t):
        self.b_tree = Tree(t)

    def generate_random_data(self, size):
        return [random.randint(1, 1000000) for _ in range(size)]

    def benchmark_search(self, data):
        start = time.time()
        for key in data:
            self.b_tree.root.search(key)
        end = time.time()
        return end - start

    def analyze_search(self, data_sizes):
        best_times = []
        average_times = []
        worst_times = []

        for size in data_sizes:
            data = self.generate_random_data(size)

            # Best case: Key is at the root
            self.b_tree = Tree(3)
            search_time = self.benchmark_search([data[0]])
            best_times.append(search_time)

            # Worst case: Key is not present in the tree
            self.b_tree = Tree(3)
            search_time = self.benchmark_search([size + 1])  # Key guaranteed to be greater than any in data
            worst_times.append(search_time)

            # Average case: Randomly generated keys
            self.b_tree = Tree(3)
            search_time = self.benchmark_search([random.choice(data)])
            average_times.append(search_time)

        return best_times, average_times, worst_times

def plot_analysis(data_sizes, best_times, average_times, worst_times):
    plt.plot(data_sizes, best_times, label='Best Case', linestyle='-', marker='o', color='green')
    plt.plot(data_sizes, average_times, label='Average Case', linestyle='--', marker='s', color='blue')
    plt.plot(data_sizes, worst_times, label='Worst Case', linestyle='-.', marker='^', color='red')
    plt.xlabel('Data Size')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Analysis of Search Operations')
    plt.legend()
    plt.show()

# Example usage:
benchmark_tree = BenchmarkTree(3)
data_sizes = [10, 1000, 10000, 50000, 100000]

best_times, average_times, worst_times = benchmark_tree.analyze_search(data_sizes)

plot_analysis(data_sizes, best_times, average_times, worst_times)
