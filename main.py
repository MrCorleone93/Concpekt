###
'''
ЗНАЙОМСТВО З ПАЙТОН

Встановлення та налаштування IDE

Створення першої програми

Виведення та форматування даних

Змінні та типи даних

Книги:

1. Марк Лутц «Вивчаємо Python»

2. Ерік Метіз «Вивчаємо Python. Програмування ігор, візуалізація даних, веб-застосунки»

3. Пол Беррі "Вивчаємо програмування на Python"

4. Ел Свейгарт «Автоматизація рутинних завдань за допомогою Python. Практичний посібник для початківців»

5. Майкл Доусон "Програмуємо на Python"

6. Девід Бізлі, Браян К. Джонс «Python. Книга рецептів"

Знайти можна у будь-якому зручному форматі.

Якщо виникають проблеми з інтерпретатором у PyCharm:

https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html
'''

# print("Hello world")
#
# print("Hello world!")
# print()
# print('test')

# print("Hello world", "Text1", "Text2", sep=", ", end=" ")
# print("Hello world")
# print('test')

# однорядковий коментар

'''
три одинарні лапки
багаторядковий
коментар
тут можна писати будь-який текст і він буде проігнорований інтерпретатором
'''

# Ctrl + / -> comment или uncomment

# print("hello11")
# print("hello22")
#
# aljfjklsdfjkvskjfd
# print("qwerty")

####
# escape послідовності
# \n -> перенесення на новий рядок
# print("Hello\n\nworld")
# # \t -> табуляція -> 4 пробіли. (буває в консолі 2 або 8 пробіли)
# print("Hello\n\tworld")
# print("\\ -> дзеркалювання, екранування – якщо необхідно службовий символ зробити друкованим")
# print("Hello\\n\\t\"world\"")
# print("\\\\\\\\\\")
# # print("\n" * 10)

#####
# int -> ціле число 12
# float -> дробове число 12.5
# bool -> логічний тип даних: True False
# str -> рядок - масив (набір) символів

# Змінна - це іменована область оперативної пам'яті значення можна змінювати
# number: int = 10
# print(number)
# print(type(number))
# number = 20.5
# print(number)
# print(type(number))
# number = "Vasya"
# print(number)
# print(type(number))
# number = True
# print(number)
# print(type(number))

# = оператор присвоєння
# userName1 = "Vasya"
# print(userName1)
# user_name = "Petya"
# print(user_name)
###

# input -> буде очікувати на введення даних з клавіатури в консолі і поверне за замовчуванням значення типу даних str
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# # # v1
# # print("Name: ", name, " Age: ", age)
# # # v2 конкатенація - складання рядків. Рядок + рядок -> один великий рядок
# # print("Name: " + name + " Age: " + str(age))
# # # print("Name: " + name + " Age: " + age, 1234, "qwehbkqwer" + "sdbhdvsfkjhbdsvafbk")
# # # v3 інтерполяція рядка - вбудовування змінних у рядок завдяки функції format (вивчимо докладніше пізніше)
# print(f"Name: {name} age: {age}")
# #
# # print(int(age) + 10)

###########
################################################################
# + - * /
# print(2 + 3)
# print(2 - 3)
# print(2 * 3)
# print(2 / 3)
# print(2 ** 3)  # основа ** показник (зведення в ступінь
# print(2 // 3)  # ціла частина від розподілу
# print(2 % 3)  # залишок від ділення

# num1 = 15
# num2 = 8
# print(num1 // num2)
# print(num1 % num2)
# print(num1 / num2)

############
# ввести з клавіатури тризначне число та вивести суму цифр цього числа
# // %
# int() - так як input поверне str, нам потрібно цей рядок привести до типу int (ціле число)
# щоб можна було застосовувати арифметичні оператори
# number = int(input("Enter 3-digit number: "))
# # 146
# n1 = number // 100
# # v1
# n2 = number // 10 % 10
# # v2
# # n2 = number % 100 // 10
# n3 = number % 10
#
# result = n1 + n2 + n3
# print(f"n1: {n1} n2: {n2} n3 {n3}")
# print(f"Result: {result}")

# number = 10
# print(number)

#######################################################################################################################

'''
>>> 2. Git, умовні конструкції <<<

1. Git та Git flow

2. Умовні оператори

3. Умовні конструкції

Завантажити та встановити:

https://git-scm.com/downloads

Windows: http://gitextensions.github.io/

Windows/Mac: https://www.sourcetreeapp.com/ чи https://desktop.github.com/ чи https://www.gitkraken.com/jc

Туторіали:

https://www.w3schools.com/git/

https://www.atlassian.com/git/tutorials

https://githowto.com/setup

https://www.tutorialspoint.com/git/index.htm

https://opensource.com/article/18/1/step-step-guide-git

https://github.com/git-guides/install-git

https://www.atlassian.com/git/tutorials/install-git

# # Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел.
# # Результат вычислений вывести на экран.
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# print(num1 * num2 * num3)
#
# #  Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его диагоналей.
# first = int(input("Enter first diagonal: "))
# second = int(input("Enter second diagonal: "))
#
# result = first * second / 2
#
# print(result)
#
# # Пользователь вводит с клавиатуры число, состоящее из четырех цифр. Требуется найти произведение цифр.
# #
# # Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4 = 24.
#
# number = int(input("Enter 4-digit number: "))
# #
# # # 4697
# n1 = number // 1000
# n2 = number // 100 % 10
#

# print("Hello world!")

#####
# умови
# v1
# n1 = 10
# n2 = 20
# v2
# n1, n2 = 10, 20  # множинне привласнення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)  # поверне True якщо обидва операнди рівні (однакові)
# print(n1 != n2)  # поверне True якщо обидва операнди різні
# #
# print(1 == 1 and 3 == 3)  # поверне True якщо обидва операнди рівні True, інакше False
# print(1 == 1 or 2 == 3)  # поверне True якщо хоча б один операнд дорівнює True, інакше False
# #
# is_valid = False
# print(is_valid)
# print(not is_valid)  # not -> інверсія, якщо значення False стане True, і навпаки
#
# print("hello" in "hello world")

############
# hours = int(input("Enter hours: "))
#
# if 12 <= hours < 24:
#     print("PM")
# elif 0 <= hours < 12:
#     print("AM")
# else:
#     print("Incorrect hours!")

# ввести рейтинг фільму: якщо рейтинг дорівнює 5 або 4 - ок, інакше - погано

###
# film_rating = int(input("Enter film rating: "))
#
# if film_rating > 0 and film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("OK!")
#     else:
#         print("Not OK!")
# else:
#     print("Incorrect rating!")
#
# print("Hello world!")

# 1. create develop branch from master branch
# 2. create feature branch from develop branch
# 3.

###
# ввести з клавіатури 3 числа
# - вивести найменше із трьох чисел
# - количество однакових чисел

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))
# #
# # # вывести наименьшее из трех чисел
# # if n1 < n2 < n3:
# #     print(n1)
# # elif n2 < n3 < n1:
# #     print(n2)
# # elif n3 < n2 < n1:
# #     print(n3)
# # else:
# #     print("All numbers equals")
#
# ########
#
# # - кол-во одинаковых чисел
# if n1 == n2 == n3:
#     print(3)
# elif n1 == n2 or n2 == n3 or n1 == n3:
#     print(2)
# else:
#     print(0)
'''
######################################################################################################################

