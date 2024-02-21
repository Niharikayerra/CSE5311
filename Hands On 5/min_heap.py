class MinHeap:
    def __init__(self):
        self.heap = []
    def parent(self,i):
        return(i-1)>>1
    def left(self,i):
        return(i<<1)+1
    def right(self,i):
        return(i<<1)+2
    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    def heapify(self,i):
        left = self.left(i)
        right = self.right(i)
        smallest = i
        if left<len(self.heap) and self.heap[left]<self.heap[i]:
            smallest = left
        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i,smallest)
            self.heapify(smallest)
    def build_min_heap(self,array):
        self.heap = array
        n = len(array)
        for i in range(n//2-1,-1,-1):
            self.heapify(i)
    def insert(self,value):
        self.heap.append(value)
        i = len(self.heap)-1
        while i>0 and self.heap[self.parent(i)]>self.heap[i]:
            self.swap(i,self.parent(i))
            i = self.parent(i)
    def pop_min(self):
        if not self.heap:
            return None
        min_value = self.heap[0]
        self.swap(0,len(self.heap)-1)
        self.heap.pop()
        self.heapify(0)
        return min_value
    def peek_min(self):
        return self.heap[0] if self.heap else None
    def __str__(self):
        return 'min_heap = ' + str(self.heap)
    
    #Example
if __name__ == "__main__":
    heap = MinHeap()
    heap.build_min_heap([9,5,3,2,4,1,6])
    print(heap)        # Output : [1,2,3,5,4,9,6]
    heap.insert(7)
    print("After inserting :",heap)   # Output : [1,2,3,5,4,9,6,7]
    print("popped minimum element is:",heap.pop_min())   # Output : 1
    print("After Popping :",heap)     # Output : [2,4,3,5,7,9,6]



