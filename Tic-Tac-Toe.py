#the i th element represents row i (indexing from 0)
board_values = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

#to output visual board
#bottom left tile is (0,0) and tiles are indexed from 0 to 2 in the standard cartesian coordinate system
def make_display_board(board_values):
    row2 = "  ------- ------- -------\n |       |       |       |\n2|   {}   |   {}   |   {}   |\n |       |       |       |\n".format(board_values[2][0], board_values[2][1], board_values[2][2])
    row1 = "  ------- ------- -------\n |       |       |       |\n1|   {}   |   {}   |   {}   |\n |       |       |       |\n".format(board_values[1][0], board_values[1][1], board_values[1][2])
    row0 = "  ------- ------- -------\n |       |       |       |\n0|   {}   |   {}   |   {}   |\n |       |       |       |\n  ------- ------- -------\n     0       1       2   ".format(board_values[0][0], board_values[0][1], board_values[0][2])
    display_board = row2+row1+row0
    return display_board

#checks if there is a three in a row on the board for one player resulting in a winner
def three_row(player, board_values):
    #creates array of all possible three in a rows 
    threes=[]
    threes.append(board_values[0])
    threes.append(board_values[1])
    threes.append(board_values[2])
    threes.append([board_values[0][0], board_values[1][0], board_values[2][0]])
    threes.append([board_values[0][1], board_values[1][1], board_values[2][1]])
    threes.append([board_values[0][2], board_values[1][2], board_values[2][2]])
    threes.append([board_values[0][0], board_values[1][1], board_values[2][2]])
    threes.append([board_values[2][0], board_values[1][1], board_values[0][2]])

    three = False
    counter = 0
    #checks if there are any three in a rows
    while three == False and counter<8:
        three = all(element == player for element in threes[counter])
        counter+=1
    return three

       
#shows starting board
print(make_display_board(board_values))

#game state=0 means game is in play
#game state=1 means player 1 has won
#game state=2 means player 2 has won
#game state=3 means game is a tie

#initalise game
print("player 1 will play with x and player 2 will play with o")
game_state = 0
#counting number of p1 moves, if p1 has made 5 moves and there is no winner the board is in a stalemate resulting in a tie
no_p1_moves = 0
while game_state == 0:
    valid1 = False
    while valid1 == False:
        p1_move_x = int(input("enter the x-coordinate of where u wish to place ur x: "))
        p1_move_y = int(input("enter the y-coordinate of where u wish to place ur x: "))
        #checks that player isnt placing in an already occupied square
        if board_values[p1_move_y][p1_move_x] == ' ':
            valid1 = True
            board_values[p1_move_y][p1_move_x] = 'x' 
        else: 
            print("invalid move, can't place over an already occupied sqaure")
    print(make_display_board(board_values))
    #counts p1 move
    no_p1_moves+=1
    #checks if p1 has won or drawn after their last move
    if three_row('x', board_values):
        game_state = 1
        break
    elif no_p1_moves == 5:
        game_state = 3
        break

    valid2 = False
    while valid2 == False:
        p2_move_x = int(input("enter the x-coordinate of where u wish to place ur o: "))
        p2_move_y = int(input("enter the y-coordinate of where u wish to place ur o: "))
        if board_values[p2_move_y][p2_move_x] == ' ':
            valid2 = True
            board_values[p2_move_y][p2_move_x] = 'o'
        else:
            print("invalid move, can't place over an already occupied sqaure")
    print(make_display_board(board_values))
    if three_row('o', board_values):
        game_state = 2
        break

#outputs game result
if game_state == 1:
    print("Player 1 wins!")
elif game_state == 2:
    print("Player 2 wins!")
elif game_state == 3:
    print("Tie")