'''
>>> 3. Винятки, цикли, дебаггер <<<

Винятки

Приклади з Винятками

умови

дебаггер

приклади використання

https://www.atlassian.com/ru/git/tutorials/undoing-changes/git-reset

https://stackoverflow.com/questions/21756614/difference-between-git-merge-origin-master-and-git-pull

https://www.jetbrains.com/help/pycharm/resolving-conflicts.html#distributed-version-control-systems

https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html

https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html

# Обробка винятків

# v1
# n1, n2 = 10, 0  # множинне привласнення
# print(n1 / n2)

# num = float(input("Enter the number: "))
# print(num)
# print(int(num))

# v2
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     result = num1 / num2
#
#     print(f"Result: {result}")
#
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occurred: {error}")
# except ValueError as error:
#     print("Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:  # Exception -> базовий тип виключення пишемо останнім з except
#     print(f"Exception occurred: {error}")
# finally:  # Відпрацьовує завжди. Писати по потребі
#     print("End of calculation")
#
# print("some text")

# У Python є такі базові типи винятків:
#
# BaseException: базовий тип для всіх вбудованих винятків
#
# Exception: базовий тип, який зазвичай застосовується для створення своїх типів винятків
#
# ArithmeticError: базовий тип для винятків, пов'язаних з арифметичними операціями
# (OverflowError, ZeroDivisionError, FloatingPointError).
#
# BufferError: Виняток, який виникає при неможливості виконати операцію з буфером
#
# LookupError: базовий тип для винятків, які виникають під час звернення до колекцій
# за некоректним ключем або індексом (наприклад, IndexError, KeyError)

# https://docs.python.org/3/library/exceptions.html

# IndexError: виняток виникає, якщо індекс при зверненні до елемента колекції знаходиться поза допустимим діапазоном
#
# KeyError: виникає, якщо у словнику немає ключа, за яким відбувається звернення до елемента словника.
#
# OverflowError: виникає, якщо результат арифметичної операції не може бути представлений поточним
# Чисельним типом (зазвичай типом float).
#
# RecursionError: виникає, якщо перевищено допустиму глибину рекурсії.
#
# TypeError: якщо операція або функція застосовується до значення неприпустимого типу.
#
# ValueError: виникає, якщо операція або функція одержують об'єкт коректного типу з некоректним значенням.
#
# ZeroDivisionError: виникає при розподілі на нуль.
#
# NotImplementedError: тип виключення для вказівки, що якісь методи класу не реалізовані
#
# ModuleNotFoundError: виникає при неможливості знайти модуль при його імпорті директивою import
#
# OSError: тип винятків, які генеруються при виникненні помилок системи (наприклад, неможливо знайти файл,
# пам'ять диска заповнена і т.д.)

###
#try:
#    name = input("Enter you name: ")

#    if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#   else:
#         raise Exception("Please enter a valid name!")  # raise -> згенерувати виняток (кинути виняток)
#except Exception as e:
#     print(f"Error: {e}")

####################
# try:
#     print("1. Start game\n2. Settings\n3. Saved games\n4. Exit")
#     user_select = int(input("Enter menu number: "))
#
#     # v1
#     if user_select == 1:
#         print("Game started")
#     elif user_select == 2:
#         print("Settings opened")
#     elif user_select == 3:
#         print("Saved games opened")
#     elif user_select == 4:
#         print("Exit...")
#     else:
#         print("Incorrect menu item!")
#
#     # v2
#     match user_select:
#         case 1:
#             print("Game started")
#         case 2:
#             print("Settings opened")
#         case 3:
#             print("Saved games opened")
#         case 4:
#             print("Exit...")
#         case _:
#             print("Incorrect menu item!")
#
# except Exception as e:
#     print(f"Error: {e}")

#########
# _ = "Petya"
# print(_)

###########
# print(num := 10)  # моржовый оператор

###########
###
# Цикли
# - while
# - for

# v1
# i = 0
#
# while i < 10:
#     print(i, end=" ")
#     i += 1  # i = i + 1
#
#
# print("\ntest")
#
# v2
# i = 12
#
# while True:
#     print(i)
#     i += 2

# v3
# i = 0
#
# while True:
#
#     if i == 5:
#         print("continue...")
#         i += 1
#         continue  # пропустить подальші дії циклу, але цикл не зупиниться
#
#     if i >= 10:
#         print("break...")
#         break  # цикл зупиниться (повне завершення циклу)
#
#     print(i)
#     i += 1

#############
###
# Користувач вводить з клавіатури числа
# якщо користувач ввів 0 -> припинити введення чисел
# в кінці вивести середню арифметичну числову послідовність

# sum_nums = 0
# count = 0

# try:
#     while True:
#         try:
#             number = int(input("Enter any number or 0 for exit: "))
#
#             if number == 0 and count == 0:
#                 print("Please enter another number!")
#                 continue
#
#             if number == 0:
#                 print("end...")
#                 break
#
#             sum_nums += number  # sum_nums = sum_nums + number
#             count += 1
#         except ValueError as error:
#             print("Enter numbers only!")
#     average = sum_nums / count
#     print(f"Sum: {sum_nums}")
#     print(f"Count: {count}")
#     print(f"Average: {average}")
# except Exception as error:
#     print(error)

'''

#######################################################################################################################

