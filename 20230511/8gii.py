def hoursMinsToMins(hours, mins):
    return 60 * hours + mins


hours = int(input("How many hours? "))
mins = int(input("How many mins? "))

finalTotal = hoursMinsToMins(hours, mins)

print(finalTotal)
