#board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


 
""" print("  +---+---+---+")
print(str(2) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
print("  +---+---+---+")
print(str(1) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
print("  +---+---+---+")
print(str(0) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
print("  +---+---+---+")
print("    0   1   2 ") """

player = "o"
win = False

for _ in range(9):
    

    #print board
    print("  +---+---+---+")
    print(str(2) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")
    print(str(1) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(0) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2 ")

    if win == True:
        break

    #Choose next player
    if player == "x":
        player = "o"
    else:
        player = "x"
    

    #user input
    print("Player " +player + " plays! ")

    while True:
        row = int(input("Give me the row: "))
        col = int(input("Give me the column: "))
        if row < 0 or row > 2:
            print("Row out of bounds (0-2) ")
            continue
        if col < 0 or col > 2:
            print("Column is out of bounds (0-2) ")
            continue
        elif board[row][col] != " ":
            print("Pick an empty box")
            continue
        else:
            break
        
    board[row][col] = player 

    if _ > 3:
        #Check if win in row
        for row in range(3):
            cnt = 0
            for col in range(3):
                if board[row][col] == player:
                    cnt +=1
            if cnt == 3:
                print("Player " + player + " Wins! ")
                win = True
                break
        
        #Check if win in column
        for col in range(3):
            cnt = 0
            for row in range(3):
                if board[row][col] == player:
                    cnt +=1
            if cnt == 3:
                print("Player " + player + " Wins! ")
                win = True
                break
        
        #Check if win in main diagonal
        cnt = 0
        for row in range(3):
            for col in range(3):
                if row == col :
                    if board[row][col] == player:
                        cnt +=1
            if cnt == 3:
                print("Player " + player + " Wins! ")
                win = True
                break

        #Check if win in secondary diagonal
        cnt = 0
        for row in range(3):
            for col in range(3):
                if row + col == 2 :
                    if board[row][col] == player:
                        cnt +=1
            if cnt == 3:
                print("Player " + player + " Wins! ")
                win = True
                break


else:
    print("Draw")