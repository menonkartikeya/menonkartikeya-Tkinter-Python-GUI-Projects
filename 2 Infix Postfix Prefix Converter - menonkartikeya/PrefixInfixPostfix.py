from tkinter import *
from tkinter import ttk, messagebox
import random

from functions import prefixToInfix
from functions import prefixToPostfix
from functions import infixToPrefix
from functions import infixToPostfix
from functions import postfixToPrefix
from functions import postfixToInfix

root = Tk()
root.geometry('600x500')
root.minsize(600, 500)  # min width,height
root.maxsize(600, 500)
root.geometry("{}x{}+{}+{}".format(600, 500, int((root.winfo_screenwidth() / 2) - (600 / 2)),
                                   int((root.winfo_screenheight() / 2) - (500 / 2))))

root.title("Prefix Infix Postfix Converter")
main_icon = PhotoImage(file="calculator3.png")
root.iconphoto(True, main_icon)

root.configure(background="white")

heading1 = Label(root, text=" Prefix-Infix-Postfix Converter\n", font=("Arial Rounded MT Bold", 26), bg='white',
                 fg='black')
heading1.pack()

main_icon = PhotoImage(file='calculator3.png')
main_icon_label = Label(root, image=main_icon, bg='white')
main_icon_label.pack()

global expressionTypeStr
def ExpressionType():
    if (expression_type.get() == 1):
        expressionTypeStr="Prefix"
    elif(expression_type.get() == 2):
        expressionTypeStr="Infix"
    elif(expression_type.get() == 3):
        expressionTypeStr="Postfix"
    else:
        expressionTypeStr="Infix"
    heading2.configure(text="Enter the "+expressionTypeStr+" Expression: ")
    
expression_type = IntVar()
chkb1 = Checkbutton(root, text='PREFIX', font=("Arial Rounded MT Bold", 16), variable=expression_type, offvalue=0, onvalue=1, compound=LEFT,bg="white", command=ExpressionType)
chkb1.place(relx=0.15, y=250, anchor='w')
chkb2 = Checkbutton(root, text='INFIX', font=("Arial Rounded MT Bold", 16), variable=expression_type, offvalue=0, onvalue=2,compound=LEFT,bg="white",command=ExpressionType)
chkb2.place(relx=0.40, y=250, anchor='w')
chkb3 = Checkbutton(root, text='POSTFIX', font=("Arial Rounded MT Bold", 16), variable=expression_type, offvalue=0, onvalue=3, compound=LEFT,bg="white",command=ExpressionType)
chkb3.place(relx=0.65, y=250, anchor='w')



heading2 = Label(root,
                 text="Select the type of expression above",
                 font=("Helvetica 12 bold"), bg='white', fg='black')
heading2.place(relx=0.50, y=290, anchor='center')


Exp=StringVar()

ExpressionEntryBox=Entry(root, bd=1,relief="solid", textvariable=Exp)
ExpressionEntryBox.place(relx=0.50, y=330, anchor='center')


