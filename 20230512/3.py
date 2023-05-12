number = 0

while number <= 100:
    new = float(input("tell me a number "))
    number = number + new
    print(number)

# Or...
#
# number = 0
#
# while number <= 100:
#     number += int(input("tell me a number "))
#     print(number)

# Or....
#
# number = 0
#
# while True:
#     number += int(input("tell me a number "))
#     print(number)
#     if number > 100:
#         break
