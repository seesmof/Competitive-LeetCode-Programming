# Клас для збереження пар ключ-значення
class HashEntry:
    def __init__(self, key, value):
        self.key = key  # Ключ
        self.value = value  # Значення
        self.next = None  # Посилання на наступний елемент у ланцюжку


# Клас для реалізації геш-таблиці
class HashTable:
    def __init__(self, size):
        self.size = size  # Розмір геш-таблиці
        self.table = [None] * size  # Масив для збереження ланцюжків

    # Геш-функція множення
    def hash_function(self, key):
        # Використовуємо константу А золотого перетину
        A = (5**0.5 - 1) / 2
        # Обчислюємо геш-значення як дробову частину множення ключа на А, помножену на розмір таблиці
        return int((key * A) % 1 * self.size)

    # Метод для вставлення елементу в геш-таблицю
    def insert(self, key, value):
        # Обчислюємо геш-значення для ключа
        hash_value = self.hash_function(key)
        # Створюємо новий елемент
        entry = HashEntry(key, value)
        # Якщо в таблиці за цим геш-значенням немає елементів, то додаємо новий елемент як перший у ланцюжку
        if self.table[hash_value] is None:
            self.table[hash_value] = entry
        else:
            # Інакше шукаємо останній елемент у ланцюжку і додаємо новий елемент після нього
            current = self.table[hash_value]
            while current.next is not None:
                current = current.next
            current.next = entry

    # Метод для видалення елементу з геш-таблиці за ключем
    def delete(self, key):
        # Обчислюємо геш-значення для ключа
        hash_value = self.hash_function(key)
        # Якщо в таблиці за цим геш-значенням немає елементів, то повертаємо повідомлення про помилку
        if self.table[hash_value] is None:
            print("Немає елемента з таким ключем")
            return
        else:
            # Інакше шукаємо елемент з таким ключем у ланцюжку і видаляємо його
            previous = None
            current = self.table[hash_value]
            while current is not None and current.key != key:
                previous = current
                current = current.next
            # Якщо елемент не знайдено, то повертаємо повідомлення про помилку
            if current is None:
                print("Немає елемента з таким ключем")
                return
            else:
                # Якщо елемент знайдено, то видаляємо його з ланцюжку
                if previous is None:
                    # Якщо елемент є першим у ланцюжку, то змінюємо початок ланцюжку на наступний елемент
                    self.table[hash_value] = current.next
                else:
                    # Інакше пропускаємо елемент у ланцюжку
                    previous.next = current.next

    # Метод для пошуку елементу в геш-таблиці за ключем
    def search(self, key):
        # Обчислюємо геш-значення для ключа
        hash_value = self.hash_function(key)
        # Якщо в таблиці за цим геш-значенням немає елементів, то повертаємо None
        if self.table[hash_value] is None:
            return None
        else:
            # Інакше шукаємо елемент з таким ключем у ланцюжку і повертаємо його значення
            current = self.table[hash_value]
            while current is not None and current.key != key:
                current = current.next
            # Якщо елемент не знайдено, то повертаємо None
            if current is None:
                return None
            else:
                # Якщо елемент знайдено, то повертаємо його значення
                return current.value

    # Метод для відображення структури геш-таблиці
    def display(self):
        # Проходимо по всіх геш-значеннях в таблиці
        for i in range(self.size):
            # Якщо в таблиці за цим геш-значенням є елементи, то виводимо їх у вигляді ланцюжка
            if self.table[i] is not None:
                print(f"Геш-значення {i}: ", end="")
                current = self.table[i]
                while current is not None:
                    print(f"({current.key}, {current.value}) -> ", end="")
                    current = current.next
                print("None")


# Клас для збереження вузлів B-дерева
class BTreeNode:
    def __init__(self, leaf):
        self.leaf = leaf  # Прапорець, що показує, чи є вузол листком
        self.keys = []  # Список ключів у вузлі
        self.children = []  # Список дочірніх вузлів


