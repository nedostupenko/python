with open('data3.txt', 'r') as f:
    sym = 0
    for ind, line in enumerate(f, 1):
        line = line.split(' ')
        if float(line[1]) < 20000.00:
             print('Emploee with less than 20000: ', line[0])
        sym += float(line[1])
    mid_sum = sym / ind
    print('Middle payment: ', mid_sum)