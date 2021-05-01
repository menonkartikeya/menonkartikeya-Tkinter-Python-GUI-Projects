import pafy
import vlc
import youtube_dl

from tkinter import *
from tkinter import ttk, messagebox

import sqlite3

#Opening/Creating/Connecting the database connection
mydb=sqlite3.connect("YouTubeLinks.db") #Also creates a database if not already present

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS youtubelinks (_id integer PRIMARY KEY,\
                 video_title_with_link text)")
#Only 5 Datatypes in sqlite: text, int, real(decimal), null (does/doesnt exists), blob (image, video,etc.)
mydb.commit()

root = Tk()
root.geometry('1200x600')
root.minsize(1200, 600)  # min width,height
root.geometry("{}x{}+{}+{}".format(1200, 600, int((root.winfo_screenwidth() / 2) - (1200 / 2)),
                                   int((root.winfo_screenheight() / 2) - (600 / 2))))

root.title("YouTube MP3 Player")
main_icon = PhotoImage(file="youtube.png")
root.iconphoto(True, main_icon)

root.configure(background="white")

heading1 = Label(root, text=" My YouTube MP3 PlayList\n", font=("Arial Rounded MT Bold", 26), bg='white',
                 fg='black')
heading1.pack()

main_icon = PhotoImage(file='youtube.png')
main_icon_label = Label(root, image=main_icon, bg='white')
main_icon_label.pack()



heading2 = Label(root,
                 text="Enter the YouTube Link",
                 font=("Helvetica 18 bold"), bg='white', fg='black')
heading2.place(relx=0.15, y=290, anchor='center')


url=StringVar()

URLEntryBox=Entry(root, bd=1,relief="solid", textvariable=url,width=50)
URLEntryBox.place(relx=0.15, y=330, anchor='center',height=30)
URLEntryBox.focus()


def start_video(event):
    index = listbox.curselection()
    movie_name = listbox.get(index).split('LinkStartsFromHere$')[1]

    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    # Add all the available extractors
    ydl.add_default_info_extractors()
    result = ydl.extract_info(movie_name,download=False) # We just want to extract the info
    for format in result['formats']:
      if format['ext'] == 'm4a':
        audio_url = format['url']
    #print(audio_url)

    player = vlc.MediaPlayer(audio_url)

#Code for playing/streaming mp4 video :
##    video = pafy.new(movie_name) #instance of pafy to extract that YouTube video
##
##    best = video.getbest()  #best quality of that video will be extracted
##
##    playurl = best.url
##
##    instance=vlc.Instance()
##    player=instance.media_player_new()
##    media=instance.media_new(playurl)
##    
##    media.get_mrl() #media resource locator
##    player.set_media(media)
    player.play()
    player.toggle_fullscreen()

    Fenetre = Tk()  #French for 'window'

    def play1():
        B1.configure(text="Pause", command=pause1)
        player.play()
    def pause1():
        B1.configure(text=" Play", command=play1)
        player.pause()
    def forwd1():
        value = player.get_length()/1000
        percent = 1000/value
        player.set_position(player.get_position() + (percent/100))
    def bacwd1():
        value = player.get_length()/1000
        percent = 1000/value
        player.set_position(player.get_position() - (percent/100))
    def volUP():
        player.audio_set_volume(player.audio_get_volume() + 10)
    def volDN():
        player.audio_set_volume(player.audio_get_volume() - 10)
    def stop1():
        player.stop()
        Fenetre.destroy()
        
    Fenetre.attributes("-topmost", True)
    Fenetre.overrideredirect(True) #Remove border

    grip = Button(Fenetre,bitmap="gray25", width = 40)
    grip.pack()
    B1 = Button(Fenetre, text="Pause", command=pause1, width = 5)
    B1.pack()
    B2 = Button(Fenetre, text=" +10s ", command=forwd1, width = 5)
    B2.pack()
    B3 = Button(Fenetre, text=" -10s ", command=bacwd1, width = 5)
    B3.pack()
    B4 = Button(Fenetre, text=" Vol+ ", command=volUP, width = 5)
    B4.pack()
    B5 = Button(Fenetre, text=" Vol- ", command=volDN, width = 5)
    B5.pack()
    B6 = Button(Fenetre, text=" Exit", command=stop1, width = 5)
    B6.pack()

    #Functions to make fenetre movable

    def do_move(event):
        Fenetre.geometry(f'+{event.x_root}+{event.y_root}')

    grip.bind("<B1-Motion>", do_move)

