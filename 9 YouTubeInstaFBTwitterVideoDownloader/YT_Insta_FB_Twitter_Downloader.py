from tkinter import *
from tkinter import messagebox, filedialog
#for ProgressBar:
from tkinter import ttk         
import urllib.request       #to get size of file from url
import threading
import time
import os                   #using getsize function os.path module

#for YouTube:
import pytube
from youtube_dl import *

#for Insta:
from bs4 import BeautifulSoup
import os, cv2, json, requests, urllib.request
import re

bgColor = "#373737"
textColor = 'whitesmoke'
secondColor = "#000000"

root = Tk()
root.state('zoomed')   #zooms the screen to maxm whenever executed
root.geometry('1300x780')
root.minsize(1300, 780)  
root.geometry("{}x{}+{}+{}".format(1300, 780, int((root.winfo_screenwidth() / 2) - (1300 / 2)),int((root.winfo_screenheight() / 2) - (780 / 2))))
root.title("YouTube Insta FaceBook Twitter Downloader")
root.configure(background=bgColor)

Label(root, text="Download Image/Video on your computer!", font=("Arial Rounded MT Bold", 26), bg=bgColor,fg=textColor).place(relx=0.5, y = 40, anchor="center")

instaURL = ""
download_Folder=""

def Download():
##    global videoStream, download_Folder, fileDownloading, link
    print(sourceOfMedia.get())
    print(v.get())

    link = LinkVar.get()
    print(link)

    
    global instaURL , download_Folder
    instaURL = link
    download_Folder = download_Path.get()
    print(download_Folder)
    if download_Folder == '(optional)':
        download_Folder = ''

##    try:
        if sourceOfMedia.get() == 1:        #YouTube

##            bar["value"]=0
##            bar["maximum"] = 100
##            global fileDownloading, videoStream, download_Folder, maxBytes, link
            messagebox.showinfo("Please Wait", "File Is downloading")
            getVideo = pytube.YouTube(link)
            videoStream = getVideo.streams.first()

##            maxBytes = videoStream.filesize
            fileDownloading = videoStream.download(download_Folder)
            
            #After Download starts, start the progress bar:
##            on_progress()
            
            messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED AS\n" + fileDownloading)
            
        elif sourceOfMedia.get() == 2:        #Insta
            
            i_Downloader()
            messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_Folder)
##    except:
##        messagebox.showerror("Error!", "Something Went Wrong. Recheck everything and try again.")
    
##maxBytes, fileDownloading, videoStream, download_Folder = 100, 0, '', ''

##def on_progress():
##    global maxBytes, fileDownloading
##    try:
##        bytes_downloaded = os.path.getsize(fileDownloading)
##    except:
##        bytes_downloaded = 0
##    liveprogress = (int)(bytes_downloaded / maxBytes * 100)
##    bar["value"] = liveprogress
##    label_progress.config(text=str(liveprogress)+"%")
##    root.update_idletasks()
##    
##    if liveprogress < 100:
##        time.sleep(0.1)
##        on_progress()
##        
        

