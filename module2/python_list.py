list1 = [ 1, 2, 3, 4, 5 ]

list2 = [ 'A', 'B', 'C', 'D', 'E' ]

list3 = [ 'Hello', 1, True, 40.22 ]

list4 = [ 1, [1, 2, 3], 3, 4, 5 ]

print(list1, sep = " ")
list1.append(6)
print(list1, sep = " ")
list1.extend([7, 8, 9])
print(list1, sep = " ")

num = list1.pop()
print(list1, sep = " ")
print(num)
list1.insert(len(list1), num)
print(list1, sep = " ")


for x in list1:
    print('here we go', x)

for idx, i in enumerate(list2):
    print(idx, i)