from tkinter import *
from tkinter import messagebox, filedialog

from tkinter import ttk         
import urllib.request       #to get size of file from url
import os                   #using getsize function os.path module

import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading

bgColor = 'whitesmoke'      #"#373737"
textColor = 'black'         #'whitesmoke'
secondColor = 'whitesmoke'  #"#000000"

root = Tk()
root.state('zoomed')   #zooms the screen to maxm whenever executed
root.geometry('1300x780')
root.minsize(1300, 780)  
root.geometry("{}x{}+{}+{}".format(1300, 780, int((root.winfo_screenwidth() / 2) - (1300 / 2)),int((root.winfo_screenheight() / 2) - (780 / 2))))
root.title("YouTube Insta FaceBook Twitter Downloader")
root.configure(background=bgColor)
##root.attributes('-alpha',0.9)

Label(root, text="Download Image/Video on your computer!", font=("Arial Rounded MT Bold", 26), bg=bgColor,fg=textColor).place(relx=0.5, y = 40, anchor="center")

def download_wait(directory, timeout):
    """
    Wait for downloads to finish with a specified timeout.
    """
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(4)
        dl_wait = False
        files = os.listdir(directory)
        for fname in files:
            if fname.endswith('.crdownload') or (('crdownload') in fname):
                dl_wait = True

        seconds += 1
    return seconds

import urllib.request
import glob
from moviepy.editor import *

def downloadit():
    global srcMedia, audVid, link, download_Folder, dwn_thread, driver, flag   
    print(download_Folder)
    if srcMedia == 1:
        if link.find('youtube') == -1:
            messagebox.showerror("The link is incorrect!", "Invalid Youtube video url. Please try again.")
            return
    elif srcMedia == 2:
        if link.find('instagram') == -1:
            messagebox.showerror("The link is incorrect!", "Invalid Instagram video url. Please try again.")
            return
    elif srcMedia == 3:
        if link.find('facebook') == -1:
            messagebox.showerror("The link is incorrect!", "Invalid FaceBook video url. Please try again.")
            return
    elif srcMedia == 4:
        if link.find('twitter') == -1:
            messagebox.showerror("The link is incorrect!", "Invalid Twitter video url. Please try again.")
            return

            
    browser = 'chrome'
    if browser == 'chrome':
        Options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": download_Folder,
                 "directory_upgrade": True}
        Options.add_experimental_option("prefs", prefs)


        Options.add_argument('headless')
        Options.add_argument("no-sandbox")
        Options.add_argument("disable-dev-shm-usage")

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=Options)
    
    if srcMedia == 1:        #YouTube
        driver.get('https://yt1s.com/en9')
        id_box = driver.find_element_by_id('s_input')
        id_box.send_keys(link)

        redBTN = driver.find_elements_by_class_name('btn-red')
        redBTN[0].click()

        time.sleep(8)
        try:
            search_error = driver.find_element_by_xpath("//p[contains(text(), 'Invalid Youtube video url. Please try again.')]")
            print(search_error.text)
            messagebox.showerror("The link is not correct!", "Invalid Youtube video url. Please try again.")
            driver.close()
            return
        except:
            print("Link OK ")
            
        if audVid == "audio":
            mp3SelectBox = driver.find_element_by_xpath("//select[@id='formatSelect']/optgroup[@label='mp3']/option")
            mp3SelectBox.click()
                                                                    
        getLinkBtn = driver.find_element_by_id('btn-action')
        getLinkBtn.click()

        time.sleep(8)
        DownloadBtn = driver.find_element_by_link_text('Download')
        DownloadBtn.click()
        download_wait(download_Folder, 1000)
        
    elif srcMedia == 2:        #Insta
        driver.get('https://inflact.com/downloader/instagram/video/')
        id_box = driver.find_element_by_id('downloaderform-url')
        id_box.send_keys(link)

        dwnBTN = driver.find_element_by_id('search')
        dwnBTN.click()

        time.sleep(12)
        try:
            search_error = driver.find_elements_by_class_name('results-not-found')
            print(search_error[0])
            messagebox.showerror("The link is not correct!", "Invalid Instagram url. Please check the URL & try again.")
            driver.close()
            return
        except:
            print("Link OK ")
                            
        DownloadBtns = driver.find_elements_by_class_name('download-button')
        print(DownloadBtns)
        list_of_files = glob.glob(download_Folder+'*.mp4')
        try:
            prev_latest_file = max(list_of_files, key=os.path.getctime)
        except:
            prev_latest_file = "1"
            print("NO mp4 file previously")
            
        for e in DownloadBtns:
            print(e)
            e.click()
            sec = download_wait(download_Folder, 1000)
            print(sec)
            
        if audVid == "audio":
            list_of_files = glob.glob(download_Folder+'*.mp4')
            try:
                latest_file = max(list_of_files, key=os.path.getctime)
                print(latest_file)
                if prev_latest_file!=latest_file:
                    video = VideoFileClip(os.path.join(download_Folder,download_Folder,latest_file))
                    latest_file_without_extension = latest_file.rsplit('.', 1)[0]
                    print(latest_file_without_extension) 
                    video.audio.write_audiofile(os.path.join(download_Folder,download_Folder,latest_file_without_extension+".mp3"))
                print("DONE")
            except:
                print("NOT mp4 file")
            
            
            
    elif srcMedia == 3:        #FB
        driver.get('https://snapsave.app/')
        id_box = driver.find_element_by_name('url')
        id_box.send_keys(link)

        dwnBTN = driver.find_element_by_id('send')
        dwnBTN.click()

        time.sleep(12)
        try:
            search_error = driver.find_element_by_xpath("//div[contains(text(), 'Url error. Please check again')]")
            print(search_error.text)
            messagebox.showerror("The link is not correct!", "Invalid FaceBook url. Please check the URL & try again.")
            driver.close()
            return
        except:
            print("Link OK ")

                           
        DownloadBtns = driver.find_elements_by_xpath("//a[contains(@class, 'button is-success is-small')]")
        print(DownloadBtns[0])
        DownloadBtns[0].click()

        try:
            iframe = driver.find_element_by_xpath("//iframe[@id='aswift_5']")
            driver.switch_to.frame(iframe)
            iframe2 = driver.find_element_by_xpath("//iframe[@id='ad_iframe']")
            driver.switch_to.frame(iframe2)
            closeAd = driver.find_element_by_xpath("//div[contains(@id, 'dismiss-button')]")
            closeAd.click()
            driver.switch_to.default_content()
        except Exception as s:
            print(s)            
        sec = download_wait(download_Folder, 1000)
        print(sec)
     
    elif srcMedia == 4:        #Twitter
        driver.get('https://www.downloadtwittervideo.com/')
        id_box = driver.find_element_by_name('url')
        id_box.send_keys(link)

        dwnBTN = driver.find_elements_by_class_name('StartDownloadButton_text')
        dwnBTN[0].click()

        time.sleep(5)
        
        try:
            iframe = driver.find_element_by_xpath("//iframe[@id='IframeErrorMessage']")
            driver.switch_to.frame(iframe)
            invalid = driver.find_element_by_xpath("//div[contains(@id, 'TitleText')]")
            print(invalid.text)
            messagebox.showerror("The link is not correct!", "Invalid Twitter url. Please check the URL & try again.")
            driver.close()
            return
        except Exception as e:
            print(e)
        driver.close()                    
        sec = download_wait(download_Folder, 1000)
        print(sec)
       
    flag = True

