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

    def delete(self, data):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
                if currentNode.prev is not None:
                    currentNode.prev.next = currentNode.next
                if currentNode.next is not None:
                    currentNode.next.prev = currentNode.prev
                if currentNode == self.head:
                    self.head = currentNode.next
                return
            currentNode = currentNode.next

    def display(self):
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


LinkedList = DoublyLinkedList()
LinkedList.append(21)
LinkedList.append(52)
LinkedList.append(33)
LinkedList.append(12)
LinkedList.append(26)
LinkedList.display()
