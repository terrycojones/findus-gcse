while True:
    x = int(input("give an x axis: "))
    y = int(input("give an y axis: "))

    if checkblock(x, y) == "FREE":
        gamegrid[x, y] = "A"
        break
