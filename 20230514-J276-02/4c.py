goals = [0, 1, 3, 0, 4, 5, 2, 0, 2, 1]

nogoalscount = 0

for index in range(len(goals)):

    if goals[index] == 0:
        nogoalscount += 1

print(nogoalscount)
