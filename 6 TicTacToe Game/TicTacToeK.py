from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe K')
main_icon_ImageTk = PhotoImage(file="tic-tac-toe.png")
root.iconphoto(True, main_icon_ImageTk)
root.geometry('315x360')
root.minsize(315, 360)  
root.geometry("{}x{}+{}+{}".format(315, 360, int((root.winfo_screenwidth() / 2) - (315 / 2)),int((root.winfo_screenheight() / 2) - (360 / 2))))


def disableAllButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#Check to see if someone won
def checkIfWon():
    backgcolor = "blue"
    global winner,AI
    winner = False
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" :
       b1.config(bg=backgcolor)
       b2.config(bg=backgcolor)
       b3.config(bg=backgcolor)
       winner = True
       messagebox.showinfo("Tic Tac Toe", "X Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" :
       b4.config(bg=backgcolor)
       b5.config(bg=backgcolor)
       b6.config(bg=backgcolor)
       winner = True
       messagebox.showinfo("Tic Tac Toe", "X Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" :
       b7.config(bg=backgcolor)
       b8.config(bg=backgcolor)
       b9.config(bg=backgcolor)
       winner = True
       messagebox.showinfo("Tic Tac Toe", "X Wins!\nCongratulations!!!")
       disableAllButtons()
         
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" :
       b1.config(bg=backgcolor)
       b4.config(bg=backgcolor)
       b7.config(bg=backgcolor)
       winner = True
       messagebox.showinfo("Tic Tac Toe", "X Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" :
       b2.config(bg=backgcolor)
       b5.config(bg=backgcolor)
       b8.config(bg=backgcolor)
       winner = True
       messagebox.showinfo("Tic Tac Toe", "X Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" :
       b3.config(bg=backgcolor)
       b6.config(bg=backgcolor)
       b9.config(bg=backgcolor)
       winner = True
       messagebox.showinfo("Tic Tac Toe", "X Wins!\nCongratulations!!!")
       disableAllButtons()
         
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" :
       b1.config(bg=backgcolor)
       b5.config(bg=backgcolor)
       b9.config(bg=backgcolor)
       winner = True
       messagebox.showinfo("Tic Tac Toe", "X Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X" :
       b3.config(bg=backgcolor)
       b5.config(bg=backgcolor)
       b7.config(bg=backgcolor)
       winner = True
       messagebox.showinfo("Tic Tac Toe", "X Wins!\nCongratulations!!!")
       disableAllButtons()

    
    #Check for O Wins:
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" :
       b1.config(bg=backgcolor)
       b2.config(bg=backgcolor)
       b3.config(bg=backgcolor)
       winner = True
       if(AI==1):
           messagebox.showinfo("Tic Tac Toe", "You Lost!!! Computer Won.")
       else:
           messagebox.showinfo("Tic Tac Toe", "O Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" :
       b4.config(bg=backgcolor)
       b5.config(bg=backgcolor)
       b6.config(bg=backgcolor)
       winner = True
       if(AI==1):
           messagebox.showinfo("Tic Tac Toe", "You Lost!!! Computer Won.")
       else:
           messagebox.showinfo("Tic Tac Toe", "O Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" :
       b7.config(bg=backgcolor)
       b8.config(bg=backgcolor)
       b9.config(bg=backgcolor)
       winner = True
       if(AI==1):
           messagebox.showinfo("Tic Tac Toe", "You Lost!!! Computer Won.")
       else:
           messagebox.showinfo("Tic Tac Toe", "O Wins!\nCongratulations!!!")
       disableAllButtons()
         
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" :
       b1.config(bg=backgcolor)
       b4.config(bg=backgcolor)
       b7.config(bg=backgcolor)
       winner = True
       if(AI==1):
           messagebox.showinfo("Tic Tac Toe", "You Lost!!! Computer Won.")
       else:
           messagebox.showinfo("Tic Tac Toe", "O Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" :
       b2.config(bg=backgcolor)
       b5.config(bg=backgcolor)
       b8.config(bg=backgcolor)
       winner = True
       if(AI==1):
           messagebox.showinfo("Tic Tac Toe", "You Lost!!! Computer Won.")
       else:
           messagebox.showinfo("Tic Tac Toe", "O Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" :
       b3.config(bg=backgcolor)
       b6.config(bg=backgcolor)
       b9.config(bg=backgcolor)
       winner = True
       if(AI==1):
           messagebox.showinfo("Tic Tac Toe", "You Lost!!! Computer Won.")
       else:
           messagebox.showinfo("Tic Tac Toe", "O Wins!\nCongratulations!!!")
       disableAllButtons()
         
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" :
       b1.config(bg=backgcolor)
       b5.config(bg=backgcolor)
       b9.config(bg=backgcolor)
       winner = True
       if(AI==1):
           messagebox.showinfo("Tic Tac Toe", "You Lost!!! Computer Won.")
       else:
           messagebox.showinfo("Tic Tac Toe", "O Wins!\nCongratulations!!!")
       disableAllButtons()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O" :
       b3.config(bg=backgcolor)
       b5.config(bg=backgcolor)
       b7.config(bg=backgcolor)
       winner = True
       if(AI==1):
           messagebox.showinfo("Tic Tac Toe", "You Lost!!! Computer Won.")
       else:
           messagebox.showinfo("Tic Tac Toe", "O Wins!\nCongratulations!!!")
       disableAllButtons()

    #Check if tie:
    if count == 9 and winner == False:
       messagebox.showinfo("Tic Tac Toe", "It's a Tie!\nNo one Wins!")
       disableAllButtons()


from MiniMaxAlgo import BestRowPlusCol
def findBestRowAndColumn():
    board_grid= []
    row1 = []
    row1.append(b1["text"])
    row1.append(b2["text"])
    row1.append(b3["text"])
    board_grid.append(row1)

    row2 = []
    row2.append(b4["text"])
    row2.append(b5["text"])
    row2.append(b6["text"])
    board_grid.append(row2)

    row3 = []
    row3.append(b7["text"])
    row3.append(b8["text"])
    row3.append(b9["text"])
    board_grid.append(row3)

    return BestRowPlusCol(board_grid)
    

def b_click(b):
    global clicked, count, AI

    if b["text"] == " " and clicked==True:
        b["text"] = "X"

        if AI==1:
            num = findBestRowAndColumn();
            if num!=0:
                bx = globals()["b"+str(num)]
                bx.config(text="O")
                count+=1
        else:
            clicked = False
        count += 1
        checkIfWon()
    elif b["text"] == " " and clicked==False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkIfWon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick another box...")


global clicked, count, AI
clicked =True   #X begins
count=0
AI=0

    
#start the game over
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9

    #X starts, so true
    global clicked, count
    clicked = True
    count=0
    
    b1 = Button(root, text=" ", font=("helvetica",20), height=3, width=6, bg="white", command= lambda: b_click(b1), relief=SOLID,borderwidth=2)
    b2 = Button(root, text=" ", font=("helvetica",20), height=3, width=6, bg="white", command= lambda: b_click(b2), relief=SOLID,borderwidth=2)
    b3 = Button(root, text=" ", font=("helvetica",20), height=3, width=6, bg="white", command= lambda: b_click(b3), relief=SOLID,borderwidth=2)
    b4 = Button(root, text=" ", font=("helvetica",20), height=3, width=6, bg="white", command= lambda: b_click(b4), relief=SOLID,borderwidth=2)
    b5 = Button(root, text=" ", font=("helvetica",20), height=3, width=6, bg="white", command= lambda: b_click(b5), relief=SOLID,borderwidth=2)
    b6 = Button(root, text=" ", font=("helvetica",20), height=3, width=6, bg="white", command= lambda: b_click(b6), relief=SOLID,borderwidth=2)
    b7 = Button(root, text=" ", font=("helvetica",20), height=3, width=6, bg="white", command= lambda: b_click(b7), relief=SOLID,borderwidth=2)
    b8 = Button(root, text=" ", font=("helvetica",20), height=3, width=6, bg="white", command= lambda: b_click(b8), relief=SOLID,borderwidth=2)
    b9 = Button(root, text=" ", font=("helvetica",20), height=3, width=6, bg="white", command= lambda: b_click(b9), relief=SOLID,borderwidth=2)

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)



def oneplayer():
    try:
        global clicked, count, AI

        if count!=0:
            raise TypeError("Please Complete or Reset")
        
        messagebox.showinfo("Tic Tac Toe", "You are X. The Computer is O")
        my_menu.delete("2 Players")
        my_menu.add_cascade(label="1 Player", menu=player_menu)

        clicked = True
        count=0
        AI=1

    except TypeError:
        messagebox.showerror("Tic Tac Toe", "Please Complete or Reset this game before changing")
    except:
        messagebox.showerror("Tic Tac Toe", "Hey! It's already 1 Player...")

def twoplayer():
    try:
        global clicked, count, AI
        if count!=0:
            raise TypeError("Please Complete or Reset")
        
        my_menu.delete("1 Player")
        my_menu.add_cascade(label="2 Players", menu=player_menu)

        clicked = True
        count=0
        AI=0

    except TypeError:
        messagebox.showerror("Tic Tac Toe", "Please Complete or Reset this game before changing")        
    except:
        messagebox.showerror("Tic Tac Toe", "Hey! It's already 2 Players...")
    
#Damn it! I could have just called reset function itself, instead of doing exception handling using TypeError and all
#Leave it...

#Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

player_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="2 Players", menu=player_menu)
player_menu.add_command(label="1 Player (Play with AI)", command=oneplayer)
player_menu.add_command(label="2 Players (Play with your friend)", command=twoplayer)
                    
reset()

root.mainloop()