'''
>>> 4. Рядки <<<

Основні можливості рядків

Вбудовані функції

Приклади розв'язання задач з рядками

# for i in range(5):  # 0 ... 4
#     # print("Hello")
#     print(i, end=" ")
#
# print()
# #
# for i in range(2, 5):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
# #
# for i in range(1, 5, 2):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
# #
# start, end = 1, 10
# for i in range(start, end + 1):
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(end, start - 1, -1):
#     # print("Hello")
#     print(i, end=" ")
#
# print()

##
# for i in 1, 3, 5, "sdfgsd", "qwerq":
#     print(i, end=" ")

###
# for _ in range(3):
#     print("Hello")

###
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print()
#
# print()
##
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i * j, end=" ")
#         j += 1
#     print()
#     i += 1

############
# Показати на екран усі прості числа в діапазоні, вказаному користувачем.
#
# Число називається простим, якщо воно ділиться без залишку тільки на себе і на одиницю.
#
# Наприклад, три - це просте число, а чотири - ні.
# try:
#
#     start = int(input("Enter start value: "))
#     end = int(input("Enter end value: "))
#
#     if start > end:
#         start, end = end, start
#
#     # if start > end:
#     #     temp = start
#     #     start = end
#     #     end = temp
#
#     for number in range(start, end + 1):
#         if number < 2:
#             continue
#
#         is_simple = True
#
#         for i in range(2, number):
#             if number % i == 0:
#                 is_simple = False
#                 break
#
#         if is_simple:
#             print(number, end=" ")
#
# except Exception as error:
#     print(error)

#########
##
# message = "hello \"world"
# message_1 = 'hello world'
# print(message)
#
# text = ("hello"
#         "world")
# print(text)
#
# # raw строка
# text = ''
# qwerrty
#     asdfadsvf
#         asdvsvb
# ''
#
# print(text)
#
# # v1
# path = r"C:\Users\admin\PycharmProjects\FastAPI_materials"
# print(path)
# # v2
# path = "C:\\Users\\admin\\PycharmProjects\\FastAPI_materials"
# print(path)
#
# #
# print("hello, \"world\"\n\tfrom program")

# dogs, cats = 12, 15
# result = f"Dogs {dogs} and cats {cats}"
# print(result)
#
# result = "Dogs {} and cats {}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {0}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {1}".format(dogs, cats)
# print(result)


###
# message = "hello world"
# # [] -> індексатори
# # Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси.
# # Індекси рахуються з нуля
# print(message[0])
# print(len(message))  # кількість символів у рядку
# # print(message[len(message)])  # IndexError: string index out of range
# print(message[len(message) - 1])
# print(message[-1])

####
###
# # # string - immutable тип даних, рядок змінити не можна
# name = "Petya"
# print(name)
# # name[1] = "r"  # TypeError: 'str' object does not support item assignment
# user_name = "Vasya"
# name = user_name
# print(name)

####
# v1
# sentence = "Hello, world 123"
# # # for letter in sentence:
# # #     print(letter, end=" ")
# # #
# # # print()
# #
# # # v2
# for i in range(len(sentence)):
#     print(sentence[i], end=" ")

# slices (срезы)
# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])

#
# name = "Vasya"
# surname = "Petrov"
# age = 33
#
# fullname = name + " " + surname + " " + str(age)  # конкатенація (додавання рядків)
# print(fullname)

#
# text = "Hello, world" * 3
# print(text)
#
# print("---" * 10)

# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)
#
# print(ord("A"))
# print(chr(98))

####
# text = "helLo woRlD"

# isalpha(): повертає True, якщо рядок складається лише з алфавітних символів
#
# print(text.isalpha())
#
# # islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі
#
# print(text.islower())
#
# # isupper(): повертає True, якщо всі символи рядка у верхньому регістрі
#
# print(text.isupper())
#
# # isdigit(): повертає True, якщо всі символи рядка - цифри
#
# print(text.isdigit())
#
# # isnumeric(): повертає True, якщо рядок є числом
#
# print(text.isnumeric())
#
# # startswith(str): повертає True, якщо рядок починається з підрядка str
#
# print(text.startswith("helLo"))
#
# # endswith(str): повертає True, якщо рядок закінчується на підрядок str
#
# print(text.endswith("D"))
#
# # lower(): перекладає рядок у нижній регістр
#
# print(text.lower())
#
# # upper(): перекладає рядок у верхній регістр
#
# print(text.upper())
#
# # title(): початкові символи всіх слів у рядку перекладаються у верхній регістр
#
# print(text.title())
#
# # capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка
#
# print(text.capitalize())

# fio = input("Enter fio: ").title()
# print(fio)

#
# lstrip(): видаляє початкові пробіли з рядка
# text = "helLo woRlD"
# print(text)
# print(text.lstrip())
#
# # rstrip(): видаляє кінцеві пробіли з рядка
# print(text)
# print(text.rstrip())
#
# # strip(): видаляє початкові та кінцеві пробіли з рядка
# print(text)
# print(text.strip())
#
# ljust(width): якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли,
# щоб доповнити значення width, а сам рядок вирівнюється по лівому краю
# text = "hello world"
# print(text)
# print(text.ljust(20))
#
# # rjust(width): якщо довжина рядка менша за параметр width, то зліва від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється праворуч
# text = "hello world"
# print(text)
# print(text.rjust(20))
#
# # center(width): якщо довжина рядка менша за параметр width,
# # то ліворуч і праворуч від рядка рівномірно додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по центру
# text = "hello world"
# print(text)
# print(text.center(20))

# find(str[, start [, end]): повертає індекс підрядка у рядку. Якщо підрядок не знайдено, повертається число -1
#  = "hello world"
# print(text.find("hello"))  # 0
# print(text.find("l"))  # 2
# print(text.rfind("l"))  # 9
#
# first_found_index = text.find("l")
# print(text.find("l", first_found_index + 1))
#
# print(text.find("p"))  # -1
#
# # v1
# for i in range(len(text)):
#     if text[i] == "l":
#         print(i)
#
# # v2
# index = 0
#
# for letter in text:
#     if letter == "l":
#         print(index)
#     index += 1

#

# # replace(old, new[, num]): замінює в рядку один підрядок на інший
# text = "hello world hello"
# print(text)
#
# text = text.replace("hello", "goodbye", 1)
# print(text)

###############
# import string
# import random
#
# MIN_PASSWORD_LENGTH = 8
# MAX_PASSWORD_LENGTH = 16
#
# data_for_password = string.digits + string.ascii_letters + string.punctuation
# # print(data_for_password)
#
# new_password = ""
#
# for i in range(MIN_PASSWORD_LENGTH):
#     new_password += random.choice(data_for_password)
#
# print(new_password)

# добавить возможность выбора длины пароля, от 8 до 16 символов,
# если юзер ввел неверную длину - попросить ввести еще раз

# если юзер ввел 'q' or 'Q' - выйти из программы

'''
#######################################################################################################################

