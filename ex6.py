from itertools import count, cycle
my_list = []
for el in count(int(input('Введите начало отсчета от 1 до 10: '))):
    if el > 10:
        break
    else:
        print(el)
        my_list.append(el)

print(my_list)
stop = 0
for el in cycle(my_list):
    if stop > 20:
        break
    print(el)
    stop += 1

