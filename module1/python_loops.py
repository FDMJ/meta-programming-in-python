for i in range(10):
    print(i)

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake' ]

for item in favorites:
    print(f'I like to eat {item}')


count = 0

while count < len(favorites):
    print('I like this desert', favorites[count])
    count += 1


for idx, item in enumerate(favorites):
    print(idx, item)