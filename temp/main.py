"""
- Розроблюваний програмний проєкт має складатися з окремих класів, що реалізують структури даних двозв’язний список та купа (черга з пріоритетами). На найвищий рівень може бути передбачено графічну інтерфейсну взаємодію з користувачем для роботи зі створеними класами.
- Клас, що реалізує двозв’язний список, має дозволяти виконувати наступні операції на основі окремих методів: додавання вузла в початок списку, додавання вузла після заданого, пошук вузла в списку, видалення вузла, виведення вузлів на екран з початку та з кінця.
- Клас, що реалізує купу (чергу з пріоритетами), має дозволяти виконувати наступні операції на основі окремих методів: вставлення елементу, сортування елементів, побудова купи з невпорядкованого масиву, видалення елементу, сортування елементів із використанням купи, виведення елементів на екран.
- Розробити окремий модуль програмного забезпечення для реалізації пірамідального сортування на основі розробленого класу.
- Розв’язати індивідуальне завдання за допомогою розробленої реалізації пірамідального сортування. Вважати, що масиви даних зберігаються в файлах.
  - Варіант: У відділі кадрів міститься інформація про захворювання співробітників, що включає: прізвище, ім’я, по батькові співробітника; відділ, посаду; вік; дату початку лікарняного; дату завершення лікарняного; хвороба. Вивести інформацію про всі хвороби, якими хворіли співробітники, за зменшенням кількості випадків.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def prepand(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            newNode = Node(data)
            currentNode.next = newNode
            newNode.prev = currentNode

    def appendAfterNode(self, nodeData, data):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == nodeData:
                newNode = Node(data)
                newNode.prev = currentNode
                newNode.next = currentNode.next
                if currentNode.next is not None:
                    currentNode.next.prev = newNode
                currentNode.next = newNode
                return
            currentNode = currentNode.next

    def search(self, data) -> bool:
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
                return True
            currentNode = currentNode.next
        return False

    def delete(self, data) -> bool:
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
                if currentNode.prev is not None:
                    currentNode.prev.next = currentNode.next
                if currentNode.next is not None:
                    currentNode.next.prev = currentNode.prev
                if currentNode == self.head:
                    self.head = currentNode.next
                return True
            currentNode = currentNode.next
        return False

    def displayFromHead(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("None")

    def displayFromTail(self):
        if self.head is None:
            print("None")
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        while currentNode is not None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.prev
        print("None")


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
