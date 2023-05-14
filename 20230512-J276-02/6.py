rows = 4
cols = 4

def checkblock(r, c):
    if r < 0 or r > rows:
        print("Hey, the board doesn't have that many rows")
        return "INVALID ROW"

    if c < 0 or c > cols:
        print("Hey, the board doesn't have that many columns")
        return "INVALID COLUMN"

    if gamegrid[r, c] == "A" or gamegrid[r, c] == "B":
        outcome = gamegrid[r, c]
    else:
        outcome = "FREE"
    return outcome
