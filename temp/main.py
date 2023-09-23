"""
- Розроблюваний програмний проєкт має складатися з окремих класів, що реалізують структури даних двозв’язний список та купа (черга з пріоритетами). На найвищий рівень може бути передбачено графічну інтерфейсну взаємодію з користувачем для роботи зі створеними класами.
- Клас, що реалізує двозв’язний список, має дозволяти виконувати наступні операції на основі окремих методів: додавання вузла в початок списку, додавання вузла після заданого, пошук вузла в списку, видалення вузла, виведення вузлів на екран з початку та з кінця.
- Клас, що реалізує купу (чергу з пріоритетами), має дозволяти виконувати наступні операції на основі окремих методів: вставлення елементу, сортування елементів, побудова купи з невпорядкованого масиву, видалення елементу, сортування елементів із використанням купи, виведення елементів на екран.
- Розробити окремий модуль програмного забезпечення для реалізації пірамідального сортування на основі розробленого класу.
- Розв’язати індивідуальне завдання за допомогою розробленої реалізації пірамідального сортування. Вважати, що масиви даних зберігаються в файлах.
  - Варіант: У відділі кадрів міститься інформація про захворювання співробітників, що включає: прізвище, ім’я, по батькові співробітника; відділ, посаду; вік; дату початку лікарняного; дату завершення лікарняного; хвороба. Вивести інформацію про всі хвороби, якими хворіли співробітники, за зменшенням кількості випадків.
"""


class Heap:
    def __init__(self):
        self.heap = []

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n // 2, 0, -1):
            self._heapify(i, n)

    def _heapify(self, i, n):
        left = 2 * i
        right = 2 * i + 1
        max_idx = i

        if left <= n and self.heap[left - 1] > self.heap[max_idx - 1]:
            max_idx = left

        if right <= n and self.heap[right - 1] > self.heap[max_idx - 1]:
            max_idx = right

        if max_idx != i:
            self.heap[i - 1], self.heap[max_idx - 1] = (
                self.heap[max_idx - 1],
                self.heap[i - 1],
            )
            self._heapify(max_idx, n)

    def heapsort(self):
        n = len(self.heap)
        self.build_max_heap()
        for i in range(n, 0, -1):
            self.heap[0], self.heap[i - 1] = self.heap[i - 1], self.heap[0]
            n -= 1
            self._heapify(1, n)


heap = Heap()
heap.heap = [1, 2, 3, 4, 5, 6, 7, 8]
heap.heapsort()
print(heap.heap)


class EmployeeData:
    def __init__(
        self,
        name: str,
        department: str,
        position: str,
        age: int,
        start_date: str,
        end_date: str,
        disease: str,
    ):
        self.name = name
        self.department = department
        self.position = position
        self.age = age
        self.start_date = start_date
        self.end_date = end_date
        self.disease = disease


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        return False

    def length(self) -> int:
        cur = self.head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next

        return count

    def search(self, data):
        cur = self.head

        while cur is not None:
            if cur.data == data:
                return cur
            cur = cur.next

        return None

    def prepend(self, data):
        new = ListNode(data)

        if self.isEmpty():
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def append(self, data):
        new = ListNode(data)

        if self.isEmpty():
            self.prepend(data)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new
            new.prev = cur

    def appendAfterElement(self, data, element: ListNode):
        tmp = self.head
        while tmp is not None:
            if tmp.data == element:
                break
            tmp = tmp.next

        if tmp is not None:
            new = ListNode(data)
            new.next = tmp.next
            new.prev = tmp
            tmp.next = new
            tmp.next.prev = new
        else:
            print(f"Element {element} not found.")

    def displayFromHead(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next

    def displayFromTail(self):
        cur = self.head
        els = []
        while cur.next is not None:
            els.append(cur)
            cur = cur.next
        els.reverse()
        for el in els:
            print(el.data, end=" ")

    def delete(self, data):
        if self.isEmpty():
            print(f"List is empty, cannot delete any elements.")
        elif self.length() == 1:
            if self.head.data == data:
                self.head = None

        else:
            cur = self.head
            while cur is not None:
                if cur.data == data:
                    break
                cur = cur.next
            if cur is None:
                print(f"Element {data} not found.")
            elif cur.next is None:
                tmp = self.head
                while tmp.next is not None:
                    tmp = tmp.next
                tmp.prev.next = None
                tmp.prev = None
            else:
                cur.next = cur.prev.next
                cur.next.prev = cur.prev
                cur.next = None
                cur.prev = None


def heapsort(A):
    def buildMaxHeap(A):
        n = len(A)
        for i in range(n // 2, 0, -1):
            heapify(A, i, n)

    def heapify(A, i, n):
        left = 2 * i
        right = 2 * i + 1
        max_idx = i

        if left <= n and A[left - 1] > A[max_idx - 1]:
            max_idx = left

        if right <= n and A[right - 1] > A[max_idx - 1]:
            max_idx = right

        if max_idx != i:
            A[i - 1], A[max_idx - 1] = A[max_idx - 1], A[i - 1]
            heapify(A, max_idx, n)

    n = len(A)
    buildMaxHeap(A)
    for i in range(n, 0, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        n -= 1
        heapify(A, 1, n)


# Example usage:
A = [4, 10, 3, 5, 1]
heapsort(A)
print(A)  # Output: [1, 3, 4, 5, 10]