'''
>>> 5. Списки <<<

Основні функції та можливості списків

Приклади використання

# list
# numbers = []
# numbers_1 = list()
# print(type(numbers))
# print(type(numbers_1))

# numbers = [1, 3, 25, 7, 2, 7]
#
# print(numbers)
# print(numbers[0])

# numbers[1] = 11111
# print(numbers)
# print(len(numbers))
# print(numbers[-1])

# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
# print()
#
# for number in numbers:
#     print(number, end=" ")
#
# print()

# #
# values = ["one", 12, 12.4, True]
# print(values)
#
# #
# nums = [1, 3] * 5
# print(nums)
#
# #
# numbers = [1, 3, 25, 7, 2, 7]
#
# print(numbers[:])
# print(numbers[1:5])
# print(numbers[1:5:2])
# print(numbers[::-1])

# Розкладання списку (декомпозиція)
# users = ["Vasya", "Petya"]
# user_1, user_2 = users
# print(user_1)
# print(user_2)
# print(users)

####
#
# import random
#
# # print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
# #
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
# # #
# print(numbers)
# # # # append(item): додає елемент item до кінця списку
# # #
# numbers.append(2222)
# print(numbers)
# # #
# # # # insert(index, item): додає елемент item до списку за індексом index
# # #
# numbers.insert(1, 3333)
# print(numbers)
# # #
# # # # extend(items): додає набір елементів items до кінця списку
# # #
# numbers.extend([2, 3, 4])
# print(numbers)
# # #
# numbers += [1, 2, 3, 4]  # numbers = numbers + [1, 2, 3, 4]
# print(numbers)
# # #
# # # # remove(item):видаляє елемент item. Видаляється лише перше входження елемента.
# # # # Якщо елемент не знайдено, генерує виняток ValueError
# # #
# numbers.remove(2222)
# print(numbers)
# #
# # clear(): видалення всіх елементів зі списку
#
# numbers.clear()
# print(numbers)
#
# del numbers
# print(numbers)
#
# # index(item): повертає індекс елемента item. Якщо елемент не знайдено, генерує виняток ValueError
#
# print(numbers.index(2))
#
# # pop([index]): видаляє та повертає елемент за індексом index.
# # Якщо індекс не передано, просто видаляє останній елемент.
#
# result = numbers.pop(0)
# print(result)
# print(numbers)
# # #
# print(numbers.pop())
# print(numbers)
# #
# # # count(item): повертає кількість входжень елемента item до списку
# #
# print(numbers.count(3))

# sort([key]): Сортує елементи. За умовчанням сортує за зростанням.
# Але за допомогою key ми можемо передати функцію сортування.
# sorted(list, [key]): повертає відсортований список

# v1
# numbers.sort()
# print(numbers)
# v2
# numbers_sorted = sorted(numbers)
# print(numbers_sorted)
# print(numbers)

# people = ["Tom", "bob", "alice", "Sam", "Bill"]
# v1
# people.sort()
# print(people)
# v2
# people.sort(key=str.lower)
# print(people)
# ##
# people_sorted = sorted(people, key=str.lower)
# print(people_sorted)
# print(people)

# # reverse(): розставляє всі елементи у списку у зворотному порядку
#
# numbers.reverse()
# print(numbers)
#
# # copy(): копіює список
#
# nums_1 = [1, 3, 5]
# nums_copy = nums_1.copy()
# print(nums_1)
# print(nums_copy)
# nums_copy[1] = 1111
# print(nums_1)
# print(nums_copy)
#
# # Крім того, Python надає ряд вбудованих функцій для роботи зі списками:
# #
# # len(list): повертає довжину списку
#
# print(len(numbers))
#
# # min(list): повертає найменший елемент списку
#
# print(min(numbers))
#
# # max(list): повертає найбільший елемент списку
#
# print(max(numbers))
#
# users = ["Vasya", "Petya"]
# print(max(users))
# #
# letters = ["ab", "ac"]
# print(max(letters))

###############
# text = "hello world. goodbye world."
# search_item = ". "
#
# sentences = text.split(search_item)
# print(sentences)
# #
# result = []
#
# for sentence in sentences:
#     result.append(sentence.capitalize())
#
# print(result)
# #
# result_sentence = search_item.join(result)
# print(result_sentence)

##
# створити список із 10 випадкових чисел
# поміняти місцями мінімальне значення з максимальним
# [3, 1, 4, 2, 5] -> [3, 5, 4, 2, 1]
# pep

# import random
#
# NUMS_SIZE = 10
# MIN_NUMBER = 1
# MAX_NUMBER = 10

# v1
# numbers = []

# for _ in range(NUMS_SIZE):
#     numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))

# print(numbers)

# min_number = min(numbers)
# max_number = max(numbers)
# min_number_index = numbers.index(min_number)
# max_number_index = numbers.index(max_number)
#
# numbers[min_number_index] = max_number
# numbers[max_number_index] = min_number

# v2
# numbers = [3, 1, 4, 2, 5]
# numbers_copy = numbers.copy()
# print(numbers)
# numbers_copy[numbers.index(min(numbers))], numbers_copy[numbers.index(max(numbers))] = max(numbers), min(numbers)
# numbers = numbers_copy.copy()
# print(numbers)

####
###############
# numbers = ["Vasya", 33, ["dance", "walk"]]
# print(numbers)
# print(numbers[2])
# print(numbers[2][0])

##
# v1
# array = [
#     [1, 3, 2],
#     [1, 4],
#     1,
#     [
#         [1, 2],
#         [3, 5]
#     ]
# ]
# print(array[3][1][1])
# print(array[3][0][0])

# v2
# matrix = [
#     [24, 41, 15, 62],
#     [22, 41, 15, 62],
#     [25, 42, 11, 66],
#     [27, 46, 16, 63]
# ]

# print(matrix[0][1])
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()
#
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()

#
# import random
#
# matrix = []
#
# print(matrix)
#
# for i in range(10):
#     matrix.append([])
#     for j in range(10):
#         matrix[i].append(random.randint(10, 99))
#
# print(matrix)
# #
# # # v1
# # print(len(matrix))
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
#
# print()
# # # v2
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

####
# import random
#
# words = ["Cat", "Apple", "Dog", "Letter", "Helicopter", "fly"]
#
# secret_word = words[random.randint(0, len(words) - 1)]
# # print(secret_word)
#
# user_word = ["_"] * len(secret_word)
# # print(user_word)
# # print(" ".join(user_word))
# attempts = 0

# while True:
#     if "".join(user_word).find("_") == -1:
#         print(f"\nYou guessed the word!\nWord: {secret_word}\nAttempts: {attempts}")
#         break
#
#     # if "".join(user_word).lower() == secret_word.lower():
#     #     print(f"\nYou guessed the word!\nWord: {secret_word}\nAttempts: {attempts}")
#     #     break
#
#     print(" ".join(user_word))
#
#     letter = input("Enter letter: ").strip().lower()
#
#     if not letter.isalpha() or len(letter) != 1:
#         print("Please enter only one letter!")
#         continue
#         # или вместо print -> raise Exception("Please enter only one letter!")
#         # но нужно добавить обработку исключений в цикле
#     attempts += 1
#
#     for i in range(len(secret_word)):
#         if letter == secret_word[i].lower():
#             user_word[i] = letter

'''
#######################################################################################################################