global color_prev;
color_prev= 'lightcyan';
def submit():
    if(Exp.get()==""):
        messagebox.showerror("Error", "Field is empty")
        root.focus_force() #To bring the window in focus
    elif(' ' in Exp.get()):
        messagebox.showerror("Error", "Field cannot contain blank spaces between characters")
        root.focus_force() 
    elif(('(' in Exp.get() or ')' in Exp.get()) and (expression_type.get()==1 or expression_type.get()==3)):
        messagebox.showerror("Error", "Field cannot have '(' or ')'. Only valid for INFIX")
        root.focus_force()
    else:
        flag=0
        if(expression_type.get()==1):
            try:
                just_checking = prefixToInfix(Exp.get())
                just_checking = prefixToPostfix(Exp.get())
                flag=1
            except:
                messagebox.showerror("Error", "Field must have prefix expression.")
                root.focus_force()
            
        elif(expression_type.get()==2):
            try:
                just_checking = infixToPrefix(Exp.get())
                just_checking = infixToPostfix(Exp.get())
                flag=1
            except:
                messagebox.showerror("Error", "Field must have infix expression.")
                root.focus_force()
                    
        elif(expression_type.get()==3):
            try:
                just_checking = postfixToPrefix(Exp.get())
                just_checking = postfixToInfix(Exp.get())
                flag=1
            except:
                messagebox.showerror("Error", "Field must have postfix expression.")
                root.focus_force()
        if(flag):
            result_window = Tk()
            result_window.title("Result")
            result_window.geometry('1200x600')
            result_window.focus_force()
            result_window.geometry("{}x{}+{}+{}".format(1200, 600, int((root.winfo_screenwidth() / 2) - (1200 / 2)),
                                           int((root.winfo_screenheight() / 2) - (600 / 2))))
            result_window.minsize(1200, 600)  # min width,height
            result_window.maxsize(1200, 600)

            L1 = Label(result_window, text='Prefix: ', font='time 26 bold', fg='black', bg='grey')
            L1.grid(row=1, column=0, padx=10, pady=10)
            L2 = Label(result_window, text='Infix: ', font='time 26 bold', fg='black', bg='grey')
            L2.grid(row=2, column=0, padx=10, pady=10)
            L3 = Label(result_window, text='Postfix: ', font='time 26 bold', fg='black', bg='grey')
            L3.grid(row=3, column=0, padx=10, pady=10)


            if(expression_type.get()==1):
                L1value = Label(result_window, text=Exp.get(), font='time 24 ', fg='black', bg='grey')
                L1value.grid(row=1, column=2, padx=10, pady=10)
                L2value = Label(result_window, text=prefixToInfix(Exp.get()), font='time 24 ', fg='black', bg='grey')
                L2value.grid(row=2, column=2, padx=10, pady=10)
                L3value = Label(result_window, text=prefixToPostfix(Exp.get()), font='time 24 ', fg='black', bg='grey')
                L3value.grid(row=3, column=2, padx=10, pady=10)
                
            elif(expression_type.get()==2):
                L1value = Label(result_window, text=infixToPrefix(Exp.get()), font='time 24 ', fg='black', bg='grey')
                L1value.grid(row=1, column=2, padx=10, pady=10)
                L2value = Label(result_window, text=Exp.get(), font='time 24 ', fg='black', bg='grey')
                L2value.grid(row=2, column=2, padx=10, pady=10)
                L3value = Label(result_window, text=infixToPostfix(Exp.get()), font='time 24 ', fg='black', bg='grey')
                L3value.grid(row=3, column=2, padx=10, pady=10)
                        
            elif(expression_type.get()==3):
                L1value = Label(result_window, text=postfixToPrefix(Exp.get()), font='time 24 ', fg='black', bg='grey')
                L1value.grid(row=1, column=2, padx=10, pady=10)
                L2value = Label(result_window, text=postfixToInfix(Exp.get()), font='time 24 ', fg='black', bg='grey')
                L2value.grid(row=2, column=2, padx=10, pady=10)
                L3value = Label(result_window, text=Exp.get(), font='time 24 ', fg='black', bg='grey')
                L3value.grid(row=3, column=2, padx=10, pady=10)
            

            L4 = Label(result_window, text='Made By: Kartikeya Menon', font='time 16 bold', fg='black', bg='grey')
            L4.place(relx=0.02, rely=0.85)
                       
            
            Button(result_window, text="Close", font=("Arial", 16), fg="white", bg="red", width=10,
                   height=1, cursor="hand2", command=lambda:[result_window.destroy(),root.focus_force()]).place(relx=0.85, rely=0.85)


            color_list=['white smoke','light yellow', 'lightcyan', 'lightsteelblue', 'lightpink', 'peachpuff']

            global color_prev;
            color = random.choice(color_list)
            while(color == color_prev):
                color = random.choice(color_list)

            color_prev = color;
            
            root.configure(background=color)
            heading1.configure(bg=color)
            main_icon_label.configure(bg=color)
            heading2.configure(bg=color)
            chkb1.configure(bg=color)
            chkb2.configure(bg=color)
            chkb3.configure(bg=color)
            result_window.configure(bg=color)
            L1.configure(bg=color)
            L2.configure(bg=color)
            L3.configure(bg=color)
            L1value.configure(bg=color)
            L2value.configure(bg=color)
            L3value.configure(bg=color)
            L4.configure(bg=color)
           
    



button1 = Button(root, text="Calculate", command=submit, compound="center", bg="black",
                 font=("Calibri", 20), fg="white", cursor="hand2")
button1.place(relx=0.50, y=400, anchor='center')
root.mainloop()
