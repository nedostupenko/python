pribil = int(input("введите значение выручки: "))
ubil = int(input("введите значение издержек: "))
if pribil > ubil:
    print("фирма работает на прибыль")
    print("Рентабельность выручки = ", pribil / (pribil - ubil))
    employe = int(input("Введите число сотрудников: "))
    print("Прибыль на одного сотрудника: ", pribil / employe)
else:
    print("фирма убыточна")