'''
>>> 6. Кортежі, Діапазони, Словники, Множини <<<

Додаткові види колекцій Python

Основні функції та можливості колекцій

Внутрішні нюанси колекцій

Приклади використання

Завдання:

множини, списки, рядки:

1. Створити список чисел. Заберіть дублікати значень. Вивести унікальні значення.

2. Дано два списки чисел.

Порахуйте, скільки чисел міститься як у першому списку, і у другому.

3. Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки.

Визначте, скільки різних слів міститься у цьому тексті.

Словом вважається послідовність непробільних символів, що йдуть поспіль, слова розділені одним 
або більшим числом пробілів або символами кінця рядка.

словники:

1. Наведено список країн і міст кожної країни. Для кожного міста вкажіть, в якій країні воно знаходиться.

Приклад результату:

{

"Ukraine": ["Kyiv", "Lviv", "Dnipro"],

"USA": ["Los Angeles", "Las Vegas"]

}

2. Дано два списки однакової довжини. Необхідно створити з них словник таким чином, 
щоб елементи першого списку були ключами, а елементи другого відповідно значеннями нашого словника.

# # Суму елементів, що знаходяться між першим та останнім позитивними елементами.
#
# import random
#
# numbers = [1, 2, 3]
#
# # for _ in range(10):
# #     numbers.append(random.randint(-10, 10))
#
# print(numbers)
#
# first_positive_num_index, last_positive_num_index = 0, 0
#
# is_positive_exists = False
#
# for number in numbers:
#     if number > 0:
#         is_positive_exists = True
#
# if is_positive_exists:
#     for i in range(len(numbers)):
#         if numbers[i] > 0:
#             first_positive_num_index = i
#             break
#
#     for i in range(len(numbers) - 1, -1, -1):
#         if numbers[i] > 0:
#             last_positive_num_index = i
#             break
#
#     print(first_positive_num_index)
#     print(last_positive_num_index)
#
#     if first_positive_num_index == last_positive_num_index 
#       or abs(first_positive_num_index - last_positive_num_index)== 1:
#         print("No numbers in this range!")
#     else:
#         if first_positive_num_index > last_positive_num_index:
#             first_positive_num_index, last_positive_num_index = last_positive_num_index, first_positive_num_index
#
#         numbers_range_sum = 0
#
#         for i in range(first_positive_num_index + 1, last_positive_num_index):
#             numbers_range_sum += numbers[i]
#
#         print(f"Sum: {numbers_range_sum}")
# else:
#     print("No positive numbers in this range!")

################################################

# # 4. Дано рядок. (зробити зрізи)
# text = "qwertyuiopasdfghjkl"
#
# # - Спершу виведіть третій символ цього рядка.
# print(text[2])
# # - У другому рядку виведіть передостанній символ цього рядка.
# print(text[-2])
# # - У третьому рядку виведіть перші п'ять символів цього рядка.
# print(text[:5])
# # - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# print(text[:-2])
# # - У п('ятому рядку виведіть усі символи з парними індексами '
# #       '(вважаючи, що індексація починається з 0, тому символи виводяться з першого).)
# print(text[2::2])
# # - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# print(text[1::2])
# # - У сьомому рядку виведіть усі символи у зворотному порядку.
# print(text[::-1])
# # - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# print(text[-1::-2])
# # - У дев'ятому рядку виведіть довжину цього рядка.
# print(len(text))

################################################

# Кортеж (tuple) – константний (immutable) список
# можна працювати як зі звичайним списком,
# тільки не можна нічого міняти (функції, які змінюють колекцію - відсутні в кортежі)
# crud -> create, read, update, delete (у кортежі можна робити лише read)

# info = ("test1", 123)
# print(info)
# print(type(info))
# #
# info = "test2",
# print(info)
# print(type(info))
# #
# print(info[0])
#
# info[0] = 123  # TypeError: 'tuple' object does not support item assignment

# num = int(input("Enter number: "))
# nums = 12, int(input("Enter number: ")), num
# print(nums)

#####
# import copy
#
# info = ("test1", 123)
# test = copy.deepcopy(info)
# print(test)
#
# info_copy = info
# print(info_copy)
# print(info)
#
# info_list = list(info)
# print(info_list)
# info_list.append(123)
# print(info_list)
# print(info)
# info = tuple(info_list)
# print(info)
# print(info_list)
# print(info[1:3])
# print(info)

###########
# for num in 1, 3, 4, 5, 6, "Hello", 7:
#     print(num)

# for i in range(5):  # 0, 1, 2, 3, 4
#     print(i)

# for _ in range(5):
#     print("Hello")

# таку змінну створювати не можна так як оскільки її складно читати та зрозуміти
# _ = "Vasya"
# print(_)

# print(range(5))
# print(range(1, 5))
# print(range(1, 5, 2))
# result = range(5)
# print(result)
# print(type(result))
#
# numbers = list(range(10))
# print(numbers)
#
# numbers = list(range(3, 10))
# print(numbers)
#
# numbers = list(range(1, 10, 2))
# print(numbers)
#
# numbers = list(range(10, 0, -1))
# print(numbers)
#
# numbers = tuple(range(10, 0, -1))
# print(numbers)
#
# result = sorted(numbers)
# print(result)
# print(numbers)

#############
##
# dict -> словник, колекція key: value

# users = {
#     1: "John",
#     2: "Vasya",
#     3: "Petya",
#     "key1": "some-value",
#     2.4: 123,
#     True: 111,
#     2: "qwerty",  # дублювати ключі не можна!
# }
#
# print(users)
# print(type(users))
# print(users[1])  # [1] -> це не індекс, а key
# print(users["key1"])
# print(users[2.4])
# print(users[True])
# print(users[2])
#
# users_list = [
#     ("+111123455", "Tom"),
#     ("+384767557", "Bob"),
#     ("+958758767", "Alice")
# ]
#
# users_dict = dict(users_list)
# print(users_dict)
#
# users_list = list(users_dict)
# print(users_list)

###########
##
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
#
# print(users["+33333333"])
# users["+33333333"] = "Petya"
# print(users["+33333333"])
#
# users["+4444444"] = "Test"
# print(users["+4444444"])
#
# print(users)
#
# for key in users:
#     print(users[key], end=" ")
#
# print()
# #
# for key in users.keys():
#     print(key, end=" ")
#
# print()
# print(users.keys())
# print(list(users.keys()))
# #
# for value in users.values():
#     print(value, end=" ")
#
# print()
# print(users.values())
#
# print()
# for key, value in users.items():
#     print(f"key: {key} value: {value}")
#
# print()
# print(users.items())

#####
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
#
# # print(users["+33333333"])
# print(users.get("+33333333", "key not exists"))
#
# # del users["+55555555"]
# deleted_value = users.pop("+55555555", "key not exists")
# print(deleted_value)
# print(users)
#
# users.clear()
# print(users)

##
# users_1 = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# #
# users_copy = users_1.copy()
#
# print(users_1)
# print(users_copy)
# users_copy[111] = "qqqqqq"
# print(users_1)
# print(users_copy)
#
# users_2 = {
#     "+11111111": "eeeeeee",
#     "+44444": "qqqqqq",
#     "+12341234": "wwwwwww"
# }
# #
# users_1.update(users_2)
# print(users_1)
# print(users_2)

################
# json
# users = {
#     "Vasya": {
#         "phone": "123123",
#         "email": "qwerty1@gmail.com",
#         "hobbies": ["one", "two", "three"]
#     },
#     "Petya": {
#         "phone": "1345555",
#         "email": "aqwfafdbsdb@gmail.com",
#         "hobby": "uerhukjshbdjbkhdf",
#         "add_data": {
#             1: "test-1",
#             2: "test-2",
#         }
#     }
# }

# print(users["Vasya"]["hobbies"][1])
# print(users["Petya"]["add_data"][2])

##
# v1
# key = input("Enter key: ")
# if key in users:
#     print(users[key])
# else:
#     print("Nothing found!")

# v2
# key = input("Enter key: ").strip().lower()
# for current_key in users.keys():
#     if key == current_key.lower():
#         print(users[current_key])
#         break
# else:
#     print("Nothing found!")

####
# for i in range(5):
#     print(i)
#     if i >= 3:
#         break
# else:
#     print("end")

##############
# # Множини (set) представляють ще один вид набору, який зберігає тільки унікальні елементи.
# Дублікати значень буде видалено.
# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
# print(type(users))
# # #
# people = ["Mike", "Bill", "Ted"]
# users = set(people)
# print(users)
# # # # #
# print(len(users))
# # #
# users.add("Sam")
# print(users)
# # #
# users = {"Tom", "Bob", "Alice"}
# #
# user = "Tom"
# if user in users:
#     users.remove(user)  # якщо немає значення – генерується виняток
# print(users)
# # #
# users = {"Tom", "Bob", "Alice"}
# #
# users.discard("Tim")  # елемент "Tim" відсутній, і метод нічого не робить
# print(users)
# # #
# users.clear()
# print(users)
##
# users = {"Tom", "Bob", "Alice"}
#
# for user in users:
#     print(user)
#
# # copy() копіювання працює так само як і в list, dict і тд
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Tom", "Sam", "Kate", "Bob"}
# #
# # # v1
# users3 = users.intersection(users2)  # перетин множин (що загальне у першої множини з другим)
# # # v2
# # print(users & users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users.intersection_update(users2)  # те саме, тільки результат буде записаний в users
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# #
# # # v1
# users3 = users.difference(users2)  # що є тільки першим і немає у другій множині
# print(users3)  # {"Tom", "Alice"}
# # v2
# print(users - users2)
# #
# users.difference_update(users2)
# print(users)
# print(users2)
# #
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.symmetric_difference(users2)  # унікальні значення першої та другої множин
# print(users3)
#
# # v2
# users4 = users ^ users2

# ##
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issubset(superusers))  # True
# print(superusers.issubset(users))  # False
#
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issuperset(superusers))  # False
# print(superusers.issuperset(users))  # True

#
# # Тип frozen set є видом множин, які не можуть бути змінені (за типом tuple у list)
# users = frozenset({"Tom", "Bob", "Alice"})
# print(users)
# users = set(users)
# print(users)
# # можна використовувати всі функції звичайного set, крім тих, що модифікують значення

#####
# створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
#
# вивести на екран
#
# - вивести суму чисел головної діагоналі матриці
#
# - вивести мінімальне та максимальне значення побічної діагоналі матриці
#
# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
#
# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# (аналогічно зробити з рядком)
#

# import random
#
# matrix = []
# SIZE = 10
#
# for i in range(SIZE):
#     matrix.append([])
#     for j in range(SIZE):
#         matrix[i].append(random.randint(10, 99))
#
#
# for i in range(SIZE):
#     for j in range(SIZE):
#         print(matrix[i][j], end=" ")
#     print()

###
# - вивести суму чисел головної діагоналі матриці
# matrix_main_diagonal_sum = 0
# print()
#
# for i in range(SIZE):
#     matrix_main_diagonal_sum += matrix[i][i]
#     print(matrix[i][i], end=" ")
#
# print()
# print(matrix_main_diagonal_sum)

###
# - вивести мінімальне та максимальне значення побічної діагоналі матриці
# print()
# row_index = 0
# nums = []
# for i in range(SIZE - 1, -1, -1):
#     print(matrix[row_index][i], end=" ")
#     nums.append(matrix[row_index][i])
#     row_index += 1
#
# print(f"\nMin: {min(nums)}\nMax: {max(nums)}")

# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)

# user_row = int(input("Enter row number: "))
#
# if user_row > SIZE or user_row <= 0:
#     print("Invalid row number")
# else:
#     for i in range(SIZE):
#         print(matrix[user_row - 1][i], end=" ")
'''
#######################################################################################################################

