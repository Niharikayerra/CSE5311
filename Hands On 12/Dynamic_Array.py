class DynamicArray:
    def __init__(self):
        self.arr = []
        self.size = 0

    def push_back(self, value):
        self.arr.append(value)
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError("Array is empty")
        self.arr.pop()
        self.size -= 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        self.arr.insert(index, value)
        self.size += 1

    def remove(self, value):
        try:
            self.arr.remove(value)
            self.size -= 1
        except ValueError:
            raise ValueError("Value not found in array")

    def resize(self, new_size):
        if new_size < 0:
            raise ValueError("New size must be non-negative")
        self.arr = self.arr[:new_size]
        self.size = min(new_size, self.size)

    def at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.arr[index]

    def getSize(self):
        return self.size
    
    def add(self, value):
        if self.size == len(self.arr):
           self.resize(2 * self.size)
        self.arr.append(value)
        self.size += 1


    def __len__(self):
        return self.size


#example

dynamic_array = DynamicArray()
dynamic_array.add(10)
dynamic_array.add(30)
dynamic_array.add(70)
dynamic_array.add(90)

print("Elements of the array:", [dynamic_array.at(i) for i in range(len(dynamic_array))])
print("Length of the array:", len(dynamic_array))

dynamic_array.insert(2, 50)
print("\nArray after inserting 50 at index 2:")
for i in range(dynamic_array.getSize()):
    print(dynamic_array.at(i), end=" ")
print()


dynamic_array.remove(30)
print("\nArray after removing 30:")
for i in range(dynamic_array.getSize()):
    print(dynamic_array.at(i), end=" ")
print("\n")

dynamic_array.add(40)
print("Elements after adding an element:", [dynamic_array.at(i) for i in range(len(dynamic_array))])
print("Length after adding an element:", len(dynamic_array))

dynamic_array.resize(3)
print("\nArray after resizing to 3 elements:")
for i in range(dynamic_array.getSize()):
    print(dynamic_array.at(i), end=" ")
print()

dynamic_array.pop_back()
print("\nArray after popping the last element:")
for i in range(dynamic_array.getSize()):
     print(dynamic_array.at(i), end=" ")
print()
