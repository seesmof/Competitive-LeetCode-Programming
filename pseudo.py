class Heap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        l, r, m = 2 * i + 1, 2 * i + 2, i
        if l < len(self.heap) and self.heap[i] < self.heap[l]:
            m = l
        if r < len(self.heap) and self.heap[m] < self.heap[r]:
            m = r
        if m != i:
            self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
            self.heapify(m)

    def push(self, item):
        self.heap.append(item)
        self.heapify(self.heap)

    def buildHeap(self):
        pass

    def pop(self):
        pass

    def sortHeap(self):
        pass

    def heapSort(self):
        pass

    def display(self):
        pass