'''
>>> 7. Функції 1: види функцій <<<

Основні види функцій

Перевантаження функцій

Приклади використання функцій

# def say_hello():
#     print("Hello")
#
#
# number = 10
# print(number)
# print(say_hello)
# say_hello()  # виклик функції (функція починає працювати)
# say_hello()
#
#
# def say_hello():
#     print("Hello Friends!")
#
#
# say_hello()
#
#
# def say_hello(name):
#     print(f"Hello {name}!")
#     name = "qqqq"
#     print(f"Hello {name}!")
#
#
# say_hello("Test user")
# name = "Anton"
# say_hello(name)
# print(name)


# def say_hello_name(username):
#     print(f"Hello, {username}")
#
#
# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)
# #


# def user_info(name: str, age: int, hobby: str) -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# try:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     user_hobby = input("Enter your hobby: ")
#     user_info(name, age, user_hobby)
# except Exception as e:
#     print(e)

########
#####################
# після того як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція)
# return – поверне результат роботи функції. Після відпрацьовування return - решта дій функції не відпрацюють
# та функція завершить свою роботу. Якщо у функції є цикл - у циклi return працює як break,
# але на відміну від break – поверне результат, а не просто
# Зупинить дії. Якщо функції є цикли, і в одному з циклів спрацював return - функція припинить свою роботу.
# ключове слово return може зустрічатися в тілі функції скільки завгодно разів
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def sub(n1, n2):
#     return n1 - n2
#
#
# def mult(n1, n2):
#     return n1 * n2
#
#
# def division(n1, n2):
#     return n1 / n2
#
#
# def show_result(num1, num2, math_action, math_func) -> None:
#     print(f"{num1} {math_action} {num2} = {math_func(num1, num2)}")
#
#
# def calculate() -> None:
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     math_operation = input("Enter math operation + - * / ")
#
#     match math_operation:
#         case "+":
#             show_result(first_number, second_number, math_operation, add)
#         case "-":
#             show_result(first_number, second_number, math_operation, sub)
#         case "*":
#             show_result(first_number, second_number, math_operation, mult)
#         case "/":
#             show_result(first_number, second_number, math_operation, division)
#         case _:
#             raise Exception("Invalid math operation!")
#
#
# try:
#     calculate()
# except ValueError:
#     print("Enter a valid number!")
# except ZeroDivisionError:
#     print("Do not divide by zero please!")
# except Exception as error:
#     print(error)

###

# def user_info(name: str, age: int = 18, hobby: str = "no hobby") -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# # user_info("Vasya", 33, "test")
# # user_info("Vasya", 33)
# # user_info("Vasya")
#
# # user_info("walking", "Petya", 33)
# user_info(hobby="walking", name="Petya", age=33)

#####
# Усі параметри,
# які розташовуються праворуч від символу *, отримують значення лише на ім'я:

# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Bob", age=41, company="Microsoft")
#
#
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(age=41, name="Bob", company="Microsoft")

# Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією,
# тобто позиційні параметри, можна використовувати символ /: всі параметри, які йдуть до символу / ,
# є позиційними і можуть отримувати значення лише за позицією

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)


# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

####
# 1. Створити список чисел. Заберіть дублікати значень. Вивести унікальні значення.
# import random
#
#
# def create_list_with_random_numbers(list_length=10, start_number=1, end_number=10) -> list:
#     # v1
#     # new_list = list()
#     # for _ in range(list_length):
#     #     new_list.append(random.randint(start_number, end_number))
#     # return new_list
#
#     # v2
#     return [random.randint(start_number, end_number) for _ in range(list_length)]
#
#
# def remove_duplicates(list_to_remove) -> list:
#     return list(set(list_to_remove))
#
#
# def get_unique_values(list_numbers) -> list:
#     unique_values = []
#     for number in list_numbers:
#         if list_numbers.count(number) == 1:
#             unique_values.append(number)
#
#     return unique_values


# numbers = create_list_with_random_numbers()
# print(numbers)
# numbers_without_duplicates = remove_duplicates(numbers)
# print(numbers_without_duplicates)
# unique_numbers = get_unique_values(numbers)
# print(unique_numbers)

# 2. Дано два списки чисел.
# Порахуйте, скільки чисел міститься як у першому списку, і у другому.

# numbers_1 = create_list_with_random_numbers(start_number=1, end_number=20)
# numbers_2 = create_list_with_random_numbers(start_number=1, end_number=20)
#
# print(numbers_1)
# print(numbers_2)
#
#
# def calc_number_of_equals_numbers_v1(nums_1: list[int], nums_2: list[int]) -> int:
#     print(set(nums_1).intersection(set(nums_2)))
#     return len(set(nums_1).intersection(set(nums_2)))
#
#
# def calc_number_of_equals_numbers_v2(nums_1: list[int], nums_2: list[int]) -> int:
#     def get_number_of_unique_values(first_nums: list[int], second_nums: list[int]) -> int:
#         counter = 0
#         equals_numbers = []
#         for num in first_nums:
#             if num in second_nums and num not in equals_numbers:
#                 equals_numbers.append(num)
#                 counter += 1
#
#         print(equals_numbers)
#         return counter
#
#     if len(nums_1) < len(nums_2):
#         return get_number_of_unique_values(nums_1, nums_2)
#     else:
#         return get_number_of_unique_values(nums_2, nums_1)
#
#
# print(f"Result: {calc_number_of_equals_numbers_v1(numbers_1, numbers_2)}")
# print(f"Result: {calc_number_of_equals_numbers_v2(numbers_1, numbers_2)}")

###########
# 3. Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки.
#
# Визначте, скільки різних слів міститься у цьому тексті.
#
# Словом вважається послідовність непробільних символів, що йдуть поспіль,
# слова розділені одним або більшим числом пробілів або символами кінця рядка.

# def generate_text(seed="Hello", multiplier=5):
#     return (seed + " ") * multiplier
# 
# 
# def calc_diff_strings(text: str) -> int:
#     print(text)
#     print(text.split())
#     return len(set(text.split()))
# 
# 
# print(calc_diff_strings(generate_text("Hello world", 10)))
# print(calc_diff_strings(generate_text("Hello how are you thank you", 1)))

'''
#######################################################################################################################

