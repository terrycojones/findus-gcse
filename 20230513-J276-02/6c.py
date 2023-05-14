# A school uses the array to call an attendance register every morning.
# Write an algorithm using iteration to:

# • display the name of each student one at a time from studentnames

# • take as input whether that student is present or absent

# • display the total number of present students and number of absent
# students in a suitable message, after all student names have been
# displayed.

studentnames = ['Rob', 'Anna', 'Huw', 'Emma', 'Patrice', 'Iqbal']

absentCount = 0

for name in studentnames:
    answer = input("Is '" + name + "' present? ")
    if answer == "no":
        absentCount += 1
    elif answer == "yes":
        pass
    else:
        print("Bad input")

print(absentCount, "students were absent, and",
      len(studentnames) - absentCount, "were present.")
