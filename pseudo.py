class Heap:
    def __init__(self):
        self.heap = []

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._heapify(largest)

    def push(self, item):
        self.heap.append(item)
        self._heapify(self.heap)

    def buildHeap(self):
        for i in reversed(range(len(self.heap) // 2)):
            self._heapify(i)

    def pop(self):
        pass

    def sortHeap(self):
        pass

    def heapSort(self):
        pass

    def display(self):
        pass