'''
>>> 8. Функції 2: область видимості змінних, рекурсія, замикання <<<

Області видимості функцій

Рекурсивні функції

Замикання у функціях

Додаткові приклади з функціями

Додатковi завдання:

Важливо: не використовувати цикли для реалізації основної логіки.

Потрібно використати рекурсію.

Цикл можна використовувати лише у 4 завданні для знаходження суми чисел.

Завдання 1.

Написати рекурсивну функцію знаходження ступеня числа.

Завдання 2.

Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.

Проілюструйте роботу функції прикладом. (Протестувати)

Завдання 3.

Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.

Користувач вводить a та b. Проілюструйте роботу функції прикладом.

Завдання 4.

Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим чином 
і знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.

# import random
#
# numbers = [random.randint(-10, 40) for _ in range(10)]
#
# print(numbers)
#
#
# def is_simple(number: int) -> bool:
#     if number < 2:
#         return False
#
#     for num in range(2, number):
#         if number % num == 0:
#             return False
#
#     return True
#
#
# def get_simple_numbers_from_list(nums: list[int]) -> None:
#     for num in nums:
#         if is_simple(num):
#             print(num, end=" ")
#
#     print()


# get_simple_numbers_from_list(numbers)
#
#
# def get_min_number(nums: list[int]) -> int:
#     if len(nums) == 0:
#         raise Exception("Provide non empty list!")
#
#     return min(nums)
#
#
####################################
# def hello(): print("Hello")
#
#
# print(hello)
# message = hello  # надав посилання на функцію в іншу змінну
# print(message)
#
# hello()
# message()

##################
# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mult(a, b): return a * b
# def division(a, b): return a / b
#
#
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return add
#         case "-":
#             return sub
#         case "*":
#             return mult
#         case "/":
#             return division
#         case _:
#             raise Exception("Invalid operation!")
#
#
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(num1,num2)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)

############
# message = lambda: print("Hello world!")
# message()
#
# ####
# square = lambda side_1, side_2: side_1 * side_2
# print(square(2, 4))

####
# def calculate(a, b, math_operation) -> None:
#     print(f"Result: {math_operation(a, b)}")
#
#
# calculate(2, 5, lambda n1, n2: n1 + n2)
# calculate(2, 5, lambda n1, n2: n1 / n2)

################
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return lambda a, b: a + b  # повернення посилання на функцію
#         case "-":
#             return lambda a, b: a - b
#         case "*":
#             return lambda a, b: a * b
#         case "/":
#             return lambda a, b: a / b
#         case _:
#             raise Exception("Invalid operation!")
#
#
# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 9)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)

#################
# LEGB - почитати
# https://www.bestprog.net/uk/2020/07/29/python-the-scopes-of-names-in-python-local-names-visibility-rules-for-names-legb-rule-the-global-keyword-overriding-names-in-functions-ua/

#####
# області видимості
# number = 10
#
#
# def test() -> None:
#     # number: int = 11  # перекриття глобальної змінної
#
#     if 1:
#         number = 12
#
#         if 1:
#             # number = 13
#             print(number)
#     print(number)
#
#
# print(number)
# test()
# print(number)
# number = 35
# print(number)

###############
# number = 10
#
#
# def test():
#     global number
#     number = 11  # змінюємо значення глобальної змінної
#     print(number)
#
#
# print(number)
# test()
# print(number)

#
#########
# def outer():
#     number = 1
#
#     def inner():
#         nonlocal number
#         number = 2
#         print(number)
#
#     inner()
#     print(number)
#
#
# outer()

#############
###
# number = 10
#
#
# def outer():
#     global number
#     number = 1
#     new_number = number
#
#     def inner():
#         global number
#         nonlocal new_number
#         new_number = 2
#         print(new_number)
#         number = 2
#
#         def inner_number_2():
#             global number
#             nonlocal new_number
#             new_number = 3
#             print(new_number)
#             number = 3
#
#         inner_number_2()
#
#     inner()
#     print(new_number)
#
#
# outer()
# print(number)

#####################
# Замикання (closure) представляє функцію, яка запам'ятовує своє лексичне оточення навіть у тому випадку,
# коли вона виконується поза своєю областю видимості.

# Зовнішня функція, яка визначає деяку область видимості і в якій визначені деякі
# Змінні та параметри - лексичне оточення
#
# Змінні та параметри (лексичне оточення), які визначені у зовнішній функції
#
# вкладена функція, яка використовує змінні та параметри зовнішньої функції

# def outer():
#     number = 10
#     print("outer")
#     test = 10
#     test_2 = 111
#
#     def inner():
#         nonlocal number
#         number += 1
#         # print(test)
#         print(number)
#         # print("hello")
#
#     return inner
#
#
# inner_func = outer()
# inner_func()
# inner_func()
# inner_func()


#####
# v1
# def multiply(num1):
#     def inner(num2): return num1 * num2
#     return inner

# v2
# def multiply(num1): return lambda num2: num1 * num2


# def multiply_v2(num1, num2):
#     return num1 * num2
#
#
# for i in range(1, 10):
#     print(f"{3} * {i} = {multiply_v2(3, i)}")


# number1 = 3
# mult_func = multiply(number1)
# # print(mult_func(4))
# # print(mult_func(5))
# # print(mult_func(7))
# #
# for number2 in range(1, 10):
#     print(f"{number1} * {number2} = {mult_func(number2)}")

# додаткове завдання:
# Вкладені функції, замикання, lambda -> почитати, продебажити та написати конспект

############
# args and kwargs
# упаковка в кортеж
# def example_1(*args, text="hello world"):
#     print(args)
#     print(text)
#
#
# example_1(text="some text")
# example_1(1, 2, 3, 4, 5, 6, 7, 8, 9, text="some text")
#
#
# # распаковка из кортежа
# def sum_numbers(n1, n2, n3, n4):
#     print(n1 + n2 + n3 + n4)
#
#
# numbers = [2, 4, 1, 5]
# sum_numbers(numbers[0], numbers[1], numbers[2], numbers[3])
# sum_numbers(*numbers)
#
#
# # упаковка в словарь
# def example_2(**kwargs):
#     print(kwargs)
#
#
# example_2()
# example_2(name="Vasya", age=33)
#
#
# # распаковка из словаря
# def example_3(name, age):
#     print(name, age)
#
#
# user = {
#     "name": "Petya",
#     "age": 44
# }
#
# example_3(**user)
#
#
# ####
# def show_info(name, age, *args, some_data, **kwargs):
#     print(f"Hello, {name}, your age: {age}")
#     print(some_data)
#     print(args)
#     print(kwargs)
#
#
# show_info("Petya", 33, 1, 2, 3, 4, some_data="data", text1="text1", text2="text2")

##############
#
# Рекурсія – коли функція викликає сама себе
# 1. продумати, яке або які параметри функції будуть змінені при рекурсивному виклику
# 2. визначити умову або умови виходу з рекурсії
# 3. запустити рекурсію (виклик цієї ж функції)

# 5! => 1 * 2 * ... * 5
# def factorial(number):
#     if number <= 1:
#         return 1
#
#     # factorial(number - 1) -> запуск рекурсії
#     return number * factorial(number - 1)
#
#
# print(factorial(5))
# #
# #
# # factorial(5) -> 5 * factorial(4) => 120
# # factorial(4) -> 4 * factorial(3) => 24
# # factorial(3) -> 3 * factorial(2) => 6
# # factorial(2) -> 2 * factorial(1) => 2
# # factorial(1) => 1

################
# Написати рекурсивну функцію знаходження ступеня числа.

# def my_pow(base, exponent):
#     # if exponent <= 1:
#     #     return base
#
#     return base * my_pow(base, exponent - 1)
#
#
# result = my_pow(2, 5)
# print(result)

# my_pow(2, 3) -> 2 * my_pow(2, 2) => 8
# my_pow(2, 2) -> 2 * my_pow(2, 1) => 4
# my_pow(2, 1) => 2

'''
#######################################################################################################################

