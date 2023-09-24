class MaxHeap:
    def __init__(self):
        # Initializing a list that will serve as our heap
        self.heap = []

    def insert(self, item):
        # Appending the item to the end of the heap
        self.heap.append(item)
        # Ensuring that the heap property is maintained after insertion
        self.__floatup(len(self.heap) - 1)

    def peek(self):
        # If the heap has at least one element, we get the maximum value (which is at the root of the heap)
        if self.heap:
            return self.heap[0]

    def pop(self):
        # Checking if the heap has more than one element
        if len(self.heap) > 1:
            # Swapping the root of the heap with the last element
            self.__swap(0, len(self.heap) - 1)
            # Removing the last element (which is now the maximum)
            max = self.heap.pop()
            # Ensuring that the heap property is maintained after removal
            self.__sinkdown(0)
        # If the heap has exactly one element, we simply remove it
        elif len(self.heap) == 1:
            max = self.heap.pop()
        # If the heap is empty, we cannot remove an element
        else:
            max = False
        # The removed element is returned
        return max

    def __swap(self, i, j):
        # Swapping the elements at indices i and j
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatup(self, index):
        # Calculating the parent's index
        parent = (index - 1) // 2
        # If we are already at the root, we can't float up
        if index <= 0:
            return
        # If the current node is larger than the parent, we swap them
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            # Recursing to ensure that the heap property is still maintained
            self.__floatup(parent)

    def __sinkdown(self, index):
        # Calculating the indices of the children
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        # If the left child exists and is larger than the current node, it becomes the largest
        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left
        # If the right child exists and is larger than the current largest, it becomes the largest
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right
        # If the largest is not the current node, we swap them
        if largest != index:
            self.__swap(index, largest)
            # Recursing to ensure that the heap property is still maintained
            self.__sinkdown(largest)

    def buildHeap(self, arr):
        # Building a max heap from an array by first copying it to our heap
        self.heap = arr
        # Iterating over the array from the middle to the start (inclusive)
        for i in range(len(arr) // 2, -1, -1):
            # For each index, sink it down so that the heap property is maintained
            self.__sinkdown(i)

    def display(self):
        # Printing the heap twice for reasons that may be specific to the user
        print(self.heap)


heap = MaxHeap()
heap.insert(20)
heap.insert(15)
heap.insert(14)
heap.insert(10)
heap.insert(12)
heap.display()
print(heap.peek())
heap.pop()
heap.display()
arr = [3, 4, 9, 7, 1, 8, 2, 6, 5]
heap.buildHeap(arr)
heap.display()
