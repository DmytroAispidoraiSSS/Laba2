# Головний список: 10 int і 10 str
main_list = [5, 2, 9, 4, 7, 8, 1, 6, 3, 10, "banana", "apple", "kiwi", "grape", "orange", "lemon", "pear", "melon", "plum", "peach"]

# Відділяємо числа і строки
int_list = []
str_list = []

for elem in main_list:
    if type(elem) == int:
        int_list.append(elem)
    else:
        str_list.append(elem)

# Сортуємо числа і строки
int_list.sort()
str_list.sort()

# Об'єднуємо у новий список: спочатку числа, потім строки
sorted_list = int_list + str_list

# Знаходимо всі числа, кратні двом
even_list = []
for num in int_list:
    if num % 2 == 0:
        even_list.append(num)

# Створюємо список строк у верхньому регістрі
caps_str_list = []
for s in str_list:
    caps_str_list.append(s.upper())

# Виводимо всі списки з підписами
print("Головний список:", main_list)
print("Відсортований список (int зростання, str від а до я):", sorted_list)
print("Список чисел, кратних двом:", even_list)
print("Список строк у верхньому регістрі:", caps_str_list)