def i_Downloader():
    # Sending request to the insta_url URL & storing the response in insta_Posts
    insta_Posts = requests.get(instaURL)
    # Specifying the desired format of the insta_Comments using html.parser
    # html.parser allows Python to read the components of the insta_Page
    soup = BeautifulSoup(insta_Posts.text, 'html.parser')
    # Finding <script> whose text matches with 'window._sharedData' using re.compile()
    script = soup.find('script', text=re.compile('window._sharedData'))
    # Splitting the text of <script>, 1 time at '=' and fetching the item at index 1
    # followed by removing the ';' from the string and storing the resulting string in page_json
    page_json = script.text.split(' = ', 1)[1].rstrip(';')
    # Parsing the above json page_json string using json_loads() and storing the resulting
    # dictionary in data variable which is a very long dictionary consisting of 19 items
    data = json.loads(page_json)
    # Storing the necessary part of the data dictionary in base_data
    base_data = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    # Fetching the __typename of the POST from base_d dictionary and storing them in typename
    typename = base_data['__typename']


    # Checking if the typename is GraphImage meaning INSTAGRAM POST is a single image
    if typename == "GraphImage":
        # Fetching the Instagram Image URL from display_url of base_data dictionary
        display_url = base_data['display_url']
        # Fetching the taken_at_timestamp value from base_data dictionary and storing in filename
        file_name = base_data['taken_at_timestamp']
        # Concatenating download_path with filename and .jpg extension and storing in download_p
        download_p = download_Folder + str(file_name) + ".jpg"
        # Checking if the file already exists using the os.path.exists() method
        if not os.path.exists(download_p):
            # If not, then download the file using the urlretrieve() of the urlib.request module
            # which takes the url and download_path as the arguments
            urllib.request.urlretrieve(display_url, download_p)
            # Opening the download_p image using the open() method of the Image module
            image = Image.open(download_p)
        else:
            print("ALREADY EXISTS")

    # Checking if the typename is GraphVideo meaning INSTAGRAM POST is a video
    elif typename == "GraphVideo":
        # Fetching the Instagram Video URL from video_url of base_data dictionary
        video_url = base_data['video_url']
        # Fetching the taken_at_timestamp value from base_data dictionary and storing in filename
        file_name = base_data['taken_at_timestamp']
        # Concatenating download_path with filename and .mp4 extension and storing in download_p
        download_p = download_Folder + str(file_name) + ".mp4"
        # Checking if the file already exists using the os.path.exists() method
        if not os.path.exists(download_p):
            # If not present then download the file using the urlretrieve() of the urlib.request
            # module which takes the url and download_path as the arguments
            urllib.request.urlretrieve(video_url, download_p)
            # Instead of displaying video in GUI, a frame of the video will be displayed as an icon
            # Creating object of class VideoCapture with the video (download_p) as argument
            vid = cv2.VideoCapture(download_p)
            # Capturing frame by frame
            ret, frame = vid.read()
            # Setting the download path and a name for the frame and storing in video_icon
            video_icon = download_path + "/Video Icons/" + str(file_name) + ".jpg"
            # Saving the frame using the cv2.imwrite()
            cv2.imwrite(video_icon, frame)
        else:
            print("HAS ALREADY BEEN DOWNLOADED")


    # Checking if typename is GraphSidecar meaning single POST consists of many images & videos
    elif typename == "GraphSidecar":
        # Fetching the value from shortcode of base_data dictionary
        shortcode = base_data['shortcode']
        # Sending request to INSTAGRAM URL with shortcode & converting the response to json and
        # storing the response in response
        response = requests.get(f"https://www.instagram.com/p/" + shortcode + "/?__a=1").json()
        # Declaring a variable named post_n and i and setting it to 1 and 0 respectively
        post_n = 1; i = 0
        # Interating through the edges present in the following location of response dictionary
        for edge in response['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']:
            # Fetching the taken_at_timestamp value from base_d dictionary and storing in filename
            file_name = response['graphql']['shortcode_media']['taken_at_timestamp']
            # Concatenating download_path with the filename & post_n value & storing in download_p
            download_p = download_Folder + str(file_name) + "-" + str(post_n)
            # Checking the value of is_video which will be either True or False
            is_video = edge['node']['is_video']

            # If is_video is False meaning single Instagram Post consists of only multiple Images
            if not is_video:
                # Fetching the Image URL from display_url of edge dictionary
                display_url = edge['node']['display_url']
                # Concatenating the download_p value with .jpg extension
                download_p += ".jpg"
                # Checking if the file already exists using the os.path.exists() method
                if not os.path.exists(download_p):
                    # If not present then download the file using the urlretrieve() of the
                    # urlib.request module which takes the url and download_path as the arguments
                    urllib.request.urlretrieve(display_url, download_p)
                    # Opening image, resizing it, & creating PhotoImage() class object to display it
                    image = Image.open(download_p)
                    
                else:
                    print(".jpg EXISTS")

            # If is_video is True meaning Instagram Post consists of VIDEO along with the image
            else:
                # Fetching the Video URL from video_url of edge dictionary
                video_url = edge['node']['video_url']
                # Concatenating the download_p value with .mp4 extension
                download_p += ".mp4"
                # Checking if the file already exists using the os.path.exists() method
                if not os.path.exists(download_p):
                    # If not present then download the file using the urlretrieve() of urlib.request
                    # module which takes the url and download_path as the arguments
                    urllib.request.urlretrieve(video_url, download_p)
                    # Creating object of VideoCapture with video as argument and capturing frame by frame
                    vid = cv2.VideoCapture(download_p)
                    ret, frame = vid.read()
                    # Setting the download path & name for frame & saving the frame using the cv2.imwrite()
                    video_icon = download_path + "/Video Icons/" + str(file_name) + ".jpg"
                    cv2.imwrite(video_icon, frame)
                    # Opening the video_icon, resizing it, & creating PhotoImage() class object to display it
                    icon = Image.open(video_icon)
                    
                else:
                    print("EXISTS")
            # Incrementing the post_n value by 1
            post_n += 1
    
sourceOfMedia = IntVar()    #IntVar(value=0)   : To initialize

