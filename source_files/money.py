f = open('../data_files/money.txt', 'r')


for line in f:
    line = line[:-1]

a = int(line)

a += 1

print(a)