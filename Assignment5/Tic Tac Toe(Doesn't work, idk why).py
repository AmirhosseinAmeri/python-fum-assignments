# from pyfiglet import Figlet
# f = Figlet(font='slant')
def show():
    for row in game_board:
        for cell in row:
            print(cell,end="")
        print()
    for i in range(3):
        if (game_board[i][0]==game_board[i][1]==game_board[i][2])and game_board[i][0]!="-":
            print("Player {} won!".format(game_board[i][0]))
            game_board=[["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]
    for j in range(3):
        if game_board[0][j]==game_board[1][j]==game_board[2][j] and game_board[0][j]!="-":
            print("Player {} won!".format(game_board[0][j]))
            game_board=[["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]
    if game_board[0][0]==game_board[1][1]==game_board[2][2] and game_board[0][0]!="-":
            print("Player {} won!".format(game_board[0][0]))
            game_board=[["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]
    if game_board[0][2]==game_board[1][1]==game_board[2][0] and game_board[0][2]!="-":
        print("Player {} won!".format(game_board[0][2]))
        game_board=[["-","-","-"],
                    ["-","-","-"],
                    ["-","-","-"]]
def player_1():
    while True:
        print("Player1")
        while True:
            row = int(input("Enter row: "))
            if 1<=row<=3:
                break
            else:
                print("Please enter a number Between 1_3")
        while True:
            col = int(input("Enter col: "))
            if 1<=col<=3:
                break
            else:
                print("Please enter a number Between 1_3")
        if game_board[row-1][col-1]=="-":
            game_board[row-1][col-1]="x"
            break
        else:
            print("Select another Cell")
    show()
def player_2():
    while True:
        print("Player2")
        while True:
            row = int(input("Enter row: "))
            if 1<=row<=3:
                break
            else:
                print("Please enter a number Between 1_3")
        while True:
            col = int(input("Enter col: "))
            if 1<=col<=3:
                break
            else:
                print("Please enter a number Between 1_3")
        if game_board[row-1][col-1]=="-":
            game_board[row-1][col-1]="o"
            break
        else:
            print("Select another Cell")
    show()   
game_board=[["-","-","-"],["-","-","-"],["-","-","-"]]
show()
# print(f.renderText('Tic Tac Toe'))
while True:
    player_1()
    player_2()
