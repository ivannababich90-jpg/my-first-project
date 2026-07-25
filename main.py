# Homework 1
import keyword

# print("Hello World")

# Homework 2

# 1.the square of a number

# print ( 5 ** 2 )

# 2. the average of three number

# number1 = 2
# number2 = 4
# number3 = 6
# print((number1 + number2 + number3)/ 3)

# 3. converting of minutes into hours

# minutes = 135
# hours = minutes // 60
# remaining_minutes = minutes % 60
# print(hours, "hours", remaining_minutes, "minutes")

# 4. discount calculation

# price = 1000
# discount = 15
# final_price = (price * discount / 100)
# final_price = price - (price * discount / 100)
# print(int(final_price))

# 5. find the last digit of number

# number = 347
# last_digit = number % 10
# print("last digit", last_digit)

# 6. calculate the perimeter of rectangle

# length = 5
# width = 3
# perimeter = 2 * (length * width)
# print("perimeter", perimeter)

# 7. print the digits of number vertically

# number4 = 1234
# digit1 = number4 // 1000
# digit2 = number4 // 100 % 10
# digit3 = number4 // 10 % 10
# digit4 = number4 % 10
# print(digit1)
# print(digit2)
# print(digit3)
# print(digit4)


# number4 = ("1234")
# print(number4[0])
# print(number4[1])
# print(number4[2])
# print(number4[3])

# Homework 3.1

# number5 = 3
# number6 = 9

# number5 = 3
# number6 = 9
# operation = "+"
# if operation == "+":
#    print(number5 + number6)

# number5 = 3
# number6 = 9
# operation = "-"
# if operation == "-":
#    print(number6 - number5)

# number5 = 3
# number6 = 9
# operation = "*"
# if operation == "*":
#    print(number6 * number5)

# number5 = 3
# number6 = 9
# operation = "/"
# if operation == "/":
#    print(int(number6 / number5))

# Homework 3.2

# numbers = [16, 5, 8, 12, 10]

# if len(numbers) > 1:
#    last_element = numbers.pop()
#    numbers.insert(0, last_element)
#    print(numbers)

# Homework 3.3

# numbers = [1, 2, 3, 4, 5, 6]
# middle = (len(numbers) + 1) // 2
# second_list = numbers[middle:]
# result = [first_list, second_list]
# print(result)

# Homework 4.1

# numbers = [0, 1, 0, 12, 3]
# result = []
# for number in numbers:
#    if number != 0:
#        result.append(number)

#for number in numbers:
#    if number == 0:
#        result.append( number )

#print(result)

#numbers = [1, 0, 13, 0, 0, 0, 5]
#result = []
#for number in numbers:
#    if number != 0:
#        result.append(number)

#for number in numbers:
#    if number == 0:
#        result.append( number )

#print(result)

#numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 0, 96, 0]
#result = []
#for number in numbers:
#    if number != 0:
#        result.append(number)

#for number in numbers:
#    if number == 0:
#        result.append( number )

#print(result)

#Homework 4.2

#numbers = [0, 1, 7, 2, 4, 8]
#if len(numbers) == 0:
#    result = 0
#    print(result)
#else:
#    even_numbers = []
#    for i in range(0, len(numbers), 2):
#        even_numbers.append(numbers[i])
#    total = sum(even_numbers)
#    result = total * numbers[-1]
#    print(f"({ " + ".join(map(str,even_numbers)) }) * {numbers[-1]} = {result}")


#numbers = [0, 1, 7, 2, 4, 8]
#if len(numbers) == 0:
#    result = 0
#else:
#    total = 0
#    for i in range(0, len(numbers), 2):
#        total +=numbers[i]
#    result = total * numbers[-1]
#print(result)

#numbers = [1, 3, 5]
#if len(numbers) == 0:
#    result = 0
#else:
#    total = 0
#    for i in range(0, len(numbers), 2):
#        total +=numbers[i]
#    result = total * numbers[-1]
#print(result)

#numbers = []
#if len(numbers) == 0:
#    print(0)
#else:
#    total = 0
#    for i in range(0, len(numbers), 2):
#        total += numbers[i]
#    result = total * numbers[-1]
#    print(result)

# Homework 4.3

#numbers = [1, 2, 3, 4, 5, 6, 7, 9]
#result = [numbers[0], numbers[2], numbers[-2]]
#print(numbers, "==", result)

#numbers = [1, 1, 2, 1]
#result = [numbers[0], numbers[2], numbers[-2]]
#print(numbers, "==", result)

