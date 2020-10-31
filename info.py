from tkinter import *
from tkinter import ttk

from tkinter import font, colorchooser, filedialog, messagebox


def aboutus():
    root1 = Tk()
    root1.geometry("{}x{}+{}+{}".format(600, 625, int((root1.winfo_screenwidth()/2) - (600/2)), int((root1.winfo_screenheight()/2) - (625/2))))
    root1.minsize(600, 625) #min width,height
    root1.focus_force() #To bring the window in focus

    root1.title("Contacts")
    main_icon1 = PhotoImage(file = 'icons/ContactsIcon2.png', master=root1)
    root1.iconphoto(False, main_icon1)
    root1.configure(background='white')
 
    def info():
        root1.destroy()
        root2=Tk()
        root2.geometry("{}x{}+{}+{}".format(700, 625, int((root2.winfo_screenwidth()/2) - (700/2)), int((root2.winfo_screenheight()/2) - (625/2))))
        root2.minsize(700, 625) #min width,height
        root2.focus_force() #To bring the window in focus

        root2.title("Contacts")
        main_icon1 = PhotoImage(file = 'icons/ContactsIcon2.png', master=root2)
        root2.iconphoto(False, main_icon1)
        root2.configure(background='white')

        Label(root2,text="Details Of This Project:\n",font=("Arial 93",17),fg="orange",bg="White").place(relx=0.5,rely=0.05,anchor='center')

        with open("about.txt", "r") as f:
            Label(root2, text=f.read(),bg='white', justify=LEFT, anchor="w").pack(pady=50)
    
        def close_window():
            root2.destroy()
        Button(root2,text="Back",font=("Arial",16),fg="white",bg="orange",compound="center",width=5,height=1,cursor="hand2",command=lambda:[close_window(), aboutus()]).place(relx=0.77,rely=0.97,anchor='se')
        Button(root2,text="Close",font=("Arial",16),fg="white",bg="orange",compound="center",width=5,height=1,cursor="hand2",command=close_window).place(relx=0.9,rely=0.97,anchor='se')

        root2.mainloop()

    Button(root1,text="Click Icon For Project Details",font=("Arial 93",17),fg="orange",bg="white",compound="center",cursor="hand2",command=info, borderwidth=0,activebackground='white').place(relx=0.5,rely=0.05,anchor='center')

    icon = PhotoImage(file = "icons/ContactsIcon.png", master=root1)
    button_style = ttk.Style()
    button_style.configure('IconButton', font =('calibri', 10, 'bold', 'underline'), foreground = 'red')
    button_style.map('IconButton', foreground = [('active', 'green')], background = [('active', 'black')]) 
    button = Button(root1, text="Hello!", image=icon,command=info, activebackground='white',fg = '#37d3ff',bg = 'white',relief='ridge')
    button.place(relx=0.5,rely=0.5,anchor='center')

    root1.mainloop()

if __name__ == "__main__":              #To run this program indiviually, if needed. This is for programmer, not used in application
    aboutus()
