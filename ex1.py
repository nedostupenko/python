from sys import argv

zarplata, time, time_set, bonus = argv

def payment():
    a = (int(time) * int(time_set) + int(bonus))
    return a
pay = payment()

print('Имя скрипта: ', zarplata)
print('Выработка, в часах: ',time)
print('Ставка в час: ',time_set)
print('Премия: ',bonus)
print('Зарплатное начисление: ',pay)
