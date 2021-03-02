import random, time, copy

def step(nextCells):
    print("\n\n\n\n\n")

    currentCells = copy.deepcopy(nextCells)

    for x in range(len(nextCells)):
        for y in range(len(nextCells[0])):
            print(currentCells[x][y], end="")
        print()

    for x in range(len(nextCells)):
        for y in range(len(nextCells[0])):
            above = (y - 1) % len(nextCells[0])
            right = (x + 1) % len(nextCells)
            below = (y + 1) % len(nextCells[0]) 
            left = (x - 1) % len(nextCells)

            numN = 0
            if currentCells[x][above] == '#':
                numN += 1
            if currentCells[right][above] == '#':
                numN += 1
            if currentCells[right][y] == '#':
                numN += 1
            if currentCells[right][below] == '#':
                numN += 1
            if currentCells[x][below] == '#':
                numN += 1
            if currentCells[left][below] == '#':
                numN += 1
            if currentCells[left][y] == '#':
                numN += 1
            if currentCells[left][above] == '#':
                numN += 1

            if currentCells[x][y] == '#' and (numN == 2 or numN == 3):
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numN == 3:
                nextCells[x][y] = "#"
            else:
                nextCells[x][y] = " "
            
    time.sleep(0.5)
    step(nextCells)
    
def main():
    print("CONWAYS GAME OF LIFE")
    print("Input the withd and height of the simulation in this format '100 100'")
    size = input().split()

    width = int(size[0])
    height = int(size[1])

    nextCells = []

    for x in range(width):
        column = []
        for y in range(height):
            if random.randint (0,1):
                column.append("#")
            else:
                column.append(" ")
        nextCells.append(column)

    step(nextCells)

if __name__ == "__main__":
    main()