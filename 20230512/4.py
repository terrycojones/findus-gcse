first = "Computer Science"
second = "is great"

# 4ci: print "great"
print(second[3:])

# 4cii: print "Computer"
print(first[:8])
# Or: print(first.split()[0])

# 4ciii: print "Science is great"
print(first[9:], second)
# Or:
print(first[9:] + " " + second)
