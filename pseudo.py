class Heap:
    def __init__(self):
        self.heap = []

    def _siftUp(self, index):
        while (index - 1) // 2 >= 0:
            if self.heap[(index - 1) // 2] < self.heap[index]:
                self._swap((index - 1) // 2, index)
            index = (index - 1) // 2

    def _siftDown(self, index):
        while (index * 2) + 1 < len(self.heap):
            mc = self._getMaxChild(index)
            if self.heap[mc] > self.heap[index]:
                self._swap(index, mc)
            index = mc

    def _getMaxChild(self, index):
        if (index * 2) + 2 > len(self.heap) - 1:
            return (index * 2) + 1
        else:
            if self.heap[(index * 2) + 1] > self.heap[(index * 2) + 2]:
                return (index * 2) + 1
            else:
                return (index * 2) + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        self.heap.append(item)
        self._siftUp(len(self.heap) - 1)

    def sort(self):
        sorted_items = []
        size = len(self.heap)
        for _ in range(size):
            sorted_items.append(self.delete())
        return sorted_items

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self._siftDown(i)

    def delete(self):
        removed = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 0:
            self._siftDown(0)
        return removed

    def display(self):
        for item in self.heap:
            print(item, end=" ")
        print()
