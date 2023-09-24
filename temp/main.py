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

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 1

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

    def buildHeap(self, arr):
        pass

    def pop(self):
        pass

    def sortHeap(self):
        pass

    def heapSort(self):
        pass

    def display(self):
        pass
