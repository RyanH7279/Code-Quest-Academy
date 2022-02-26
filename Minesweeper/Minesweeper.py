"""PRogram: Minesweeper.py
Programmer: Ryan"""
testcases = input()
for test in range(int(testcases)):
    input1 = input().split(" ")
    #print(input1)

    table = []
    rows = int(input1[0])
    colums = int(input1[1])
    bombs = int(input1[2])

    for row in range(rows):
        table.append([])
        for colum in range(colums):
            table[row].append(0)

    #print(table)


    for bomb in range(bombs):
        bomb_input = input().split(" ")
        bombx = int(bomb_input[0])
        bomby = int(bomb_input[1])
        table[bombx][bomby] = "*"

    for row in range(rows):
        for colum in range(colums):
            if table[row][colum] != "*":
                try:
                    if row-1 >= 0 and colum-1 >= 0 and table[row-1][colum-1] == "*" and row-1 <= rows and colum-1 <= colums:
                        #print(str(row-1) + " " + str(colum-1) + " has a bomb")
                        table[row][colum] = table[row][colum] + 1
                except:
                    pass
                try:
                    if row-1 >= 0 and colum >= 0 and table[row-1][colum] == "*" and row-1 <= rows and colum <= colums:
                        #print(str(row-1) + " " + str(colum) + " has a bomb")
                        table[row][colum] = table[row][colum] + 1
                except:
                    pass
                try:
                    if row-1 >= 0 and colum+1 >= 0 and table[row-1][colum+1] == "*" and row-1 <= rows and colum+1 <= colums:
                        #print(str(row-1) + " " + str(colum+1) + " has a bomb")
                        table[row][colum] = table[row][colum] + 1
                except:
                    pass

                try:
                    if row >= 0 and colum-1 >= 0 and table[row][colum-1] == "*" and row <= rows and colum-1 <= colums:
                        #print(str(row) + " " + str(colum-1) + " has a bomb")
                        table[row][colum] = table[row][colum] + 1
                except:
                    pass
                try:
                    if row >= 0 and colum+1 >= 0 and table[row][colum+1] == "*" and row <= rows and colum+1 <= colums:
                        #print(str(row) + " " + str(colum+1) + " has a bomb")
                        table[row][colum] = table[row][colum] + 1
                except:
                    pass
                try:
                    if row+1 >= 0 and colum-1 >= 0 and table[row+1][colum-1] == "*" and row+1 <= rows and colum-1 <= colums:
                        #print(str(row+1) + " " + str(colum-1) + " has a bomb")
                        table[row][colum] = table[row][colum] + 1
                except:
                    pass
                try:
                    if row+1 >= 0 and colum >= 0 and table[row+1][colum] == "*" and row+1 <= rows and colum <= colums:
                        #print(str(row+1) + " " + str(colum) + " has a bomb")
                        table[row][colum] = table[row][colum] + 1
                except:
                    pass
                try:
                    if row+1 >= 0 and colum+1 >= 0 and table[row+1][colum+1] == "*" and row+1 <= rows and colum+1 <= colums:
                        #print(str(row+1) + " " + str(colum+1) + " has a bomb")
                        table[row][colum] = table[row][colum] + 1
                except:
                    pass

    for row in table:
        outrow = ""
        for colum in row:
            outrow += str(colum)
        print(outrow)
