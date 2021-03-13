import math

print(math.factorial(4))

def fact():
    from functools import reduce
    n = int(input('Insert number: '))
    my_list = [el for el in range(1, n + 1)]
    result = reduce(lambda a, b: a * b, my_list)
#  не понял суть задания