# Клас для реалізації B-дерева
class BTree:
    def __init__(self, t):
        self.root = None  # Кореневий вузол дерева
        self.t = (
            t  # Мінімальна кількість дочірніх вузлів для кожного вузла (окрім кореня)
        )

    # Метод для створення порожнього дерева
    def create_empty(self):
        # Створюємо новий вузол, який є листком і не має ключів або дочірніх вузлів
        node = BTreeNode(True)
        # Задаємо цей вузол як кореневий
        self.root = node

    # Метод для вставлення ключа в дерево
    def insert(self, key):
        # Якщо дерево порожнє, то створюємо порожнє дерево і вставляємо ключ у кореневий вузол
        if self.root is None:
            self.create_empty()
            self.root.keys.append(key)
        else:
            # Якщо дерево не порожнє, то шукаємо місце для вставлення ключа
            node = self.root
            # Якщо кореневий вузол повний, то розбиваємо його на два і створюємо новий кореневий вузол з середнім ключем
            if len(node.keys) == 2 * self.t - 1:
                new_root = BTreeNode(False)
                new_root.children.append(node)
                self.split_child(new_root, 0)
                self.root = new_root
                node = new_root
            # Проходимо по дереву зверху вниз, розбиваючи повні вузли на шляху, поки не дійдемо до листка
            while not node.leaf:
                i = len(node.keys) - 1
                while i >= 0 and key < node.keys[i]:
                    i -= 1
                i += 1
                # Якщо дочірній вузол повний, то розбиваємо його на два і переставляємо середній ключ у батьківський вузол
                if len(node.children[i].keys) == 2 * self.t - 1:
                    self.split_child(node, i)
                    if key > node.keys[i]:
                        i += 1
                node = node.children[i]
            # Вставляємо ключ у листковий вузол у відповідному місці
            node.keys.append(key)
            node.keys.sort()

    # Метод для розбиття повного дочірнього вузла на два і перестановки середнього ключа у батьківський вузол
    def split_child(self, parent, index):
        # Отримуємо повний дочірній вузол
        full_node = parent.children[index]
        # Створюємо новий вузол для правої половини ключів і дочірніх вузлів
        new_node = BTreeNode(full_node.leaf)
        # Переміщуємо праву половину ключів з повного вузла в новий вузол
        for i in range(self.t - 1):
            new_node.keys.append(full_node.keys.pop(self.t))
        # Якщо повний вузол не є листком, то переміщуємо праву половину дочірніх вузлів з повного вузла в новий вузол
        if not full_node.leaf:
            for i in range(self.t):
                new_node.children.append(full_node.children.pop(self.t))
        # Переміщуємо середній ключ з повного вузла в батьківський вузол на місце індекса
        parent.keys.insert(index, full_node.keys.pop(self.t - 1))
        # Додаємо новий вузол як дочірній для батьківського вузла після індекса
        parent.children.insert(index + 1, new_node)

    # Метод для пошуку ключа в дереві
    def search(self, key):
        # Якщо дерево порожнє, то повертаємо None
        if self.root is None:
            return None
        else:
            # Інакше шукаємо ключ у дереві, починаючи з кореневого вузла
            return self.search_in_node(self.root, key)

    # Метод для пошуку ключа у заданому вузлі
    def search_in_node(self, node, key):
        # Шукаємо позицію ключа у списку ключів вузла
        i = len(node.keys) - 1
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1
        # Якщо ключ знайдено у списку ключів, то повертаємо його індекс і вузол
        if i < len(node.keys) and key == node.keys[i]:
            return (i, node)
        # Якщо вузол є листком, то ключ не знайдено, повертаємо None
        if node.leaf:
            return None
        else:
            # Інакше продовжуємо пошук у дочірньому вузлі
            return self.search_in_node(node.children[i], key)

    # Метод для видалення ключа з дерева
    def delete(self, key):
        # Якщо дерево порожнє, то повертаємо повідомлення про помилку
        if self.root is None:
            print("Дерево порожнє")
            return
        else:
            # Інакше шукаємо ключ у дереві і видаляємо його, починаючи з кореневого вузла
            self.delete_from_node(self.root, key)
            # Якщо після видалення кореневий вузол став порожнім, то замінюємо його першим дочірнім вузлом або робимо дерево порожнім
            if len(self.root.keys) == 0:
                if self.root.leaf:
                    self.root = None
                else:
                    self.root = self.root.children[0]

    # Метод для видалення ключа з заданого вузла
    def delete_from_node(self, node, key):
        # Шукаємо позицію ключа у списку ключів вузла
        i = len(node.keys) - 1
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1
        # Якщо ключ знайдено у списку ключів, то видаляємо його залежно від того, чи є вузол листком
        if i < len(node.keys) and key == node.keys[i]:
            if node.leaf:
                # Якщо вузол є листком, то просто видаляємо ключ зі списку
                node.keys.pop(i)
            else:
                # Якщо вузол не є листком, то шукаємо передник або наступник ключа у дочірніх вузлах і замінюємо ключ на нього, а потім рекурсивно видаляємо передник або наступник
                predecessor = self.get_predecessor(node, i)
                successor = self.get_successor(node, i)
                if len(predecessor.keys) >= self.t:
                    # Якщо лівий дочірній вузол має не менше t ключів, то знаходимо максимальний ключ у ньому (передник) і замінюємо ключ на нього, а потім видаляємо передник з лівого дочірнього вузла
                    node.keys[i] = predecessor.keys[-1]
                    self.delete_from_node(predecessor, predecessor.keys[-1])
                elif len(successor.keys) >= self.t:
                    # Якщо правий дочірній вузол має не менше t ключів, то знаходимо мінімальний ключ у ньому (наступник) і замінюємо ключ на нього, а потім видаляємо наступник з правого дочірнього вузла
                    node.keys[i] = successor.keys[0]
                    self.delete_from_node(successor, successor.keys[0])
                else:
                    # Якщо обидва дочірніх вузли мають по t-1 ключів, то об'єднуємо їх у один вузол з ключем між ними і рекурсивно видаляємо ключ з об'єднаного вузла
                    self.merge_children(node, i)
                    self.delete_from_node(node.children[i], key)
        else:
            # Якщо ключ не знайдено у списку ключів, то продовжуємо пошук у дочірньому вузлі, якщо вузол не є листком
            if node.leaf:
                # Якщо вузол є листком, то ключ не знайдено, повертаємо повідомлення про помилку
                print("Немає такого ключа")
                return
            else:
                # Якщо дочірній вузол має менше t ключів, то заповнюємо його додатковими ключами з сусідніх вузлів або об'єднуємо його з сусідом
                if len(node.children[i].keys) < self.t:
                    self.fill_child(node, i)
                # Якщо вузол змінився після заповнення, то оновлюємо позицію для пошуку
                if i < len(node.keys) and key > node.keys[i]:
                    i += 1
                # Рекурсивно видаляємо ключ з дочірнього вузла
                self.delete_from_node(node.children[i], key)

    # Метод для отримання передника ключа у вузлі (максимального ключа у лівому дочірньому піддереві)
    def get_predecessor(self, node, index):
        # Проходимо по лівому дочірньому піддереву до останнього правого вузла (листка)
        current = node.children[index]
        while not current.leaf:
            current = current.children[-1]
        # Повертаємо останній правий ключ у листку
        return current

    # Метод для отримання наступника ключа у вузлі (мінімального ключа у правому дочірньому піддереві)
    def get_successor(self, node, index):
        # Проходимо по правому дочірньому піддереву до останнього лівого вузла (листка)
        current = node.children[index + 1]
        while not current.leaf:
            current = current.children[0]
        # Повертаємо перший лівий ключ у листку
        return current

    # Метод для заповнення дочірнього вузла додатковими ключами з сусідніх вузлів або об'єднання його з сусідом
    def fill_child(self, node, index):
        # Якщо дочірній вузол має лівого сусіда з не менше t ключами, то переміщуємо останній ключ з сусіда в батьківський вузол, а останній ключ з батьківського вузла в дочірній вузол
        if index > 0 and len(node.children[index - 1].keys) >= self.t:
            self.borrow_from_left(node, index)
        # Якщо дочірній вузол має правого сусіда з не менше t ключами, то переміщуємо перший ключ з сусіда в батьківський вузол, а перший ключ з батьківського вузла в дочірній вузол
        elif index < len(node.keys) and len(node.children[index + 1].keys) >= self.t:
            self.borrow_from_right(node, index)
        # Якщо обидва сусіди мають по t-1 ключів, то об'єднуємо дочірній вузол з одним із сусідів і переміщуємо ключ з батьківського вузла між ними
        else:
            if index < len(node.keys):
                self.merge_children(node, index)
            else:
                self.merge_children(node, index - 1)

    # Метод для переміщення першого ключа з правого сусіда в батьківський вузол, а першого ключа з батьківського вузла в дочірній вузол
    def borrow_from_right(self, node, index):
        # Отримуємо дочірній вузол і його правого сусіда
        child = node.children[index]
        right_sibling = node.children[index + 1]
        # Додаємо перший ключ з батьківського вузла в кінець списку ключів дочірнього вузла
        child.keys.append(node.keys[index])
        # Замінюємо перший ключ з батьківського вузла на перший ключ з правого сусіда
        node.keys[index] = right_sibling.keys.pop(0)
        # Якщо правий сусід не є листком, то переміщуємо його першого дочірнього вузла в кінець списку дочірніх вузлів дочірнього вузла
        if not right_sibling.leaf:
            child.children.append(right_sibling.children.pop(0))

    # Метод для об'єднання двох дочірніх вузлів з одним із сусідів і переміщення ключа з батьківського вузла між ними
    def merge_children(self, node, index):
        # Отримуємо дочірній вузол і його правого сусіда
        child = node.children[index]
        right_sibling = node.children[index + 1]
        # Додаємо ключ з батьківського вузла в кінець списку ключів дочірнього вузла
        child.keys.append(node.keys.pop(index))
        # Додаємо всі ключі з правого сусіда в кінець списку ключів дочірнього вузла
        child.keys.extend(right_sibling.keys)
        # Якщо дочірній вузол не є листком, то додаємо всі дочірні вузли з правого сусіда в кінець списку дочірніх вузлів дочірнього вузла
        if not child.leaf:
            child.children.extend(right_sibling.children)
        # Видаляємо правого сусіда з списку дочірніх вузлів батьківського вузла
        node.children.pop(index + 1)

    # Метод для виводу структури дерева
    def display(self):
        # Якщо дерево порожнє, то повертаємо повыдомлення про це
        if self.root is None:
            print("Дерево порожнє")
            return
        else:
            # Інакше рекурсивно виводимо структуру дерева, починаючи з кореневого вузла і рiвня 0
            self.display_node(self.root, 0)

    # Метод для рекурсивного виводу структури заданого вузла на заданому рiвнi
    def display_node(self, node, level):
        # Виводимо пробiли для видiлення рiвня
        print(" " * level * 4, end="")
        # Виводимо ключi у квадратних дужках
        print("[", end="")
        for key in node.keys:
            print(key, end=" ")
        print("]")
        # Якщо вузол не є листком, то рекурсивно виводимо його дочірнi вузли на наступному рiвнi
        if not node.leaf:
            for child in node.children:
                self.display_node(child, level + 1)
