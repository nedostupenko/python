with open('data2.txt', 'r') as f:
    for ind, line in enumerate(f, 1):
        line = line.split(' ')
        print('In', ind, 'line - ', len(line), 'words')