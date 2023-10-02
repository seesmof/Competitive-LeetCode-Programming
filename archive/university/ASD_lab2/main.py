"""
- Розроблюваний програмний проєкт має складатися з окремих класів, що реалізують структури даних геш-таблиця та бінарне дерево пошуку, а також має містити окремий модуль, що забезпечує інтерфейсну взаємодію з користувачем для роботи зі створеними класами.
- Клас, що реалізує геш-таблицю, має дозволяти виконувати наступні операції на основі окремих методів: вставлення елементу, видалення елементу, пошук елементу, відображення структури геш-таблиці на основі використання параметрів, обраних у відповідності з варіантом індивідуального завдання
- Клас, що реалізує B-дерево, має дозволяти виконувати наступні операції на основі окремих методів: створення порожнього дерева, відображення структури дерева, пошук у дереві, вставлення ключа, видалення ключа.
- Розв’язати індивідуальне завдання з таблиці, що складається з 2 задач, наведених нижче, за допомогою розроблених модулів програмного забезпечення. 
- Створити геш-таблицю, що використовує метод ланцюжків для розв’язання колізій та геш-функцію множення. Геш-таблицю заповнити на основі виділення інформації з текстового файлу, в якому містяться прізвища, ім’я і по батькові співробітників фірми та займані ними посади. Ви значити посаду заданого співробітника.
- Мобільний оператор повинен мати інформацію про абонентів для забезпечення послуг. Кожний абонент характеризується номером, прізвищем, ім’ям, по батькові, тарифним планом. Сформувати дерево з відповідної інформації про абонентів, забезпечити пошук інформації про абонента за його телефонним номером та визначення кількості підключень за кожним з тарифів.
"""


class HashTable:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        hashed = 0
        for char in str(key):
            hashed += ord(char)
        return hashed % self.size

    def insert(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            self.map[key_hash] = [[key, value]]
        else:
            self.map[key_hash].append([key, value])
        return True

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def search(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def display(self):
        for item in self.map:
            if item is not None:
                print(str(item))


# Demonstrating use of HashTable class
hashTable = HashTable()
hashTable.insert(1, "One")
hashTable.insert(2, "Two")
hashTable.insert(3, "Three")
hashTable.insert(4, "Four")
hashTable.insert(5, "Five")
hashTable.insert(6, "Six")

# Displaying entire hash table
hashTable.display()

# Searching for an element
result = hashTable.search(2)
print(f"Search Result for 2: {result}")

# Deleting an Element
hashTable.delete(2)

# Displaying hash table after deletion
hashTable.display()