def after_dwn():
     global srcMedia, audVid, link, download_Folder, dwn_thread, driver, flag
     dwn_thread.join()           #waits till thread1 has completed executing

     driver.quit()

     if flag:
         messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_Folder)
     listbox.delete(0)
     check()
     
srcMedia, audVid, link, download_Folder, dwn_thread, driver, flag = '', '', '', '', '', '', False

import requests
    
def check():
    if q.empty():
        root.after(2000,check)
    else:
        newDnld = q.get()
        
        global srcMedia, audVid, link, download_Folder, dwn_thread, driver, flag
        srcMedia = newDnld.srcMedia
        audVid = newDnld.audVid
        link = newDnld.dnLink
        download_Folder = newDnld.dnFolder

        flag = False
        dwn_thread = threading.Thread(target=downloadit)
        dwn_thread.start()

        metadata_thread = threading.Thread(target=after_dwn)
        metadata_thread.start()
        
    
def change_color(container=None):
    global bgColor, textColor, secondColor
    if container is None:
        container = root  # set to root window
    container.config(bg=bgColor)
    for child in container.winfo_children():
        if child.winfo_children():
            change_color(child)# child has children, go through its children
        elif (type(child) is Label) or (type(child) is Checkbutton) or (type(child) is Radiobutton) or (type(child) is Button):
            child.config(bg=bgColor, fg=textColor,activebackground=bgColor, activeforeground=textColor)
            if type(child) is Radiobutton:
                child.config(selectcolor=secondColor,cursor="hand2", bg=bgColor, fg=textColor,activebackground=bgColor, activeforeground=textColor)
            
def changeTheme():
    global bgColor, textColor, secondColor
    if sourceOfMedia.get()==1:
        bgColor='#CC2E3C'
        textColor='whitesmoke'
        secondColor='#FE6A77'
    elif sourceOfMedia.get()==2:
        bgColor='#cd486b'
        textColor='white'
        secondColor='#ED93C3'
    elif sourceOfMedia.get()==3:
        bgColor='#4A5DAA'
        textColor='white'
        secondColor='#A3B0E7'
    elif sourceOfMedia.get()==4:
        bgColor='#6BC1F4'
        textColor='#373737'
        secondColor='#AED7EF'
    else:
        bgColor='whitesmoke'
        textColor='#373737'
        secondColor='whitesmoke'
    change_color()
    root.update()

from queue import Queue
q = Queue(maxsize = 30)


class downloadClass:
    def __init__(self, srcMedia, audVid, dnLink, dnFolder):
        self.srcMedia = srcMedia
        self.audVid = audVid
        self.dnLink = dnLink
        self.dnFolder = dnFolder
        
