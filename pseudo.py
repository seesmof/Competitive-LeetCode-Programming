class Heap:
    def __init__(self):
        self.heap = []

    def _siftUp(self, index):
        while (index - 1) // 2 >= 0:
            if self.heap[(index - 1) // 2] < self.heap[index]:
                self._swap((index - 1) // 2, index)
            index = (index - 1) // 2

    def _siftDown(self, index):
        while 2 * index + 1 < len(self.heap):
            max_child_index = self._getMaxChild(index)
            if self.heap[max_child_index] > self.heap[index]:
                self._swap(max_child_index, index)
            index = max_child_index

    def _getMaxChild(self, index):
        if 2 * index + 2 > len(self.heap) - 1:
            return 2 * index + 1
        if self.heap[2 * index + 1] > self.heap[2 * index + 2]:
            return 2 * index + 1
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        self.heap.append(item)
        self._siftUp(len(self.heap) - 1)

    def sort(self):
        sorted_items = []
        while self.heap:
            sorted_items.append(self.delete())
        return sorted_items

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(self.heap) // 2, -1, -1):
            self._siftDown(i)

    def delete(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._siftDown(0)
        return max_val

    def display(self):
        for item in self.heap:
            print(item, end=" ")
        print()


heap = Heap()

# Insert numbers into the heap
for i in [2, 7, 1, 3, 5, 12, 8, 4, 6, 9, 11, 10]:
    heap.insert(i)

# Display the heap
heap.display()

# Delete the max item from the heap and display the heap
print("Deleted:", heap.delete())
heap.display()

# Sort all items in the heap and display them
sorted_items = heap.sort()
print("Sorted items:", sorted_items)

# Build heap from a list and display it
heap.buildHeap([7, 12, 5, 6, 13, 9, 10, 15, 11, 8])
heap.display()
