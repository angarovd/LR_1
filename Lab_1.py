from random import randint, choice, shuffle  # Для генерации случайного списка
from statistics import median  # Для поиска медианы
from string import punctuation, ascii_lowercase, ascii_uppercase, digits  # Для создания пароля

print('Task 1')
my_set = set(range(1, 11)) # Создание множества
print('Created set: ' + str(my_set) + '\n')  

print('Task 2')
my_list = [i ** 2 for i in range(0, 11)]  # Создание списка для последующего заполнения кортежа
print('My list: ' + str(my_list))
my_tuple = tuple([j for j in my_list])  # Заполнение
my_list.clear()  # Очистка списка
print('My tuple: ' + str(my_tuple))
print('My list: ' + str(my_list)+'\n')

print('Task 3')
my_list = [i + 5 for i in range(1, 11)]  # Заполняем новый список (генераторным методом)
print('List: ' + str (my_list))
print ('Set: ' + str (my_set))
my_dict = dict(zip(my_set, my_list)) 
print('My dictionary: ' + str (my_dict)+'\n') 
# my_dict = dict ()# Создаём пустой словарь
# i = 0  # Инкремент для перебора
# for j in my_set:
#     my_dict[j] = my_list[i]  # Создаём пару "элемент множества" - "элемент списка" и записываем её в словарь
#     i = i + 1


print('Task 4')
new_list = list()
for i in range(0, 10):
    new_list.append(randint(-10, 100))  # Заполняем список случайными числами
print('New list: ' + str (new_list))
even_num = 0
uneven_num = 0  # В эти переменные записываем числа чётных и нечётных элементов
for j in new_list:  # Считаем количество чётных и нечётных чисел
    if j != 0 and j % 2 == 0:
        even_num += 1
    elif j != 0:
        uneven_num += 1
print('Number of even elements: ' + str(even_num))
print('Number of uneven elements: ' + str (uneven_num)+'\n')

print('Task 5')
def task5(task5_dict: dict):  # Функция ожидает на вход тип данных - словарь. 
    for key in task5_dict.keys():  # Проверка словаря на соответствие условиям
        if not isinstance(key, int):
            return 'Ключи в словаре должны быть int'
    for elem in task5_dict.values():
        if not isinstance(elem, str):
            return 'Элементы в словаре должны быть str'
    print('Введённый словарь ' + str (task5_dict))
    keys = task5_dict.keys()  #получаем коллекцию ключей из словаря 
    max_key = max(keys)
    min_key = min(keys)  # Ищем наибольшее и наименьшее значения
    print('Наименьший ключ в словаре: ' + str (min_key) + '\n' + 'Наибольший ключ в словаре: ' + str (max_key))
    mid = (max_key + min_key) / 2  # Ищем среднее
    print('Среднее: ' + str (mid))
    elem_to_del = list(filter(lambda a: a if a >= mid else None, task5_dict.keys()))  # Фильтрация словаря
    for elem in elem_to_del:
        del task5_dict[elem]
    print('Полученный словарь: ' + str (task5_dict))
    return task5_dict

my_dict = {1: '1', 2: '2', 15: '15'} # Исходный словарь, подаваемый на вход
my_new_dict = task5(my_dict)  # Выполняем функцию, получаем новый словарь
print(my_new_dict, '\n')

print('Task 6')
def task6(width: list, length: list):
    set_of_square = set()  # Считаем площади
    for i in range(len(length)): 
        set_of_square.add(width[i] * length[i])
    med = median(set_of_square)  # Медиана
    print('Множество посчитанных площадей: ' + str (set_of_square) + '\n' + 'Медиана: ' + str (med))
    filtered_squares = list(filter(lambda a: a if a >= med else None, set_of_square))
    print('Отфильтрованный список: ' + str (filtered_squares))
    final = sum(filtered_squares) / len(width)
    print('Финальный результат: ' + str (final) + '\n')
    return final

z = task6([2, 4, 6, 7], [1, 10, 12, 13])

print('Task 7')
def task7(length: int, uppercase_num: int, special_symbols_num: int):
    if length < uppercase_num + special_symbols_num:
        return 'Такой пароль невозможно сгенерировать'
    specials = []  # Специальные символы
    upper = []  # прописные буквы
    another = []  # Другие символы (строчные + цифры)
    for i in range(uppercase_num):
        upper.append(choice(ascii_uppercase))  # Выбираем нужное число спец символов (далее аналогично)
    for i in range(special_symbols_num):
        specials.append(choice(punctuation))
    for i in range(length - special_symbols_num - uppercase_num):
        another.append(choice(ascii_lowercase + digits))
    elem_of_password = specials+upper+another  # Список со всеми символами
    shuffle(elem_of_password)  # перемешиваем, чтобы не было последовательностей спец символов и строчных букв
    password = ''
    for j in elem_of_password:
        password += j  # записываем пароль в строку
    return password

a = int(input('Введите требуемое количество символов в пароле: '))
b = int(input('Введите количество прописных (заглавных) букв: '))
c = int (input('Введите количество специальных символов: '))
print(task7(a, b, c))
