f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
# data = f2.read()
# print(data)
print(f2.read())
f2.close()
