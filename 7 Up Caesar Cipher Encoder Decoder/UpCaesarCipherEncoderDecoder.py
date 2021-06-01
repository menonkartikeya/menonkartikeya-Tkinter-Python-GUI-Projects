from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.state('zoomed')   #zooms the screen to maxm whenever executed
root.geometry('1300x780')
root.minsize(1300, 780)  
root.geometry("{}x{}+{}+{}".format(1300, 780, int((root.winfo_screenwidth() / 2) - (1300 / 2)),int((root.winfo_screenheight() / 2) - (780 / 2))))
root.title("UP Caesar Cipher Code")
root.configure(background="seagreen2")

Label(root, text="Caesar Cipher Code!", font=("Arial Rounded MT Bold", 26), bg='seagreen2',fg='black').place(relx=0.5, y = 40, anchor="center")

keyVar=IntVar()


def EncodeCipher(k):
    if(isinstance(k, int)):
        a = stringToEncode.get('1.0', 'end-1c')
    ##    print(a)
        res=""
        for s in a:
            ints = ord(s)       #The function ord() gets the int value of the char, not int()
            if(ints>= 65 and ints<= 90):
                res+= chr(((ints-65+k)%26)+65)
            elif(ints>= 97 and ints<= 122):
                res+= chr(((ints-97+k)%26)+97)
            else:
                res+=s

        a = stringToDecode.get('1.0', 'end-1c')
        if a !="":
            ClearDeco();
##            stringToDecode.insert(INSERT,"\n")
        stringToDecode.insert(INSERT,res)
            
    
def DecodeCipher(k):
    if(isinstance(k, int)):
        a = stringToDecode.get('1.0', 'end-1c')
    ##    print(a)
        res=""
        for s in a:
            ints = ord(s)       #The function ord() gets the int value of the char, not int()
            if(ints>= 65 and ints<= 90):
                res+= chr(((ints-65-k)%26)+65)
            elif(ints>= 97 and ints<= 122):
                res+= chr(((ints-97-k)%26)+97)
            else:
                res+=s
        a = stringToEncode.get('1.0', 'end-1c')
        if a !="":
            ClearEnco()
##            stringToEncode.insert(INSERT,"\n")
        stringToEncode.insert(INSERT,res)

def ClearEnco():
    stringToEncode.delete('1.0', END)
def ClearDeco():
    stringToDecode.delete('1.0', END)

def CopyEnco():
    res = stringToEncode.get('1.0', 'end-1c')
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(res)
    clip.update() # now it stays on the clipboard after the window is closed
    clip.destroy()

def CopyDeco():
    res = stringToDecode.get('1.0', 'end-1c')
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(res)
    clip.update() # now it stays on the clipboard after the window is closed
    clip.destroy()
    
Label(root,text="Enter String to Encode:", font=("Arial Rounded MT Bold", 16),bg='seagreen2',fg='black').place(relx=0.12, y = 180, anchor="center")
stringToEncode = scrolledtext.ScrolledText(root,font=("Helvetica",14),bd=1,relief="solid", width=40, height=8) #wrap=WORD
stringToEncode.place(relx=0.38, y = 180, anchor="center")
stringToEncode.focus()

Label(root,text="Enter Key Value:", font=("Arial Rounded MT Bold", 16),bg='seagreen2',fg='black').place(relx=0.72, y = 310, anchor="center")
keyEntry = Entry(root,font=("Helvetica",14),bd=1,relief="solid",textvariable=keyVar) 
keyEntry.place(relx=0.88, y = 310, anchor="center")
keyEntry.insert(1,7)

Button(root, text="Clear", command=ClearEnco, compound="center", bg="gold2",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.58, y = 180, anchor="center")
Button(root, text="Copy", command=CopyEnco, compound="center", bg="gold2",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.63, y = 180, anchor="center")

Button(root, text="Encode", command=lambda:EncodeCipher(keyVar.get()), compound="center", bg="gold2",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.85, y = 350, anchor="center")

Label(root,text="Enter String to Decode:", font=("Arial Rounded MT Bold", 16),bg='seagreen2',fg='black').place(relx=0.12, y = 480, anchor="center")
stringToDecode = scrolledtext.ScrolledText(root,font=("Helvetica",14),bd=1,relief="solid", width=40, height=8) #wrap=WORD
stringToDecode.place(relx=0.38, y = 480, anchor="center")

Button(root, text="Clear", command=ClearDeco, compound="center", bg="gold2",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.58, y = 480, anchor="center")
Button(root, text="Copy", command=CopyDeco, compound="center", bg="gold2",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.63, y = 480, anchor="center")

Button(root, text="Decode", command=lambda:DecodeCipher(keyVar.get()), compound="center", bg="gold2",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.91, y = 350, anchor="center")

Label(root, text='''This application encodes and decodes a String in "up" Caesar Cipher :
User can set the value of key. (By default, it is 7)
Coded message will have (alphabetical letters + key) letters
Since, "+" therefore, I'm calling it "Up" Caesar Cipher
                                                                                        -Kartikeya Menon''', justify=LEFT).place(relx=0.50, y = 620, anchor="n")


root.mainloop()
