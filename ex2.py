my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
new_list = [el for ind, el in enumerate(my_list) if my_list[ind] > my_list[ind - 1] if ind - 1 != -1]
print(new_list)

