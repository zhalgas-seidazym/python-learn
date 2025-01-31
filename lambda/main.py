# lambda
funct1 = lambda x, y: x + y
funct2 = lambda x, y: x - y

print(funct1(1, 2))
print(funct2(1, 2))


# map
list1 = ['1', '2', '3']
list2 = list(map(int, list1))

list3 = [1, 2, 3]
list4 = list(map(lambda x: x * 530, list3))
print(list4)

# filter
list4 = ['Max', 'Yan', 'Pik', 'Elek']
list_filter = list(filter(lambda name: len(name) < 4, list4))
print(list_filter)

# zip
listC = [1, 2, 3, 4]
strC = "ABC"
tupleC = (True, False, True, False)

res = list(zip(listC, strC, tupleC))
print(res) #[(1, 'A', True), (2, 'B', False), (3, 'C', True)]

