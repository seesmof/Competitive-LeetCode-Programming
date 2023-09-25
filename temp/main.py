"""
- Розроблюваний програмний проєкт має складатися з окремих класів, що реалізують структури даних двозв’язний список та купа (черга з пріоритетами). На найвищий рівень може бути передбачено графічну інтерфейсну взаємодію з користувачем для роботи зі створеними класами.
- Клас, що реалізує двозв’язний список, має дозволяти виконувати наступні операції на основі окремих методів: додавання вузла в початок списку, додавання вузла після заданого, пошук вузла в списку, видалення вузла, виведення вузлів на екран з початку та з кінця.
- Клас, що реалізує купу (чергу з пріоритетами), має дозволяти виконувати наступні операції на основі окремих методів: вставлення елементу, сортування елементів, побудова купи з невпорядкованого масиву, видалення елементу, сортування елементів із використанням купи, виведення елементів на екран.
- Розробити окремий модуль програмного забезпечення для реалізації пірамідального сортування на основі розробленого класу.
- Розв’язати індивідуальне завдання за допомогою розробленої реалізації пірамідального сортування. Вважати, що масиви даних зберігаються в файлах.
  - Варіант: У відділі кадрів міститься інформація про захворювання співробітників, що включає: прізвище, ім’я, по батькові співробітника; відділ, посаду; вік; дату початку лікарняного; дату завершення лікарняного; хвороба. Вивести інформацію про всі хвороби, якими хворіли співробітники, за зменшенням кількості випадків.
"""

import json


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

    def insert(self, value):
        self.heap.append(value)
        self._heapifyUp(len(self.heap) - 1)

    def sort(self):
        sortedItems = []
        size = len(self.heap)
        for _ in range(size):
            sortedItems.append(self.delete())
        return sortedItems

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self._heapifyDown(i)

    def delete(self):
        # if the heap is empty, return null
        if len(self.heap) == 0:
            return None
        # swap root with the last element
        self._swap(0, len(self.heap) - 1)
        # assign root to temporary veriable
        root = self.heap.pop()
        # heapify the new root, which previously was the last element, to set it in a correct position
        self._heapifyDown(0)
        # return the original root
        return root

    def display(self):
        for item in self.heap:
            print(item, end=" ")
        print()

    def _heapifyUp(self, index):
        parentIndex = (index - 1) // 2
        if parentIndex >= 0 and self.heap[index] > self.heap[parentIndex]:
            self._swap(parentIndex, index)
            self._heapifyUp(parentIndex)

    def _heapifyDown(self, index):
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2
        largest = index
        if (
            leftChildIndex < len(self.heap)
            and self.heap[leftChildIndex] > self.heap[largest]
        ):
            largest = leftChildIndex
        if (
            rightChildIndex < len(self.heap)
            and self.heap[rightChildIndex] > self.heap[largest]
        ):
            largest = rightChildIndex
        if largest != index:
            self._swap(index, largest)
            self._heapifyDown(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def heapSort(arr):
    heap = Heap()
    # inserting each item from the array into the heap. maintaining the heap structure
    for num in arr:
        heap.insert(num)
    sortedArray = []
    while True:
        # getting the largest element, which is also a root, by using a delete method
        num = heap.delete()
        # break out if there's no more elements
        if num is None:
            break
        # append the element into the temporary array
        sortedArray.append(num)
    return sortedArray


def getEmployeesData():
    # opening file for read and reading JSON data from a file into the variable
    with open("employees.json", "r") as inputFile:
        data = json.load(inputFile)
    return data


def countDiseaseCases(employeeData):
    diseasesCount = dict()
    for employee in employeeData["employees"]:
        # if employee's disease doesn't yet exist in the dictionary
        if employee["disease"] not in diseasesCount:
            # add it with a count of 0
            diseasesCount[employee["disease"]] = 0
        # else just increment the count
        diseasesCount[employee["disease"]] += 1
    return diseasesCount


def demoDoublyLinkedList():
    linkedListDemo = DoublyLinkedList()

    linkedListDemo.append("Node1")
    linkedListDemo.append("Node2")
    linkedListDemo.append("Node3")

    print("Displaying list from head:")
    linkedListDemo.displayFromHead()

    print("\nDisplaying list from tail:")
    linkedListDemo.displayFromTail()

    linkedListDemo.appendAfterNode("Node2", "Node2.5")
    print("\nAfter adding a node after Node2:")
    linkedListDemo.displayFromHead()

    print("\nSearching for Node2.5:")
    print(linkedListDemo.search("Node2.5"))

    linkedListDemo.delete("Node2.5")
    print("\nAfter deleting Node2.5:")
    linkedListDemo.displayFromHead()


def main():
    # getting raw emloyee data from a JSON file
    employeeData = getEmployeesData()
    # counting number of occurences of each disease
    diseasesCount = countDiseaseCases(employeeData)
    # converting disease occurences to a list of tuples
    diseasesCountList = [
        (occurences, name) for name, occurences in diseasesCount.items()
    ]

    print("Welcome! Make your choice below\n")

    while True:
        print("1. See a demo of a doubly linked list usage")
        print("2. See the raw data from your file")
        print("3. Sort the data")
        print("4. See the number of occurrences for each disease")
        print("5. Exit")
        choice = input("> ")

        print("\n---\n")
        if choice == "1":
            demoDoublyLinkedList()
        elif choice == "2":
            for employee in employeeData["employees"]:
                print(
                    f"- {employee['name']} - {employee['age']} years old, had {employee['disease']}. Works in {employee['department']} as a {employee['position']}"
                )
        elif choice == "3":
            diseasesCountList = heapSort(diseasesCountList)
            print("Data successfully sorted")
        elif choice == "4":
            for occurences, name in diseasesCountList:
                print(f"- {name}: {occurences} times")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    print()
    main()
    print()
