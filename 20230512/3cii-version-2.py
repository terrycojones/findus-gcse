numbers = []
over10 = 0

# Use abstraction by not worrying about the details of the computation.
maxNumbers = 10
cutoff = 50


# The code below is abstract because it doesn't care about the actual
# number of numbers or what the actual cutoff is.
#
# Use decomposition into three steps.

# First, gather the numbers.
while over10 < maxNumbers:
    over10 += 1
    numbers.append(float(input("tell me a number: ")))


# Second, count how many are over the cutoff.
count = 0
for number in numbers:
    if number > cutoff:
        count += 1

# Print the output.
print ("you had this many numbers over 50", count)
