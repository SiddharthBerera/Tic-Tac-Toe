import tkinter as tk

window_1 = tk.Tk()
window_1.title("Tic Tac Toe")


#starting player is X
player = "X"
#initilise board for display
board=[[0,0,0],[0,0,0],[0,0,0]]


#outputs the unoccupied sqaures
def available_spots():
    available=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]["text"] == "":
                available.append((i,j))
    return available


#checks the state of the game (someone has won, draw, game still in play)
def check_win():
    #checks if rows have a winning 3
    for i in range(0,3):
        if board[i][0]["text"] == board[i][1]["text"] == board[i][2]["text"] != "":
            return 1

    #checks if columns have a winning 3
    for j in range(0,3):
        if board[0][j]["text"] == board[1][j]["text"] == board[2][j]["text"] != "":
            return 1

    #checks if diagonals have a winning 3
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        return 1
    elif board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        return 1

    #checks if board is full and since there was no winning 3 => a draw
    elif available_spots() == []:
        return 0
    #otherwise game is still in play
    else:
        return -1
        

def main_gameflow(r,c):
    global player
    #they can only place their move on an unoccupied sqaure and if the game is still in play
    if board[r][c]["text"] == "" and check_win() == -1:
        if player == "X":
            board[r][c].config(text="X")
            if check_win() == -1:
                player = "O"
                label_1.config(text=("It's O's turn"))
            elif check_win() == 1:
                label_1.config(text=("X wins"))
            elif check_win() == 0:
                label_1.config(text="Draw")
        elif player == "O":
            board[r][c].config(text="O")
            if check_win() == -1:
                player = "X"
                label_1.config(text=("It's X's turn"))
            elif check_win() == 1:
                label_1.config(text=("O win"))
            elif check_win() == 0:
                label_1.config(text="Draw")


def refresh():
    for i in range(0,3):
        for j in range(0,3):
            board[i][j]["text"] = ""   


#make display
for i in range(0,3):
    for j in range(0,3):
        #makes each of the 9 sqaures in the grid a button 
        board[i][j] = tk.Button(text = "", font = ("normal", 60, "normal"), width = 2, height = 1, command=lambda r=i, c=j: main_gameflow(r,c))
        board[i][j].grid(row = i, column = j)

label_1=tk.Label(text="It's X's Turn", font=("normal",22,"bold"))
label_1.grid(row=3, column =1)

button_1=tk.Button(text="Restart", font=("Courier",18,"normal"), fg="red",command=refresh)
button_1.grid(row=4,column=1)

#display_board()
window_1.mainloop()









