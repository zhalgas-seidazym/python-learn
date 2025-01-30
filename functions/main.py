def hello(name = "default"):
    print('Name: ', name)

hello()

def sum(a: int, b: int) -> int:
    return a + b

num = sum(3, 4)
print(num)

def just():
    pass # this is placeholder for just not to get syntax error