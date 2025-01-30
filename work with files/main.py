# open(path, r or w)

# file = open("text.txt", "r+")

# read readline readlines
#test1 = file.read() # reads all ur file, read(n) read n symbols

# test2 = file.readline()

# test3 = file.readlines()
# file.write("1")
# file.close()

with open('text.txt', 'r+') as f:
    f.read()
    f.write('Hello World')

