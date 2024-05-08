
import random
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

    def split_child(self, idx, child, t):
        new_child = TreeNode(leaf=child.leaf)
        self.children.insert(idx + 1, new_child)
        self.keys.insert(idx, child.keys[t - 1])
        new_child.keys = child.keys[t:]
        child.keys = child.keys[:t - 1]
        if not child.leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]

    def insert_non_full(self, key, t):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == (2 * t) - 1:
                self.split_child(i, self.children[i], t)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key, t)

    def find_key(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        return i

class Tree:
    def __init__(self, t):
        self.root = TreeNode(leaf=True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = TreeNode(leaf=False)
            new_root.children.append(self.root)
            new_root.split_child(0, self.root, self.t)
            self.root = new_root
        self.root.insert_non_full(key, self.t)

class BenchmarkTree:
    def __init__(self, t):
        self.tree = Tree(t)

    def generate_random_data(self, size):
        return [random.randint(1, 1000000) for _ in range(size)]

    def benchmark_insertion(self, data):
        start_time = time.time()
        for key in data:
            self.tree.insert(key)
        end_time = time.time()
        return end_time - start_time

    def analyze_insertion(self, data_sizes):
        best_times = []
        average_times = []
        worst_times = []

        for size in data_sizes:
            data = self.generate_random_data(size)

            # Best case: Already balanced tree
            self.tree = Tree(3)
            insertion_time = self.benchmark_insertion(data)
            best_times.append(insertion_time)

            # Worst case: Tree needs rebalancing after each insertion
            self.tree = Tree(3)
            self.tree.insert(data[0])
            insertion_time = self.benchmark_insertion(data[1:])
            worst_times.append(insertion_time)

            # Average case: Uniformly distributed keys
            insertion_time = self.benchmark_insertion(data)
            average_times.append(insertion_time)

        return best_times, average_times, worst_times

def plot_analysis(data_sizes, best_times, average_times, worst_times):
    plt.plot(data_sizes, best_times, label='Best Case',  color='blue')
    plt.plot(data_sizes, average_times, label='Average Case',  color='orange')
    plt.plot(data_sizes, worst_times, label='Worst Case',  color='green')
    plt.xlabel('Data Size')
    plt.ylabel('Time (seconds)')
    plt.title('Insertion Operation Analysis')
    plt.legend()
    plt.show()

# Example usage:
benchmark_tree = BenchmarkTree(3)
sizes = [100, 1000, 2000, 5000, 10000, 20000, 50000] 

best_times, average_times, worst_times = benchmark_tree.analyze_insertion(sizes)

plot_analysis(sizes, best_times, average_times, worst_times)
