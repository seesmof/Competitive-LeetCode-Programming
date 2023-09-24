class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapifyUp(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None

        self._swap(0, len(self.heap) - 1)
        root = self.heap.pop()
        self._heapifyDown(0)

        return root

    def _heapifyUp(self, index):
        parent_index = (index - 1) // 2

        if parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            self._swap(parent_index, index)
            self._heapifyUp(parent_index)

    def _heapifyDown(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] > self.heap[largest]
        ):
            largest = left_child_index

        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] > self.heap[largest]
        ):
            largest = right_child_index

        if largest != index:
            self._swap(index, largest)
            self._heapifyDown(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def heapSort(arr):
    heap = Heap()

    for num in arr:
        heap.insert(num)

    sorted_arr = []
    while True:
        num = heap.delete()
        if num is None:
            break
        sorted_arr.append(num)

    return sorted_arr


arr = [5, 9, 3, 6, 11, 2, 8]
print(heapSort(arr))

arr = [4, 10, 3, 5, 1]
print(heapSort(arr))