##    if(not player.is_playing()):
##        Fenetre.destroy()
        
    #Don't use time.sleep() with tkinter. Instead, call the function after on the widget you want to close.
    #Fenetre.after(video.length*1000,lambda: Fenetre.destroy())

    Fenetre.mainloop()

##    time.sleep(video.length)
##    player.stop()

    
listbox = Listbox(root, width=130,exportselection=0)    #When set to 0, the selection won't change just because another widget gets some or all of its data selected.
listbox.pack(side = RIGHT, fill = Y)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM youtubelinks")
result=mycursor.fetchall()
for x in result:
    listbox.insert(END, x[1])   #Just x in place of x[1] will also give S.No.

scrollbar = Scrollbar(root, orient="vertical")
scrollbar.pack(side = RIGHT, fill = BOTH)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

listbox.bind("<Double-Button>", start_video)
#listbox.bind("<Button>", start_video)
listbox.bind('<FocusOut>', lambda e: listbox.selection_clear(0, END)) #To deselect the selected item by clicking at entry box or any widget outside outside the listbox

def submit():
    if(url.get()==""):
        messagebox.showerror("Error", "field is empty")
        root.focus_force() #To bring the window in focus
        URLEntryBox.focus()
    else:
        try:
            video = pafy.new(url.get()) #if the url is wrong except block will be executed
            
            title = video.title
            mp4 = [title,"                                                                                                                                                                                                                                                                 LinkStartsFromHere$",url.get()]

            mycursor=mydb.cursor()
            mp4ListINTOString = "".join(mp4)      #to avoid adding braces (since it is a list) along with the text use " ".join(list)
            mycursor.execute("INSERT INTO youtubelinks (video_title_with_link) VALUES (?)", (mp4ListINTOString,))   #Just ? in place of (?) is also fine
            mydb.commit()
            
            listbox.insert(END, mp4ListINTOString)
                    
            URLEntryBox.delete(0, END)
            
        except:
            messagebox.showerror("Error", "Invalid URL")
            URLEntryBox.delete(0, END)
            root.focus_force()
            URLEntryBox.focus()

L4 = Label(root, text='Made By: Kartikeya Menon', font='time 10 bold', fg='black', bg='white')
L4.place(relx=0.08, rely=0.85)    

add_btn = PhotoImage(file = "Picture.png")
button1 = Button(root, text="Add to PlayList", command=submit, compound="center", bg="white",
                 font=("Calibri", 20), fg="black", cursor="hand2", image = add_btn, activebackground='white',
             borderwidth = 0)
button1.place(relx=0.15, y=400, anchor='center')

#TWO BUTTONS CLEAR AND CLEAR ALL:
def clear():
    try:
        indexofSelectedItem = listbox.curselection() #returns only a tuple which is : (index_in_listbox,)    Hence, only using here to handle exception. See its use in next 3rd line.
        index = listbox.get(ACTIVE)     #returns entire tuple which is : (index_in_listbox,)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM youtubelinks WHERE _id = ?", (indexofSelectedItem[0],)) #Just using for raising exception , this raises error when nothing is selected. Hence "except" block.
##        option = messagebox.askyesno("Caution!", "Pressing Yes Will Delete It From Your Record")
##        if option:
        mycursor.execute("DELETE FROM youtubelinks WHERE video_title_with_link = ?",(index,))
        mydb.commit()
        listbox.delete(ANCHOR)  #to delete the selected item from listbox
    except:
        messagebox.showerror("Error", "Select a Link To Delete")
        
    
def clearAll():
    option = messagebox.askyesno("Caution!", "Pressing Yes Will Delete All Your Records")
    if option:
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM youtubelinks") #not truncate, unlike MySQL
        mydb.commit()
        listbox.delete(0,END)   #to delete all items from listbox
        messagebox.showinfo("Deleted!", "All Records Deleted successfully ")
    
    
button2 = Button(root, text="Clear", command=clear, compound="center", bg="white",width=10,
                 font=("Calibri", 12), fg="black", cursor="hand2",activebackground='white')
button2.place(relx=0.85, y=180, anchor='center')

button3 = Button(root, text="Clear All", command=clearAll, compound="center", bg="white",width=10,
                 font=("Calibri", 12), fg="black", cursor="hand2", activebackground='white')
button3.place(relx=0.95, y=180, anchor='center')

root.mainloop()

mydb.close()
