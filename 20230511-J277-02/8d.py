# total = 0
# total = total + minsPlayed[2,0]
# total = total + minsPlayed[2,1]
# total = total + minsPlayed[2,2]
# total = total + minsPlayed[2,3]
# total = total + minsPlayed[2,4]
# print(total)

total = 0

for row in range(5):
    total += minsPlayed[2, row]

print(total)
