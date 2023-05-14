newstate = input("Enter the new state : ")


if newstate == "on":
    statevalue = 1

elif newstate == "off":
    statevalue = 2

elif newstate == "suspended":
    statevalue = 3

else:
    print("Invalid state")
