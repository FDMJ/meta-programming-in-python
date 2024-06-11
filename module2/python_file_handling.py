file = open('E:\\meta\\meta-programming-in-python\\module2\\test.txt', mode = 'r')

data = file.readline()

print(data)

file.close()

# with open('E:\\meta\\meta-programming-in-python\\module2\\test.txt', mode = 'r') as file:
#    data = file.readline()
#    print(data)