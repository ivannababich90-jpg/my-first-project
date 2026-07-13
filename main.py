# Homework 1

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

numbers = [1, 2, 3, 4, 5, 6]
middle = (len(numbers) + 1) // 2

first_list = numbers[:middle]
second_list = numbers[middle:]
result = [first_list, second_list]
print(result)


