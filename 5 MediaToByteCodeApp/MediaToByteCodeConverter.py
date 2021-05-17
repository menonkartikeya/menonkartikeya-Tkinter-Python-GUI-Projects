from tkinter import *
import base64
from tkinter.filedialog import askopenfilename

root = Tk()
root.state('zoomed')   #zooms the screen to maxm whenever executed
root.geometry('1300x780')
root.minsize(1300, 780)  
root.geometry("{}x{}+{}+{}".format(1300, 780, int((root.winfo_screenwidth() / 2) - (1300 / 2)),
                                   int((root.winfo_screenheight() / 2) - (780 / 2))))
root.title("Image and video to ByteCode!")
root.configure(background="lemonchiffon2")

Label(root, text="Convert Image/Video To String!", font=("Arial Rounded MT Bold", 26), bg='lemonchiffon2',fg='black').place(relx=0.5, y = 40, anchor="center")

def chooseFile():
##    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    global filename
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    message.config(text="Selected : "+filename,bg='white', fg='green')
    
def convertToString():
    if(name.get()==""):
        message.config(text="Please give a variable name",bg='white',fg='red')
    else:
        try:
            Btxt = base64.b64encode(open(filename,"rb").read())
            
            content = '{} = {}\n'.format(name.get(),Btxt)
            
            f = open("mediaToStr.py", "a")
            f.write(content)
            f.close()
            
            howToImport.config(text="\
import base64\n\
from io import BytesIO\n\
from PIL import Image, ImageQt, ImageTk\n\
from mediaToStr.py import \
"+name.get())
            nameEntry.focus()
            nameEntry.delete(0,'end')
            message.config(text="Done! Read below the next steps.",bg='white', fg='green')
        except:
            message.config(text="Error! Select a proper file",bg='white',fg='red')
    
message = Label(root,text="", font=("Arial Rounded MT Bold", 14),bg='lemonchiffon2',fg='red')
message.place(relx=0.50, y = 100, anchor="center")

Label(root,text="Choose the file:", font=("Arial Rounded MT Bold", 16),bg='lemonchiffon2',fg='black').place(relx=0.45, y = 140, anchor="center")
Button(root, text="Select", command=chooseFile, compound="center", bg="lemonchiffon3",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.55, y = 140, anchor="center")

name=StringVar()
Label(root,text="Enter Name (variable_name) You Want That String Variable To Be:", font=("Arial Rounded MT Bold", 16),bg='lemonchiffon2',fg='black').place(relx=0.42, y = 180, anchor="center")
nameEntry = Entry(root,font=("Helvetica",14),bd=1,relief="solid", textvariable=name)
nameEntry.place(relx=0.78, y = 180, anchor="center")
nameEntry.focus()

Button(root, text="Convert", command=convertToString, compound="center", bg="lemonchiffon3",font=("Calibri", 14), fg="black", cursor="hand2").place(relx=0.50, y = 250, anchor="center")


Label(root,text="Add these packages (specially if adding an image,\n3rd line is not necessary for video, videos require other packages like vlc):", font=("Arial Rounded MT Bold", 16),bg='lemonchiffon2',fg='black').place(relx=0.50, y = 330, anchor="center")
howToImport = Label(root, text="\
import base64\n\
from io import BytesIO\n\
from PIL import Image, ImageQt, ImageTk\n\
from mediaToStr.py import variable_name\n\n\
#NOTE: save the mediaToStr.py file from here to the directory where your source code is.\
", justify=LEFT)
howToImport.place(relx=0.50, y = 370, anchor="n")

Label(root,text="Example For Adding IconPhoto:", font=("Arial Rounded MT Bold", 16),bg='lemonchiffon2',fg='black').place(relx=0.20, y = 485, anchor="center")
Label(root, text="\
byte_data = base64.b64decode(logoinbytecode)\n\
image_data = BytesIO(byte_data)\n\
main_icon_img = Image.open(image_data)\n\
main_icon_ImageTk = ImageTk.PhotoImage(main_icon_img)\n\
root.iconphoto(True, main_icon_ImageTk)\
", justify=LEFT).place(relx=0.20, y = 505, anchor="n")

Label(root,text="Example For Adding an Image to a Label:", font=("Arial Rounded MT Bold", 16),bg='lemonchiffon2',fg='black').place(relx=0.80, y = 485, anchor="center")
Label(root, text="\
byte_data2 = base64.b64decode(photoinbytecode)\n\
image_data2 = BytesIO(byte_data2)\n\
photo_img = Image.open(image_data2)\n\
photo_ImageTk = ImageTk.PhotoImage(photo_img)\n\
Label(root, image=photo_ImageTk).pack()\
", justify=LEFT).place(relx=0.80, y = 505, anchor="n")

Label(root,text="If using a video, add this in your code:", font=("Arial Rounded MT Bold", 16),bg='lemonchiffon2',fg='black').place(relx=0.50, y = 600, anchor="center")
Label(root, text='''fh = open("video.mp4", "wb")
fh.write(base64.b64decode(variable_name))
fh.close()\n
Also, vlc will have to be used
(since TkVideo is only for playing videos "without sound" inside tkinter Label widget)''', justify=LEFT).place(relx=0.50, y = 620, anchor="n")


root.mainloop()
