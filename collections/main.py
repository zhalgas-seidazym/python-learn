from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap

# Создание счетчика из списка
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})

# 🔹 Доступ к количеству элемента
print(counter['apple'])  # 3

# 🔹 Получение самых частых элементов
print(counter.most_common(2))  # [('apple', 3), ('banana', 2)]

# 🔹 Итерация по элементам
print(list(counter.elements()))  # ['apple', 'apple', 'apple', 'banana', 'banana', 'orange']

# 🔹 Обновление счетчика
counter.update(['apple', 'banana', 'grape'])
print(counter)  # Counter({'apple': 4, 'banana': 3, 'orange': 1, 'grape': 1})

# 🔹 Вычитание элементов
counter.subtract(['apple', 'banana', 'banana'])
print(counter)  # Counter({'apple': 3, 'banana': 1, 'orange': 1, 'grape': 1})

# -------------------------------------------------------------------------------

# 🔹 Пример с list
my_dict = defaultdict(list)
my_dict['a'].append(1)
print(my_dict)  # {'a': [1]}

# 🔹 Пример с int
counter_dict = defaultdict(int)
counter_dict['a'] += 1
print(counter_dict)  # {'a': 1}

# 🔹 Пример с set
set_dict = defaultdict(set)
set_dict['b'].add(5)
print(set_dict)  # {'b': {5}}

# -------------------------------------------------------------------------------

# 🔹 Создание упорядоченного словаря
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

print(ordered_dict)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 🔹 Перемещение элемента в конец
ordered_dict.move_to_end('a')
print(ordered_dict)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# 🔹 Перемещение в начало
ordered_dict.move_to_end('c', last=False)
print(ordered_dict)  # OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# 🔹 Удаление последнего элемента
ordered_dict.popitem()
print(ordered_dict)  # OrderedDict([('c', 3), ('b', 2)])

# --------------------------------------------------------------------------------------

# 🔹 Создание двусторонней очереди
dq = deque([1, 2, 3])
print(dq)  # deque([1, 2, 3])

# 🔹 Добавление элементов
dq.append(4)  # В конец
dq.appendleft(0)  # В начало
print(dq)  # deque([0, 1, 2, 3, 4])

# 🔹 Удаление элементов
dq.pop()  # Удаляет с конца
dq.popleft()  # Удаляет с начала
print(dq)  # deque([1, 2, 3])

# 🔹 Ограничение размера (автоматически удаляет старые элементы)
dq = deque([1, 2, 3, 4], maxlen=3)
print(dq)  # deque([2, 3, 4], maxlen=3)

# 🔹 Циклический сдвиг
dq.rotate(1)  # Сдвиг вправо
print(dq)  # deque([4, 2, 3], maxlen=3)

# ---------------------------------------------------------------------------------------

# 🔹 Создание именованного кортежа
Person = namedtuple('Person', ['name', 'age', 'city'])
p = Person(name='Alice', age=30, city='New York')

print(p.name)  # Alice
print(p.age)  # 30
print(p.city)  # New York

# 🔹 Преобразование в словарь
print(p._asdict())  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 🔹 Создание из списка/слов
data = ['Bob', 25, 'Los Angeles']
p2 = Person._make(data)
print(p2)  # Person(name='Bob', age=25, city='Los Angeles')

# 🔹 Замена значения
p3 = p._replace(age=35)
print(p3)  # Person(name='Alice', age=35, city='New York')

# -----------------------------------------------------------------------

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# 🔹 Объединение словарей
chain = ChainMap(dict1, dict2)
print(chain['a'])  # 1 (из dict1)
print(chain['b'])  # 2 (из dict1, т.к. он первый в цепочке)
print(chain['c'])  # 4 (из dict2)

# 🔹 Добавление нового уровня
new_dict = {'d': 5}
chain = chain.new_child(new_dict)
print(chain['d'])  # 5 (из нового уровня)
