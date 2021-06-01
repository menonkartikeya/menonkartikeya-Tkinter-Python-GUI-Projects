from tkinter import *
import base64
from tkinter import scrolledtext

root = Tk()
root.state('zoomed')   #zooms the screen to maxm whenever executed
root.geometry('1300x780')
root.minsize(650, 640)  
root.geometry("{}x{}+{}+{}".format(1300, 780, int((root.winfo_screenwidth() / 2) - (1300 / 2)),
                                   int((root.winfo_screenheight() / 2) - (780 / 2))))
root.title("ByteCode to image and video!")
root.configure(background="lemonchiffon2")

Label(root, text="Convert String To Image/Video!", font=("Arial Rounded MT Bold", 26), bg='lemonchiffon2',fg='black').place(relx=0.5, y = 40, anchor="center")

def convertToMedia():
    img_data = stringToEncode.get('1.0', 'end-1c')
    if(img_data==""):
        message.config(text="Please give a variable name",bg='white',fg='red')
    else:
        try:
            data = eval(img_data.encode('latin1'))  #since we're taking string input but we want value in bytes
            img_data = bytes(data.encode('latin1')) #so these two steps
            with open("image1.jpg", "wb") as fh:  #now just write it in a file "image.extension"
                encoded=base64.decodebytes(img_data)
                fh.write(encoded)
####        Alternatively:
##            image = open("image.jpg", "wb")
##            img.write(base64.b64decode(img_data))
##            image.close()

####            If Video was there too:
##            fh = open("video.mp4", "wb")
##            fh.write(base64.b64decode(string))
##            fh.close()
                
            stringToEncode.focus()
            stringToEncode.delete('1.0','end')
            message.config(text="Done! Read below the next steps.",bg='white', fg='green')
        except:
            message.config(text="Error! Select a proper file",bg='white',fg='red')

def dataURI():
    import urllib.request
    data = daturi.get('1.0', 'end-1c')
    if(data==""):
        message.config(text="Please give a variable name",bg='white',fg='red')
    else:
        try:
            response = urllib.request.urlopen(data)
            with open('image2.jpg', 'wb') as f:
                f.write(response.file.read())

            stringToEncode.focus()
            stringToEncode.delete('1.0','end')
            message.config(text="Done! Read below the next steps.",bg='white', fg='green')
        except:
            message.config(text="Error! Select a proper file",bg='white',fg='red')


message = Label(root,text="", font=("Arial Rounded MT Bold", 14),bg='lemonchiffon2',fg='red')
message.place(relx=0.50, y = 100, anchor="center")

name=StringVar()
Label(root,text="Enter String To Decode:", font=("Arial Rounded MT Bold", 16),bg='lemonchiffon2',fg='black').place(relx=0.50, y = 180, anchor="center")
stringToEncode = scrolledtext.ScrolledText(root,font=("Helvetica",10),bd=1,relief="solid", width=40, height=8) #wrap=WORD
stringToEncode.place(relx=0.45, y = 260, anchor="center")
stringToEncode.focus()

Button(root, text="Convert", command=convertToMedia, compound="center", bg="lemonchiffon3",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.60, y = 230, anchor="center")


Label(root,text="For data URI strings:", font=("Arial Rounded MT Bold", 16),bg='lemonchiffon2',fg='black').place(relx=0.50, y = 360, anchor="center")
daturi = scrolledtext.ScrolledText(root,font=("Helvetica",8),bd=1,relief="solid", width=40, height=2) #wrap=WORD
daturi.place(relx=0.45, y = 400, anchor="center")
Button(root, text="Convert", command=dataURI, compound="center", bg="lemonchiffon3",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.60, y = 400, anchor="center")

Label(root,text="If error is caused because of what image's original extension is:", font=("Arial Rounded MT Bold", 16),bg='lemonchiffon2',fg='black').place(relx=0.50, y = 460, anchor="center")
Label(root, text='''
Change the extension inside this source code:
      Try changing jpg to any other image extension like png, jpeg, etc.
      At line 24: image1.jpg
      At line 51: image2.jpg
''', justify=LEFT).place(relx=0.50, y = 480, anchor="n")

root.mainloop()