def DownloadBTN():
    if q.full():
        messagebox.showerror("Limit crossed","Wait till previous downloads are finished")
    else:
        link = LinkVar.get()
        try:
            req = requests.get(link)
        except Exception as ex:
            messagebox.showerror("Something went wrong!", ex)
            return
                
        download_Folder = download_Path.get()
        if download_Folder == '(optional)':
            download_Folder = os.path.dirname(os.path.realpath(__file__))
            
        if os.path.exists(download_Folder):
            print("Folder exists")
        else:
            messagebox.showerror("No such folder exists!", "Choose a correct file destination and try again")
            return 
        download_Folder = download_Folder.replace("/", "\\")

        newDownload = downloadClass(sourceOfMedia.get(),v.get(),link,download_Folder)
        q.put(newDownload)
        listbox.insert(END, "   " + newDownload.dnLink)
        
        
sourceOfMedia = IntVar(root, 1)  

#CHECKBUTTON OF YouTube:
YTphoto = PhotoImage(file = "youtube.png")
YTphoto = YTphoto.subsample(10, 10)
chkb1 = Radiobutton(root, width=60, image=YTphoto,compound="center", font=("Arial Rounded MT Bold", 16),indicator=0, variable=sourceOfMedia, value=1, command=changeTheme) #value=1 means selected, is by default checked
##chkb1.select()              #To by default check the checkbutton
chkb1.place(relx=0.43, y=185, anchor='center')

#CHECKBUTTON OF Insta:
Instaphoto = PhotoImage(file = "instagram.png")
Instaphoto = Instaphoto.subsample(10, 10)
chkb1 = Radiobutton(root, width=60, image=Instaphoto, compound="center",font=("Arial Rounded MT Bold", 16) ,indicator=0, variable=sourceOfMedia, value=2, command=changeTheme) 
chkb1.place(relx=0.48, y=185, anchor='center')

#CHECKBUTTON OF FaceBook:
FBphoto = PhotoImage(file = "facebook.png")
FBphoto = FBphoto.subsample(10, 10)
chkb1 = Radiobutton(root, width=60, image=FBphoto,compound="center", font=("Arial Rounded MT Bold", 16),indicator=0, variable=sourceOfMedia,  value=3, command=changeTheme) 
chkb1.place(relx=0.53, y=185, anchor='center')

#CHECKBUTTON OF Twitter:
Twitterphoto = PhotoImage(file = "twitter.png")
Twitterphoto = Twitterphoto.subsample(10, 10)
chkb1 = Radiobutton(root, width=60, image=Twitterphoto,compound="center", font=("Arial Rounded MT Bold", 16),indicator=0, variable=sourceOfMedia, value=4, command=changeTheme) 
chkb1.place(relx=0.58, y=185, anchor='center')


#RadioButtons for Audio or Video Format:
Label(root, text="Choose Format", font=("Arial Rounded MT Bold", 14), bg=bgColor,fg=textColor).place(relx=0.5, y = 250, anchor="center")

v = StringVar(root, "audio")
Radiobutton(root, text = "Audio", variable = v, value = "audio", indicator = 0, padx=40).place(relx=0.46, y = 300, anchor="center")
Radiobutton(root, text = "Video", variable = v, value = "video", indicator = 0, padx=40).place(relx=0.54, y = 300, anchor="center")



LinkVar=StringVar(root)

import pyperclip as pc
def Paste():
    linkInClipBoard= pc.paste()
    keyEntry.delete(0,END)
    keyEntry.insert(0,linkInClipBoard)
    
Label(root,text="Enter URL:", font=("Arial Rounded MT Bold", 16),bg=bgColor,fg=textColor).place(relx=0.50, y = 370, anchor="center")
keyEntry = Entry(root,font=("Helvetica",18),bd=1,relief="solid", width=60, textvariable=LinkVar) #,bg=bgColor,fg=textColors
keyEntry.place(relx=0.50, y = 410, anchor="center")
keyEntry.focus()

Button(root, text="Paste", command=Paste, compound="center", bg=bgColor,font=("Calibri", 10), fg=textColor, cursor="hand2").place(relx=0.77, y = 410, anchor="center")

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

Button(root, text="Download", command=DownloadBTN, compound="center", bg=bgColor,font=("Calibri", 14), fg=textColor, cursor="hand2").place(relx=0.50, y = 550, anchor="center")



#ListBox Frame:
f = Frame(root)
f.place(relx=0.50, y = 610, anchor="n")

listbox = Listbox(f, width=130, height=5, exportselection=0)    #When set to 0, the selection won't change just because another widget gets some or all of its data selected.
listbox.pack(side = LEFT, fill = Y)

scrollbar = Scrollbar(f, orient="vertical")
scrollbar.pack(side = LEFT, fill = BOTH)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

listbox.bind('<FocusOut>', lambda e: listbox.selection_clear(0, END)) #To deselect the selected item by clicking at entry box or any widget outside outside the listbox




changeTheme()
check()
root.mainloop()
