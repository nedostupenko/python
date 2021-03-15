try:
    with open('data5.txt', 'x') as f:
        f.write('101 202 303 404')
except FileExistsError:
    print('File is already exist')
with open('data5.txt') as f:
    symma = 0
    line = f.read()
    line = line.split()
    for el in line:
        symma += int(el)

    print('Sum of numbers in file', symma)



