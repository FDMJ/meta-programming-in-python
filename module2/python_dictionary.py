sample_dict = { 1: 'Coffee', 2: 'Tea', 3: 'Juice' }

print(sample_dict.keys())

print(sample_dict[1])

sample_dict[2] = 'Mint Tea'

print(sample_dict)

del sample_dict[3]

print(sample_dict)

print(type(sample_dict))

for key, value in sample_dict.items():
    print(key, value)