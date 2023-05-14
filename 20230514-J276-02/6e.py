allowedCount = 0

while allowedCount < 8:
    height = int(input("What is your height (in cm)? "))

    if height < 140:
        if height < 120:
            print("You are too small!")
        else:
            withAdult = input("Are you with an adult? ")
            if withAdult == "yes":
                print("Have a good time!")
                allowedCount += 1
            else:
                print("You are too small, unless you can find an adult to go with.")
    else:
        print("Have a good time!")
        allowedCount += 1
