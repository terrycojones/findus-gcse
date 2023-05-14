string = "Findus"
print(string[2])

numbers = [4, 5, 6]
print(numbers[2])

numbers = [
    [4, 5, 6],
    [7, 8, 9],
]

print(numbers[1][2])

if numbers[1][2] == 10:
    print("hi")
else:
    print("lo")

numbers[1][2] = 77

print(numbers[1][2])