#numbers = [6, 3, 7]
#result = [numbers[0], numbers[2], numbers[-2]]
#print(numbers, "==", result)

# Homework 5.1

#import string
#import keyword

#name = input()

#result = True

# не може бути порожним
#if name == "":
#    result = False

# не може починатися з цифри
#elif name[0].isdigit():
#    result = False

# не може бути зарезервованим словом
#elif name in keyword.kwlist:
#    result = False

#не може мiстити "__"
#elif "__" in name:
#    result = False

#else:
#    for symbol in name:

# великi лiтери
#        if symbol.isupper():
#            result = False
#            break

# пробiли
#        if symbol == " ":
#            result = False
#            break
# знаки пунктуацii, окрiм "_"
#        if symbol in string.punctuation and symbol != "_":
#            result = False
#            break

#print(result)

# Homework 5.2

#while True:
#    num1 = float(input("Enter a number: "))
#    operator = input("+, -, *, /):")
#    num2 = float(input("Enter a number: "))

#    if operator == "+":
#        result = num1 + num2
#    elif operator == "-":
#        result = num1 - num2
#    elif operator == "*":
#        result = num1 * num2
#    elif operator == "/":
#        if num2 != 0:
#            result = num1 / num2
#        else:
#            result = "деление на ноль не возможно"
#    else:
#        result = "неизвестная опеация"

#    print(result)

#    answer = input("продолжить? *yes/y):")
#    if answer.lower() not in ("Yes", "y"):
#        print("калькулятор завершил работу")
#        break

# Homework 5.3

#import string

#text = input()

# убираем знаки пунктуации
#for symbol in string.punctuation:
#    text = text.replace(symbol, "")

#роздиляемо на слова
#words = text.split()

#каждое слово с большой + соединяем
#hashtag = "#" + "".join(word.capitalize() for word in words)

#обрезаем до 140 символов
#hashtag = hashtag[:140]
#print(hashtag)

# Homework 6.1

#import string
#letters = string.ascii_letters
#user = input("Enter your username-: ")
#start, end = user.split("-")
#start_index = letters.index(start)
#end_index = letters.index(end)

#print(letters[start_index:end_index + 1])

# Homework 6.2
#
#seconds = int(input("Enter the number of seconds: "))
#
#day_seconds = 24 * 60 * 60
#hour_seconds = 60 *60
#minute_seconds = 60
#
#days, rest = divmod(seconds, day_seconds)
#hours, rest = divmod(rest, hour_seconds)
#minutes, seconds = divmod(rest, minute_seconds)
#
# word "день"
#if days % 10 == 1 and days % 100 != 11:
#    day_word = "день"
#elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
#    day_word = "дня"
#else:
#    day_word = "дней"
#
#print(f"{days} {day_word} , {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
#
# Homework 6.3
#
#number = int(input("Enter the number: "))
#while number > 9:
#    product = 1
#    while number > 0:
#        digit = number % 10
#        product *= digit
#        number //= 10
#
#    number = product
#print(number)
#
# Homework 7.1
#
#def say_hi(name,age):
#    return f"Hi. My name is {name} and I am {age} years old"
#assert say_hi("Alex", 32) == "Hi. My name is Alex and I am 32 years old", "Test1"
#assert say_hi("Frank", 68) == "Hi. My name is Frank and I am 68 years old", "Test2"
#
#print("OK")
#
# Homework 7.2
#
#def correct_sentence(text):
#    text = text[0].upper() + text[1:]
#    if not text.endswith("."):
#        text += "."
#    return text
#
#assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
#assert correct_sentence("hello") == "Hello.", 'Test2'
#assert correct_sentence("Greetings, Friends") == "Greetings, Friends.", 'Test3'
#assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
#assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

#print('ОК')

# Homework 7.3

#def second_index(text, some_str) :
#    first = text.find(some_str)
#
#    if first == -1:
#        return None
#
#    second = text.find(some_str, first +1)
#
#    if second == -1:
#        return None
#    return second
#
#assert second_index("sims", "s") == 3, 'Test1'
#assert second_index("find the river", "e") == 12, 'Test2'
#assert second_index("hi", "h") is None, 'Test3'
#assert second_index("Hello, hello", "lo") == 10, 'Test4'
#print('ОК')

# Homework 7.4

#def common_elements():
#
#    list_3 = [i for i in range(100) if i % 3 == 0]
#
#    list_5 = [i for i in range(100) if i % 5 == 0]
#
#    set_3 = set(list_3)
#
#    set_5 = set(list_5)
#
#    return set_3 & set_5
#
#assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
#
#print("OK")






