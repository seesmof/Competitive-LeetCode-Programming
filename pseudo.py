class Heap:
    def __init__(self):
        self.heap = []

    def _siftUp(self, i):
        while (i - 1) // 2 >= 0:
            if self.heap[(i - 1) // 2] < self.heap[i]:
                self._swap((i - 1) // 2, i)
            i = (i - 1) // 2

    def _siftDown(self, i):
        while 2 * i + 1 < len(self.heap):
            max_child_index = self._getMaxChild(i)
            if self.heap[max_child_index] > self.heap[i]:
                self._swap(max_child_index, i)
            i = max_child_index

    def _getMaxChild(self, i):
        if 2 * i + 2 > len(self.heap) - 1:
            return 2 * i + 1
        if self.heap[2 * i + 1] > self.heap[2 * i + 2]:
            return 2 * i + 1
        return 2 * i + 2

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
            print(item)
