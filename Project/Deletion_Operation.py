import time
import random
import matplotlib.pyplot as plt

class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

    def remove_key(self, key):
        if key in self.keys:
            self.keys.remove(key)
            return True, self

        return False, self

class BTree:
    def __init__(self, degree):
        self.root = BTreeNode(leaf=True)
        BTree.degree = degree

    def delete(self, key):
        if not self.root:
            return False

        deleted, self.root = self.root.remove_key(key)

        if not self.root.keys:
            self.root = None

        return deleted

class PerformanceBTree:
    def __init__(self, degree):
        self.tree = BTree(degree)

    def generate_data(self, size):
        return [random.randint(1, 1000000) for _ in range(size)]

    def test_deletion(self, data):
        start_time = time.time()
        for key in data:
            self.tree.delete(key)
        end_time = time.time()
        return end_time - start_time

    def evaluate_deletion(self, data_sizes):
        best_times = []
        average_times = []
        worst_times = []

        for size in data_sizes:
            data = self.generate_data(size)

            # Best case: Key to be deleted is at the root
            self.tree = BTree(3)
            self.tree.root = BTreeNode(leaf=True)  # Reset root to an empty leaf node
            self.tree.root.keys = [data[0]]  # Insert key directly at the root
            deletion_time = self.test_deletion([data[0]])
            best_times.append(deletion_time)

            # Worst case: Key to be deleted requires merging of nodes
            self.tree = BTree(3)
            for key in data:
                self.tree.delete(key)
            deletion_time = self.test_deletion([random.choice(data)])
            worst_times.append(deletion_time)

            # Average case: Randomly generated keys
            self.tree = BTree(3)
            for key in data:
                self.tree.delete(key)
            deletion_time = self.test_deletion([random.choice(data)])
            average_times.append(deletion_time)

        return best_times, average_times, worst_times

def visualize_deletion_analysis(data_sizes, best_times, average_times, worst_times):
    plt.plot(data_sizes, best_times, label='Best Case', linestyle='-', linewidth=2, color='red')
    plt.plot(data_sizes, average_times, label='Average Case', linestyle='--', linewidth=2, color='green')
    plt.plot(data_sizes, worst_times, label='Worst Case', linestyle='-.', linewidth=2, color='skyblue')
    plt.xlabel('Data Size')
    plt.ylabel('Time (seconds)')
    plt.title('Deletion Operation Analysis')
    plt.legend()
    plt.show()

# Example usage:
btree = PerformanceBTree(3)
data_sizes = [500, 1000, 2000, 5000, 10000, 20000, 50000]  

best_times, average_times, worst_times = btree.evaluate_deletion(data_sizes)

visualize_deletion_analysis(data_sizes, best_times, average_times, worst_times)