'''
>>> 9. Сортування, пошук <<<

Вивчення основних алгоритмів сортувань

Алгоритми пошуку: бінарний та лінійний

Приклади використання алгоритмів

Додаткове завдання:

Продебажити алгоритми розглянуті на уроці, написати короткі тези про кожен алгоритм.

Написати гру "Вгадай число" використовуючи бінарний пошук: гравець загадує число, пк відгадує і показує кількість спроб.

Усі результати надсилати мені в особисті повідомлення.

https://flexiple.com/algorithms/big-o-notation-cheat-sheet/

https://www.geeksforgeeks.org/python-program-for-binary-search/

https://pythontutor.com/render.html#mode=edit

# # Напишите рекурсивную функцию, которая принимает одномерный массив из 100 целых чисел заполненных
# # случайным образом и находит позицию, с которой начинается последовательность из 10 чисел, сумма которых минимальна.
#
# import math
# import random
#
#
# def find_min_sum_index(numbers, start_index, end_index, min_sum=math.inf, min_index=0):
#     if end_index < len(numbers):
#         current_sum = sum(numbers[start_index:end_index + 1])
#
#         if current_sum < min_sum:
#             min_sum = current_sum
#             min_index = start_index
#
#         start_index += 1
#         end_index += 1
#
#         print(f"Min sum: {min_sum} Current sum: {current_sum} Index: {min_index}")
#
#         return find_min_sum_index(numbers, start_index, end_index, min_sum, min_index)
#
#     return min_index
#
#
# nums = [random.randint(1, 10) for _ in range(100)]
# print(nums)
# result = find_min_sum_index(nums, 0, 9)
# print(result)

###################
# import random
#
#
# def generate_random_list(list_len, start_value=1, end_value=100):
#     return [random.randint(start_value, end_value) for _ in range(list_len)]
#
#
# def bubble_sort(nums):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 swapped = True
#
#
# def selection_sort(nums):
#     for i in range(len(nums)):
#         lowest_value_index = i
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[lowest_value_index]:
#                 lowest_value_index = j
#         nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#
#
# def insertion_sort(nums):
#     for i in range(1, len(nums)):
#         item_to_insert = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > item_to_insert:
#             nums[j + 1] = nums[j]
#             j -= 1
#         nums[j + 1] = item_to_insert
#
#
# def merge(left_list, right_list):
#     sorted_list = []
#     left_list_index = right_list_index = 0
#     left_list_length, right_list_length = len(left_list), len(right_list)
#
#     for _ in range(left_list_length + right_list_length):
#         if left_list_index < left_list_length and right_list_index < right_list_length:
#             if left_list[left_list_index] <= right_list[right_list_index]:
#                 sorted_list.append(left_list[left_list_index])
#                 left_list_index += 1
#             else:
#                 sorted_list.append(right_list[right_list_index])
#                 right_list_index += 1
#         elif left_list_index == left_list_length:
#             sorted_list.append(right_list[right_list_index])
#             right_list_index += 1
#         elif right_list_index == right_list_length:
#             sorted_list.append(left_list[left_list_index])
#             left_list_index += 1
#
#     return sorted_list
#
#
# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     middle_index = len(nums) // 2
#
#     left_list = merge_sort(nums[:middle_index])
#     right_list = merge_sort(nums[middle_index:])
#
#     return merge(left_list, right_list)
#
#
# numbers = generate_random_list(5, start_value=1, end_value=10)
# print(numbers)
# bubble_sort(numbers)
# selection_sort(numbers)
# insertion_sort(numbers)
# numbers = merge_sort(numbers)
# print(numbers)


#####################
# def linear_search(nums, target) -> int:
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#     return -1  # означает что значение не найдено
#
#
# print(linear_search(numbers, 3))
# print(linear_search(numbers, 4))
# print(linear_search(numbers, 6))
# print(linear_search(numbers, 7))

####################
# бінарний пошук працює ТІЛЬКИ на відсортованому масиві
# def binary_search(nums, search_item) -> int:
#     first_index = 0
#     last_index = len(nums) - 1
#
#     while first_index <= last_index:
#         middle_index = (first_index + last_index) // 2
#         if nums[middle_index] == search_item:
#             return middle_index
#         else:
#             if search_item < nums[middle_index]:
#                 last_index = middle_index - 1
#             else:
#                 first_index = middle_index + 1
#
#     return -1  # -1 означає, що значення не знайдено
#
#
# numbers.sort()
# print(numbers)
# print(binary_search(numbers, 5))
# print(binary_search(numbers, 3))
# print(binary_search(numbers, 1))

'''
#######################################################################################################################