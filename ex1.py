try:
    f = open('data.txt', 'x')
    while True:
        line = input('Insert text: ')
        if line == '':
            break
        f.write(line + '\n')

except FileExistsError:
     print( "File is already exist!" )