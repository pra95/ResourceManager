
f = open('../data_files/availability.txt','r')

for rows in f:
    print('*'+rows[:-1]+'*')