#CHECKBUTTON OF YouTube:
YTphoto = PhotoImage(file = "youtube.png")
YTphoto = YTphoto.subsample(10, 10)
chkb1 = Checkbutton(root, text='YouTube', image=YTphoto, font=("Arial Rounded MT Bold", 16), variable=sourceOfMedia, bg=bgColor,fg=textColor,  activebackground=bgColor, activeforeground=textColor, selectcolor=bgColor, offvalue=0, onvalue=1, compound=LEFT) #value=1 means selected, is by default checked
chkb1.select()              #To by default check the checkbutton
chkb1.place(relx=0.20, y=185, anchor='center')

#CHECKBUTTON OF Insta:
Instaphoto = PhotoImage(file = "instagram.png")
Instaphoto = Instaphoto.subsample(10, 10)
chkb1 = Checkbutton(root, text='Instagram', image=Instaphoto, font=("Arial Rounded MT Bold", 16), variable=sourceOfMedia, bg=bgColor,fg=textColor,  activebackground=bgColor, activeforeground=textColor, selectcolor=bgColor, offvalue=0, onvalue=2, compound=LEFT) 
chkb1.place(relx=0.40, y=185, anchor='center')

#CHECKBUTTON OF FaceBook:
FBphoto = PhotoImage(file = "facebook.png")
FBphoto = FBphoto.subsample(10, 10)
chkb1 = Checkbutton(root, text='FaceBook', image=FBphoto, font=("Arial Rounded MT Bold", 16), variable=sourceOfMedia, bg=bgColor,fg=textColor,  activebackground=bgColor, activeforeground=textColor, selectcolor=bgColor, offvalue=0, onvalue=3, compound=LEFT) 
chkb1.place(relx=0.60, y=185, anchor='center')

#CHECKBUTTON OF Twitter:
Twitterphoto = PhotoImage(file = "twitter.png")
Twitterphoto = Twitterphoto.subsample(10, 10)
chkb1 = Checkbutton(root, text='Twitter', image=Twitterphoto, font=("Arial Rounded MT Bold", 16), variable=sourceOfMedia, bg=bgColor,fg=textColor,  activebackground=bgColor, activeforeground=textColor, selectcolor=bgColor, offvalue=0, onvalue=4, compound=LEFT) 
chkb1.place(relx=0.80, y=185, anchor='center')


#RadioButtons for Audio or Video Format:
Label(root, text="Choose Format", font=("Arial Rounded MT Bold", 14), bg=bgColor,fg=textColor).place(relx=0.5, y = 250, anchor="center")

v = StringVar(root, "audio")
Radiobutton(root, text = "Audio", variable = v, value = "audio", indicator = 0, background = "#808080", padx=40).place(relx=0.46, y = 300, anchor="center")
Radiobutton(root, text = "Video", variable = v, value = "video", indicator = 0, background = "#808080", padx=40).place(relx=0.54, y = 300, anchor="center")



LinkVar=StringVar(root)


Label(root,text="Enter Key Value:", font=("Arial Rounded MT Bold", 16),bg=bgColor,fg=textColor).place(relx=0.50, y = 410, anchor="center")
keyEntry = Entry(root,font=("Helvetica",18),bd=1,relief="solid",bg=textColor,fg=bgColor, width=60, textvariable=LinkVar) 
keyEntry.place(relx=0.50, y = 410, anchor="center")
keyEntry.focus()

#Destination:
download_Path = StringVar()
def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")  # Presenting user with a pop-up for
    download_Path.set(download_Directory)
  
destination_label = Label(root, text="Destination    :", bg=bgColor, fg=textColor).place(relx=0.25, y = 450, anchor="center")
destinationText = Entry(root, width=90, textvariable=download_Path)
destinationText.place(relx=0.50, y = 450, anchor="center")
def focusIn(*args):
    destinationText.delete(0, 'end')
def focusOut(*args):    
    destinationText.delete(0, 'end')
    destinationText.insert(0, '(optional)')
    root.focus()
    
destinationText.insert(0, '(optional)')
destinationText.bind("<FocusIn>", focusIn)
destinationText.bind("<FocusOut>", focusOut)

browse_B = Button(root, text="Browse", command=Browse,width=10, bg=bgColor, fg=textColor).place(relx=0.75, y = 450, anchor="center")

Button(root, text="Download", command=Download, compound="center", bg=secondColor,font=("Calibri", 14), fg=textColor, cursor="hand2").place(relx=0.50, y = 550, anchor="center")



#Progress Bar:
bar= ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
bar.place(relx=0.45, y = 610, anchor="center")

label_progress = Label(root, font='arial 11 bold', fg=textColor, bg=bgColor)
label_progress.place(relx=0.60, y = 610, anchor="center")


root.mainloop()
