int_list = [5, 2, 8, 4, 3, 7, 9, 1, 10, 6]
str_list = ["banana", "apple", "kiwi", "grape", "orange", "lemon", "pear", "melon", "peach", "pineapple"]

int_list.sort()
str_list.sort()

sorted_list = int_list.copy()
sorted_list.extend(str_list)

sort_list = [ ]
for num in int_list:
    if num % 2 == 0:
        sort_list.append(num)

STR_list = [ ]
for x in str_list:
    STR_list.append(x.upper())

print("стрічковий список:", str_list)
print("ціло численний список:", int_list)
print("відсортований список:", sorted_list)
print("список який кратних двом:", sort_list)
print("стрічковий список капсом:", STR_list)

