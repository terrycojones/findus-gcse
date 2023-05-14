count = 0
over10 = 0

while over10 < 10:
    over10 += 1
    number = float(input("tell me a number: "))

    if number > 50:
        count += 1

print ("you had this many numbers over 50", count)
