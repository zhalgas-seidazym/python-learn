import math

try:
    f = open('./../work with files/text.txt', "w")
    f.write("asd")
    raise Exception("Error from Jaga")
except Exception as e:
    print("File not found: ", e)
finally:
    f.close()
    print("File closed")
