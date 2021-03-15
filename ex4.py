f1 = open('data4.txt', 'r')
f3 = ['Один', 'Два', 'Три', 'Четыре']
f3.reverse()
try:
    with open('data41.txt', 'x') as f2:
        for line in f1:
            line = line.split(' ')
            print(line)
            line[0] = f3.pop()
            print(line)
            f2.write(str(line) + '\n')

except FileExistsError:
    print('File is already exist')
f1.close()