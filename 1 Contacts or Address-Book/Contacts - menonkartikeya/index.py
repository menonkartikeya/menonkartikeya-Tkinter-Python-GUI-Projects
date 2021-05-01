from tkinter import *

from tkcalendar import Calendar, DateEntry
from tkinter import ttk, font, colorchooser, filedialog, messagebox

import sqlite3

from info import aboutus

import csv
from tkinter import filedialog as fd


#Opening/Creating/Connecting the database connection

mydb=sqlite3.connect("Contacts.db") #Also creates a database if not already present

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS contactsdata (_id integer PRIMARY KEY,\
                 firstname text,\
                 middlename text,\
                 lastname text,\
                 nickname text,\
                 gender  text,\
                 dob  text,\
                 address text,\
                 city text,\
                 state text,\
                 pin text,\
                 country text,\
                 phone1 text,\
                 phone2 text,\
                 phone3 text,\
                 email1 text,\
                 email2 text,\
                 webs text,\
                 contactgroup text)")
#Only 5 Datatypes in sqlite: text, int, real(decimal), null (does/doesnt exists), blob (image, video,etc.)
mydb.commit()






mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS grouplist (_id integer PRIMARY KEY,\
                 group_name text,\
                 extra_id text)")
val=[('','by_default'),
     ('Friends','by_default'),
     ('Family','by_default'),
     ('Relatives','by_default'),
     ('Classmate','by_default'),
     ('School','by_default')]
mycursor=mydb.cursor()
result = mycursor.execute("SELECT * FROM grouplist WHERE group_name = 'Friends'") #Without this and the next if not statement, the rows will be added everytime this program is run
result = mycursor.fetchall()
if not result:
        mycursor.executemany("INSERT INTO grouplist (group_name,extra_id) VALUES (?,?)",val) #sqlite3 syntax: ? instead of %s
        mydb.commit()





mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS ColorTheme (_id integer PRIMARY KEY,\
                 themename text,\
                 colornames text)")
mydb.commit()
default_colors = ('#474747','#e0e0e0', '#474747')
result = mycursor.execute("SELECT * FROM ColorTheme WHERE _id = 1") #Without this and the next if not statement, the rows will be added everytime this program is run
result = mycursor.fetchall()
if not result:
        mycursor.execute("INSERT INTO ColorTheme (themename,colornames) VALUES (?,?)",('  Default',' '.join(default_colors),)) #sqlite3 syntax: ? instead of %s
        mydb.commit()        

      
      
      
      
      
def refresh():
    main_application.destroy()
    mainapplication()
        
def mainapplication():
    global main_application
    main_application = Tk()
    main_application.state('zoomed')   #zooms the screen to maxm whenever executed
    main_application.geometry('550x650')
    main_application.minsize(550, 650) #min width,height

    main_application.title("Contacts")
    main_icon = PhotoImage(file = "icons/ContactsIcon1.png")
    main_application.iconphoto(False, main_icon)

    global fg_color, bg_color, text_color
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM ColorTheme")
    res = mycursor.fetchall()        #colors is a list of all rows of that table
    Theme_Name = res[0][1]              
    colors = res[0][2]               #we need the 2nd column of 1st row, hence [0][1]
    colors = tuple(map(str, colors.split(' ')))         #make this string as tuple
    fg_color, bg_color, text_color = colors[0], colors[1], colors[2]
    
    #-------------------------------------------------------- Main menu ---------------------------------------------------

    main_menu=Menu()

    global id_reference
    id_reference=-1
    def ContactEditor(id_reference):
            add_contact_window = Tk()
            add_contact_window.geometry('600x625')
            add_contact_window.minsize(600, 625) #min width,height
            add_contact_window.maxsize(600, 625) #min width,height
            add_contact_window.focus_force() #To bring the window in focus
            add_contact_window.geometry("{}x{}+{}+{}".format(600, 625, int((add_contact_window.winfo_screenwidth()/2) - (600/2)), int((add_contact_window.winfo_screenheight()/2) - (625/2))))
            add_contact_window.title("Edit Contact")
            main_icon = PhotoImage(file = "icons/ContactsIcon1.png", master=add_contact_window)
            add_contact_window.iconphoto(False, main_icon)

            fg_color, bg_color, text_color = '#474747','white', 'black'

            #-------------------------------------------------------- Heading frame ---------------------------------------------------

            heading_frame = Frame(add_contact_window, height=100, bg='white')
            heading_frame.pack(fill=X,side=TOP)

            main_icon= PhotoImage(file='icons/ContactsIcon2.png', master=add_contact_window)
            main_icon_label= Label(heading_frame, image=main_icon, bg='white')
            main_icon_label.place(relx = 0.008, rely = 0.1)

            heading1 = Label(heading_frame, text=" Contact Editor",font=("Arial Rounded MT Bold", 26),bg='white',fg='black')
            heading1.place(x = 90, rely = 0.1)

            heading2 = Label(heading_frame, text="   My Address Book",font=("", 10),bg='white',fg='black')
            heading2.place(x = 90, rely = 0.5)
            ##################################################### End of Heading frame ################################################

            #--------------------------------------------------ContactDetails Frame ---------------------------------------------------

            #############################################################

            ContactDetails_frame = Frame(add_contact_window,bg='white', relief=RIDGE, bd=2, highlightthickness=2, highlightbackground='black')
            ContactDetails_frame.pack(fill=BOTH,expand=True)

            canvas_contact_window = Canvas(ContactDetails_frame,bg='white',scrollregion=(0,0,0,800), bd=0, highlightthickness=0)
            canvas_contact_window.pack(side=LEFT,fill=BOTH,expand=True)

            scrollbar = Scrollbar(ContactDetails_frame,orient=VERTICAL)
            scrollbar.pack(side=RIGHT,fill=Y)

            #Attach scrollbar to canvas_contact_window
            canvas_contact_window.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=canvas_contact_window.yview)

            #Binding MouseWheel to all window on canvas_contact_window
            def on_mousewheel(event):
                canvas_contact_window.yview_scroll(int(-1*(event.delta/120)), "units")
            canvas_contact_window.bind_all("<MouseWheel>", on_mousewheel)


            ##############################################

        #Variables to store the inputs
            VFirstName=StringVar(add_contact_window)
            VMiddleName=StringVar(add_contact_window)
            VLastName=StringVar(add_contact_window)
            VNickName=StringVar(add_contact_window)
            VGender=StringVar(add_contact_window)
            VDOB=StringVar(add_contact_window)
            VAddress=StringVar(add_contact_window)
            VCity=StringVar(add_contact_window)
            VState=StringVar(add_contact_window)
            VPIN=StringVar(add_contact_window)
            VCountry=StringVar(add_contact_window)
            VPhone1=StringVar(add_contact_window)
            VPhone2=StringVar(add_contact_window)
            VPhone3=StringVar(add_contact_window)
            VEmail1=StringVar(add_contact_window)
            VEmail2=StringVar(add_contact_window)
            Vwebs=StringVar(add_contact_window)
            VGroup=StringVar(add_contact_window)

         #To display on screen
            w=50
            FirstName2 = Label(canvas_contact_window, text="First name:", font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=FirstName2, anchor="w")
            EFirstName=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VFirstName)
            canvas_contact_window.create_window(150,w, window=EFirstName, anchor="w")

            w+=20
            MiddleName2 = Label(canvas_contact_window, text="Middle name:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=MiddleName2, anchor="w")
            EMiddleName=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VMiddleName)
            canvas_contact_window.create_window(150,w, window=EMiddleName, anchor="w")

            w+=20
            LastName2 = Label(canvas_contact_window, text="Last name:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=LastName2, anchor="w")
            ELastName=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VLastName)
            canvas_contact_window.create_window(150,w, window=ELastName, anchor="w")

            w+=20
            NickName2 = Label(canvas_contact_window, text="Nick name:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=NickName2, anchor="w")
            ENickName=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VNickName)
            canvas_contact_window.create_window(150,w, window=ENickName, anchor="w")

            w+=30
            Gender2 = Label(canvas_contact_window, text="Gender:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=Gender2, anchor="w")    
            VGender.set('Female')
            
            EGender1=Radiobutton(canvas_contact_window,text="Male",variable=VGender,value='Male',bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(150,w, window=EGender1, anchor="w")

            EGender2=Radiobutton(canvas_contact_window,text="Female",variable=VGender,value='Female',bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(220,w, window=EGender2, anchor="w")

            EGender3=Radiobutton(canvas_contact_window,text="Others",variable=VGender,value='Others',bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(290,w, window=EGender3, anchor="w")

            w+=30
            DOB2 = Label(canvas_contact_window, text="Date of birth:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=DOB2, anchor="w")
            EDOB=DateEntry(canvas_contact_window,width=17,height=2,bg="black",year=2001,fg="white",bd=1,relief="solid",textvariable=VDOB)
            EDOB.delete(0, "end")
            canvas_contact_window.create_window(150,w, window=EDOB, anchor="w")

            w+=20
            canvas_contact_window.create_line(5,w,285,w, fill="black")

            w+=20
            Address2 = Label(canvas_contact_window, text="Address:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=Address2, anchor="w")
            EAddress=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VAddress)
            canvas_contact_window.create_window(150,w, window=EAddress, anchor="w")

            w+=20
            City2 = Label(canvas_contact_window, text="City:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=City2, anchor="w")
            ECity=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VCity)
            canvas_contact_window.create_window(150,w, window=ECity, anchor="w")

            w+=20
            State2 = Label(canvas_contact_window, text="State:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=State2, anchor="w")
            EState=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VState)
            canvas_contact_window.create_window(150,w, window=EState, anchor="w")

            w+=20
            PIN2 = Label(canvas_contact_window, text="PIN/ZIP:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=PIN2, anchor="w")
            EPIN=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VPIN)
            canvas_contact_window.create_window(150,w, window=EPIN, anchor="w")
            
            w+=20
            Country2 = Label(canvas_contact_window, text="Country:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=Country2, anchor="w")
            ECountry=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VCountry)
            canvas_contact_window.create_window(150,w, window=ECountry, anchor="w")

            w+=20
            canvas_contact_window.create_line(5,w,285,w, fill="black")

            w+=20
            Phone12 = Label(canvas_contact_window, text="Phone(1):",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=Phone12, anchor="w")
            EPhone1=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VPhone1)
            canvas_contact_window.create_window(150,w, window=EPhone1, anchor="w")

            w+=20
            Phone22= Label(canvas_contact_window, text="Phone(2):",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=Phone22, anchor="w")
            EPhone2=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VPhone2)
            canvas_contact_window.create_window(150,w, window=EPhone2, anchor="w")

            w+=20
            Phone32 = Label(canvas_contact_window, text="Phone(3):",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=Phone32, anchor="w")
            EPhone3=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VPhone3)
            canvas_contact_window.create_window(150,w, window=EPhone3, anchor="w")
            
            w+=20
            Email12 = Label(canvas_contact_window, text="Email(1):",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=Email12, anchor="w")
            EEmail1=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VEmail1)
            canvas_contact_window.create_window(150,w, window=EEmail1, anchor="w")

            w+=20
            Email22 = Label(canvas_contact_window, text="Email(2):",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=Email22, anchor="w")
            EEmail2=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=VEmail2)
            canvas_contact_window.create_window(150,w, window=EEmail2, anchor="w")

            w+=20
            webs2 = Label(canvas_contact_window, text="Web:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=webs2, anchor="w")
            Ewebs=Entry(canvas_contact_window, bd=1,relief="solid", textvariable=Vwebs)
            canvas_contact_window.create_window(150,w, window=Ewebs, anchor="w")

            w+=20
            canvas_contact_window.create_line(5,w,285,w, fill="black")

            w+=20
            Group2 = Label(canvas_contact_window, text="Group:",font=(12),bg=bg_color,fg=text_color)
            canvas_contact_window.create_window(10,w, window=Group2, anchor="w")
            EGroup = ttk.Combobox(canvas_contact_window, width=22,textvariable = VGroup, state="readonly" ) #state readonly, otherwise user can type in the combobox
            # Adding combobox drop down list
            mycursor = mydb.cursor()
            G = mycursor.execute("SELECT group_name FROM grouplist")
            G = mycursor.fetchall()
            result=[]
            for row in G:
                result.append(row[0])

            EGroup['values'] = result 
            canvas_contact_window.create_window(150,w, window=EGroup, anchor="w")
            EGroup.current(0)# Shows none as default value 

        #When User is editing a contact... the previous data will be inserted in entry boxes prior like this:
            if(id_reference!=-1):
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM contactsdata WHERE _id = ?" ,(id_reference,))
                rn = mycursor.fetchall()
                for result_new in rn:
                    EFirstName.insert(0,result_new[1])
                    EMiddleName.insert(0,result_new[2])
                    ELastName.insert(0,result_new[3])
                    ENickName.insert(0,result_new[4])
                    VGender.set(result_new[5])
                    EDOB.insert(0,result_new[6])
                    EAddress.insert(0,result_new[7])
                    ECity.insert(0,result_new[8])
                    EState.insert(0,result_new[9])
                    EPIN.insert(0,result_new[10])
                    ECountry.insert(0,result_new[11])
                    EPhone1.insert(0,result_new[12])
                    EPhone2.insert(0,result_new[13])
                    EPhone3.insert(0,result_new[14])
                    EEmail1.insert(0,result_new[15])
                    EEmail2.insert(0,result_new[16])
                    Ewebs.insert(0,result_new[17])

                    G_index = result.index(result_new[18])  #To get the group_name's index in list and make it default
                    EGroup.current(G_index)

            def clear_fields():
                EFirstName.delete(0,"end")
                EMiddleName.delete(0,"end")
                ELastName.delete(0,"end")
                ENickName.delete(0,"end")
                VGender.set('Female')
                EDOB.delete(0,"end")
                EAddress.delete(0,"end")
                ECity.delete(0,"end")
                EState.delete(0,"end")
                EPIN.delete(0,"end")
                ECountry.delete(0,"end")
                EPhone1.delete(0,"end")
                EPhone2.delete(0,"end")
                EPhone3.delete(0,"end")
                EEmail1.delete(0,"end")
                EEmail2.delete(0,"end")
                Ewebs.delete(0,"end")
                EGroup.current(0)

            if(id_reference==-1):  #Adding a new contact
                                              
                    def saveit():
                        #To check if the contact does not exist already
                        sql = "SELECT * FROM contactsdata WHERE firstname = ?"      
                        name = (VFirstName.get(),)
                        mycursor=mydb.cursor()
                        result = mycursor.execute(sql,name)
                        result = mycursor.fetchall()
                        if(VFirstName.get()==""):
                            messagebox.showerror("Error", "First name field is empty")
                            add_contact_window.focus_force() #To bring the window in focus
                        elif not result:                           #Contact with same name does not exist already
                            mycursor1 = mydb.cursor()
                            sql1= "INSERT INTO contactsdata (firstname,middlename,lastname,nickname,gender,dob,address,city,state,pin,country,phone1,phone2,phone3,email1,email2,webs,contactgroup) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                            val1 = (VFirstName.get(),VMiddleName.get(),VLastName.get(),VNickName.get(),VGender.get(),VDOB.get(),VAddress.get(),VCity.get(),VState.get(),VPIN.get(),VCountry.get(),VPhone1.get(),VPhone2.get(),VPhone3.get(),VEmail1.get(),VEmail2.get(),Vwebs.get(),VGroup.get())
                            mycursor1.execute(sql1,val1)
                            mydb.commit()
                            clear_fields()#clear the fields
                            messagebox.showinfo("Saved!", "Record Saved successfully ")
                            add_contact_window.destroy()
                            refresh()
                        else:                                      #Contact with same name exists already
                            messagebox.showerror("Error", "Contact with same name already exists!")
                            add_contact_window.focus_force() #To bring the window in focus


            else:                   #Editing a contact
                    def saveit():
                        if(VFirstName.get()==""):
                            messagebox.showerror("Error", "First name field is empty")
                            add_contact_window.focus_force() #To bring the window in focus
                        else:
                            mycursor2 = mydb.cursor()
                            sql2= "UPDATE contactsdata SET firstname = ?,middlename = ? ,lastname=?,nickname=?,gender=?,dob=?,address=?,city=?,state=?,pin=?,country=?,phone1=?,phone2=?,phone3=?,email1=?,email2=?,webs=?,contactgroup=? WHERE _id = ? "
                            val2 = (VFirstName.get(),VMiddleName.get(),VLastName.get(),VNickName.get(),VGender.get(),VDOB.get(),VAddress.get(),VCity.get(),VState.get(),VPIN.get(),VCountry.get(),VPhone1.get(),VPhone2.get(),VPhone3.get(),VEmail1.get(),VEmail2.get(),Vwebs.get(),VGroup.get(),id_reference)
                            mycursor2.execute(sql2,val2)
                            mydb.commit()
                            clear_fields()#clear the fields
                            messagebox.showinfo("Updated!", "Record Updated successfully ")
                            add_contact_window.destroy()
                            refresh()
                            
            button1 = Button(canvas_contact_window, text ="   Save ")
            save_icon=PhotoImage(file='icons/save.png', master=add_contact_window)
            button1.configure(bg='white',activebackground = "#33B5E5", relief = FLAT, image=save_icon, compound=LEFT,command=saveit,padx=10)
            button1_window = canvas_contact_window.create_window(400, 205, anchor=NW, window=button1)
            
            button3 = Button(canvas_contact_window, text ="   Cancel ")
            cancel_icon=PhotoImage(file='icons/cancel.png', master=add_contact_window)
            button3.configure(bg='white',activebackground = "white", relief = FLAT, image=cancel_icon, compound=LEFT, command=lambda:[clear_fields(),add_contact_window.destroy()],padx=10)
            button3_window = canvas_contact_window.create_window(400, 265, anchor=NW, window=button3)


            add_contact_window.mainloop()

    #new contact
            
    new_icon=PhotoImage(file='icons/new.png')
    new=Menu(main_menu, tearoff=False)      #if tearoff is not False, then there will appear a dotted line & on clicking that it will come out of its place and float i.e. tearoff
    id_reference=-1
    new.add_command(label=' Add new contact',image=new_icon,compound='left', command=lambda:ContactEditor(id_reference))
    
    #delete contact
    delete=Menu(main_menu, tearoff=False)
    def delete_all():
            option = messagebox.askyesno("Caution!", "Pressing Yes Will Delete All Your Records")
            if option:
                    mycursor = mydb.cursor()
                    Delete_all_rows = "DELETE FROM contactsdata" #not truncate, unlike MySQL
                    mycursor.execute(Delete_all_rows)
                    mydb.commit()
                    messagebox.showinfo("Deleted!", "All Records Deleted successfully ")
                    refresh()
            else:
                    pass

    delete_all_icon=PhotoImage(file='icons/deleteall.png')
    delete.add_command(label=' Delete all contacts',image=delete_all_icon,compound='left',command=delete_all)


    #Color-theme button...
    color_theme=Menu(main_menu, tearoff=False)

    default_icon = PhotoImage(file='icons/light_plus.png')
    light_plus_icon = PhotoImage(file='icons/light_blue.png')
    dark_icon = PhotoImage(file='icons/dark.png')
    red_icon = PhotoImage(file='icons/red.png')
    monokai_icon = PhotoImage(file='icons/monokai.png')
    night_blue_icon = PhotoImage(file='icons/night_blue.png')

    theme_choice = StringVar(None, Theme_Name) #variable to store which theme is chosen 
    
    color_icons = (default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon) #using tuple
    color_dict = { #dictionary... storing bg and fg colors
        '  Default':('#474747','#e0e0e0','#474747'),
        '  Light Blue' : ('#c4c4c4', '#CDEDF6','black'),
        '  Dark' : ('#c4c4c4', '#2d2d2d','#c4c4c4'),
        '  Red' : ('#2d2d2d', '#ffe8e8','#2d2d2d'),
        '  Monokai' : ('#d3b774', '#474747','#d3b774'),
        '  Night Blue' :('#ededed', '#6b9dc2','#ededed')
    }

    def change_theme():
        chosen_theme = theme_choice.get()
        color_tuple = color_dict.get(chosen_theme)
        global fg_color, bg_color ,text_color
        fg_color, bg_color, text_color = color_tuple[0], color_tuple[1], color_tuple[2]
                
        canvas.config(background=bg_color)
        canvas2.config(background=fg_color)
        
        search_contact.config(background=bg_color,foreground=fg_color)
        edit_contact.config(background=bg_color,foreground=fg_color)
        delete_contact.config(background=bg_color,foreground=fg_color)
        clearbutton.config(background=bg_color,foreground=fg_color)
        note_text.config(background=bg_color,foreground=fg_color)

        search()

        FirstName_label.config(background=fg_color,foreground=bg_color)
        MiddleName_label.config(background=fg_color,foreground=bg_color)
        LastName_label.config(background=fg_color,foreground=bg_color)
        DOB_label.config(background=fg_color,foreground=bg_color)
        Phone1_label.config(background=fg_color,foreground=bg_color)
        Phone2_label.config(background=fg_color,foreground=bg_color)
        Email1_label.config(background=fg_color,foreground=bg_color)
        create_canvas2()
        
        mycursor=mydb.cursor()
        mycursor.execute("UPDATE ColorTheme SET (themename,colornames) = (?,?) WHERE _id = 1",(theme_choice.get(),' '.join(color_tuple),))
        mydb.commit()
        
    count = 0 
    for i in color_dict: #to add radiobuttons for all themes
        color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=LEFT, command=change_theme)
        count += 1 


    #Tools
    tools=Menu(main_menu, tearoff=False)
    #Drop-down menu of Tools
     #Backup contacts to csv
    backup_icon=PhotoImage(file='icons/backup.png')
     
    def exportcsv():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM contactsdata")
        result=mycursor.fetchall()
        with open(fd.asksaveasfilename(title='Save the file...',initialfile='Contacts_Data.csv', filetypes=[("csv", ".CSV")]),'a', newline='') as f: #newline='' is needed so that there is no empty newline after every row
            w = csv.writer(f, dialect='excel')
            for record1 in result:
                record=list(record1)
                record.pop(0)
                w.writerow(record)
#####ERROR WHEN CANCELLED MIDWAY
                
        messagebox.showinfo("Exported!", "All Records Saved Locally in Contacts_Data.csv ")
    tools.add_command(label='  Backup Contacts To CSV',image=backup_icon, compound=LEFT,command=exportcsv)  #exports as csv


     #Import contacts from csv
    import_icon=PhotoImage(file='icons/import.png')
     
    def importcsv():
        #opens a dialog box to choose the file
        filename = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))

        my_file = open(filename)
        parsed_data = csv.reader(my_file)
        for row in parsed_data:
            # row <--- a list of strings
            if row: # if the list is not empty

                #To check if the contact does not exist already
                sql = "SELECT * FROM contactsdata WHERE firstname = ?"
                name = (row[0],)
                mycursorx = mydb.cursor()
                resultx = mycursorx.execute(sql,name)
                resultx = mycursorx.fetchall()
                if(row[0]==""):
                    pass
                elif not resultx:                           #Contact with same name does not exist already
                    mycursor = mydb.cursor()
                    sql1= "INSERT INTO contactsdata (firstname,middlename,lastname,nickname,gender,dob,address,city,state,pin,country,phone1,phone2,phone3,email1,email2,webs,contactgroup) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                    val1 = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17])
                    mycursor.execute(sql1,val1)
                    mydb.commit()
                else:                                      #Contact with same name exists already
                    pass
        
        messagebox.showinfo("Imported!", "All Records Added in Contacts (Contacts with names already present were skipped)")
        refresh()
        
    tools.add_command(label='  Import Contacts From CSV',image=import_icon, compound=LEFT,command=importcsv)  #imports a csv file

     #Add/Edit Groups
    group_icon=PhotoImage(file='icons/group_icon.png')

     #Add/Edit Groups
    group_icon=PhotoImage(file='icons/group_icon.png')
    
    def add_edit_group():
            add_edit_group_window = Tk()
            add_edit_group_window.geometry('300x325')
            add_edit_group_window.minsize(300, 325) #min width,height
            add_edit_group_window.maxsize(300, 325) #min width,height
            add_edit_group_window.focus_force() #To bring the window in focus
            add_edit_group_window.geometry("{}x{}+{}+{}".format(300, 325, int((add_edit_group_window.winfo_screenwidth()/2) - (300/2)), int((add_edit_group_window.winfo_screenheight()/2) - (325/2))))
            add_edit_group_window.title("Groups")
            main_icon = PhotoImage(file = "icons/ContactsIcon1.png", master=add_edit_group_window)
            add_edit_group_window.iconphoto(False, main_icon)
            add_edit_group_window.configure(bg='white')

            fog_color, bog_color = 'black','white'

            def search_and_next():
                    searched = VGroup_name.get()
                    sql = "SELECT * FROM grouplist WHERE group_name = ? COLLATE NOCASE"
                    name = (searched,)
                    mycursor = mydb.cursor()
                    myresult = mycursor.execute(sql,name)
                    myresult = mycursor.fetchall()
                    if searched=="": #Nothing Entered
                        pass
                    elif not myresult: #Enterred group Not found, so display button to add
                        Click_me.configure(state='disabled')
                        def add_group():
                                mycursor = mydb.cursor()
                                sql = "INSERT INTO grouplist (group_name,extra_id) VALUES (?,?)"
                                val = (searched,'Added_by_user')
                                mycursor.execute(sql,val)
                                mydb.commit()
                                messagebox.showinfo("Saved!", "Group Added successfully ")
                                add_edit_group_window.destroy()                        
                        button_add_group = Button(add_edit_group_window, text ="   Add in Groups")
                        global add_group_icon
                        add_group_icon=PhotoImage(file='icons/add_group.png', master=add_edit_group_window)
                        button_add_group.configure(bg=bog_color,activebackground = "#33B5E5", relief = SOLID, image=add_group_icon, compound=LEFT,command=add_group)
                        button_add_group.place(x=5,y=45)
                    else:            #Enterred group found and diplaying buttons to edit or delete
                        Click_me.configure(state='disabled')
                        def edit_group():
                                if(VGroup_name.get()==""):
                                    messagebox.showerror("Error", "Group name field is empty")
                                else:
                                    mycursor = mydb.cursor()
                                    sql= "UPDATE grouplist SET group_name = ?,extra_id = ? WHERE group_name = ? COLLATE NOCASE"
                                    val=(VGroup_name.get(),'Edited_by_user',searched)
                                    mycursor.execute(sql,val)
                                    mydb.commit()
                                    messagebox.showinfo("Updated!", "Group name Updated successfully ")
                                    add_edit_group_window.destroy()
                        def del_group():
                                mycursor = mydb.cursor()
                                sql= "DELETE FROM grouplist WHERE group_name = ? COLLATE NOCASE"
                                val= searched
                                mycursor.execute(sql,(val,))
                                mydb.commit()
                                messagebox.showinfo("Deleted!", "Deleted the group successfully ")
                                add_edit_group_window.destroy()

                        note_label= Label(add_edit_group_window,text="To rename, change\nthe enterred name\nto new name\nand press Rename",bg=bog_color,fg=fog_color)
                        note_label.place(x=130,y=95)
                        button_edit_group = Button(add_edit_group_window, text ="   Rename ")
                        global edit_group_icon
                        edit_group_icon=PhotoImage(file='icons/edit_group.png', master=add_edit_group_window)
                        button_edit_group.configure(bg=bog_color,activebackground = "#33B5E5", relief = SOLID, image=edit_group_icon, compound=LEFT,command=edit_group)
                        button_edit_group.place(x=5,y=95)
                        
                        button_del_group = Button(add_edit_group_window, text ="   Delete    ")
                        global del_group_icon
                        del_group_icon=PhotoImage(file='icons/del_group.png', master=add_edit_group_window)
                        button_del_group.configure(bg=bog_color,activebackground = "#33B5E5", relief = SOLID, image=del_group_icon, compound=LEFT,command=del_group)
                        button_del_group.place(x=5,y=175)

            VGroup_name = StringVar(add_edit_group_window)

            GroupName = Label(add_edit_group_window, text="Enter Group Name: ", font=(12),bg=bog_color,fg=fog_color)
            GroupName.place(x=5,y=5)
            EFirstName=Entry(add_edit_group_window, bd=1,relief="solid", textvariable=VGroup_name)
            EFirstName.place(relx=0.75,y=17,anchor="center")
            
            Click_me = Button(add_edit_group_window)
            global Click_me_icon  #when you return from a function which stored an image in a local variable, the image is cleared, hence make it global
            Click_me_icon = PhotoImage(file='icons/click_me.png', master=add_edit_group_window)
            Click_me.configure(bg=bog_color,fg=fog_color, image=Click_me_icon,compound=LEFT,command=search_and_next)
            Click_me.place(relx=0.8,y=35)

            Cancel_button = Button(add_edit_group_window, text="  Cancel")
            global Cancel_button_icon  #when you return from a function which stored an image in a local variable, the image is cleared, hence make it global
            Cancel_button_icon = PhotoImage(file='icons/cancel.png', master=add_edit_group_window)
            Cancel_button.configure(bg=bog_color,fg=fog_color, image=Cancel_button_icon,compound=LEFT,command=lambda:add_edit_group_window.destroy())
            Cancel_button.place(relx=0.8,rely=0.8,anchor="center")

            Note_about=Label(add_edit_group_window, text="Enter the Group's Name\nYou want to Add/Rename/Delete",bg=bog_color,fg=fog_color)
            Note_about.place(relx=0.5,rely=0.93,anchor="center")
   
    tools.add_command(label='  Add/Edit Groups',image=group_icon, compound=LEFT,command=add_edit_group)

    #Info

    info_icon=PhotoImage(file='icons/info.png')
    info=Menu(main_menu, tearoff=False)
    info.add_command(label='   About', image=info_icon, compound=LEFT, command=aboutus)



    #--------------------------------cascade... without cascading menu won't be visible
    main_menu.add_cascade(label='Add ', menu=new)
    main_menu.add_cascade(label='Delete ', menu=delete)
    main_menu.add_cascade(label='Theme ', menu=color_theme)
    main_menu.add_cascade(label='Tools ', menu=tools)
    main_menu.add_cascade(label='Info ', menu=info)

    main_application.config(menu=main_menu)  #we don't use grid/pack for main menu
    ##################################################### End of Main menu ################################################

    #-------------------------------------------------------- Heading frame ---------------------------------------------------

    heading_frame = Frame(main_application, height=100, bg='white')
    heading_frame.pack(fill=X,side=TOP)

    main_icon= PhotoImage(file='icons/ContactsIcon2.png')
    main_icon_label= Label(heading_frame, image=main_icon, bg='white')
    main_icon_label.place(relx = 0.008, rely = 0.1)#relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0,
                                                   #as a fraction of the height and width of the parent widget.

    heading1 = Label(heading_frame, text=" Contacts",font=("Arial Rounded MT Bold", 26),bg='white',fg='black')
    heading1.place(x = 90, rely = 0.1)

    heading2 = Label(heading_frame, text="   My Address Book",font=("", 10),bg='white',fg='black')
    heading2.place(x = 90, rely = 0.5)

    mycursor9 = mydb.cursor() #Without buffered, it will give error as cursor is used again in canvas2
    mycursor9.execute("SELECT COUNT(*) FROM contactsdata")   #query for count
    row_count = Label(heading_frame, text="Total No. of Contacts: "+str(list(mycursor9.fetchone())[0]),font=("", 10),bg='white',fg='black')
    row_count.place(relx = 0.8, rely = 0.5)
    
    ##################################################### End of Heading frame ################################################

    #--------------------------------------------------ContactDetails Frame ---------------------------------------------------

    #############################################################

    ContactDetails_frame = Frame(main_application,width=320,bd=3, relief=RIDGE)
    ContactDetails_frame.pack(side=LEFT,fill=BOTH)
            
    canvas = Canvas(ContactDetails_frame,bg='#e0e0e0',scrollregion=(0,0,0,800), highlightbackground='white', bd=0, highlightthickness=0)
    canvas.pack(side=LEFT,fill=BOTH)

    scrollbar = Scrollbar(ContactDetails_frame,orient=VERTICAL)
    scrollbar.pack(side=RIGHT,fill=Y)

    #Attach scrollbar to canvas
    canvas.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=canvas.yview)


    #Binding MouseWheel to the canvas
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind("<MouseWheel>", on_mousewheel)


    ##############################################
    
    def search():
        searched=search_box.get()
        sql = "SELECT * FROM contactsdata WHERE firstname = ? COLLATE NOCASE"
        name = (searched,)
        mycursor=mydb.cursor()
        result = mycursor.execute(sql,name)
        result=mycursor.fetchall()
        l=[]
        for y in result:
            l.append(y)
        if searched=="": #Nothing Entered
                pass
        elif not result: #Enterred contact Not found 
            messagebox.showinfo("Not Found!", " Record not found in contacts... ")
        else:            #Enterred contact found and displaying the details
            heading3 = Label(canvas, text="Details",font=(12),bg=bg_color,fg=text_color)
            canvas.create_window(160,155, window=heading3)
            for index,x in enumerate(result):
                col,v,list_i = 0,175,0

                global id_reference
                id_reference = str(x[0])
                headingtext=["S. No:","First name: ","Middle name: ","Last name: ","Nick name: ","Gender: ","Date of birth: ","Address: ","City: ","State: ","PIN/ZIP: ","Country: ","Phone(1): ","Phone(2): ","Phone(3): ","Email(1): ","Email(2): ", "Website: ","Group: "]
                for y in x:
                    if(list_i!=0):#Skipping id i.e. 0th in list_i
                        searched_label = Label(canvas,text=headingtext[list_i]+str(y),bg=bg_color,fg=text_color)
                        canvas.create_window(10,v*(index+1),window=searched_label, anchor="w")
                    col+=1
                    v+=20
                    list_i+=1
                break

    def DeleteContact(id_reference):
        if(id_reference==-1):
            pass
        else:
                mycursor1 = mydb.cursor()
                sql3= "DELETE FROM contactsdata WHERE _id = ? "
                val3= str(id_reference)
                mycursor1.execute(sql3,(val3,))
                mydb.commit()
                messagebox.showinfo("Deleted!", "Deleted contact successfully ")
                refresh()
    def EditContact(id_reference):
        if(id_reference==-1):
            pass
        else:
            ContactEditor(id_reference)

    search_box=Entry(canvas, width=9,font=('Arial',20))
    canvas.create_window(25,25, window=search_box,anchor="w")

    search_contact=Button(canvas,text="Search")
    search_icon=PhotoImage(file='icons/search.png', master=main_application)
    search_contact.configure(bg=bg_color,fg=text_color, image=search_icon, compound=LEFT,command=search,padx=10,borderwidth=1,relief='solid')
    canvas.create_window(250,25, window=search_contact)

    edit_contact=Button(canvas,text="Edit")
    edit_icon=PhotoImage(file='icons/edit.png', master=main_application)
    edit_contact.configure(bg=bg_color,fg=text_color, image=edit_icon, compound=LEFT,command=lambda:EditContact(id_reference),padx=10,borderwidth=1,relief='solid')
    canvas.create_window(50,70, window=edit_contact)

    delete_contact=Button(canvas,text="Delete")
    delete_contact_icon=PhotoImage(file='icons/delete.png', master=main_application)
    delete_contact.configure(bg=bg_color,fg=text_color, image=delete_contact_icon, compound=LEFT,command=lambda:DeleteContact(id_reference),padx=10,borderwidth=1,relief='solid')
    canvas.create_window(172,70, window=delete_contact)

    clearbutton = Button(canvas, text ="Clear")
    clear_icon=PhotoImage(file='icons/clear.png', master=main_application)
    clearbutton.configure(bg=bg_color,fg=text_color,activebackground = "light green", image=clear_icon, compound=LEFT,command=refresh,padx=10,borderwidth=1,relief='solid')
    canvas.create_window(250,70, window=clearbutton,anchor="w")
    
    note_text=Label(canvas,text="NOTE:   Enter the First name to search\n\n   After a search, press Clear button :\n\tBefore going for another Search\n\tOR\n\tBefore adding any New Contact",bg=bg_color,fg=text_color)
    canvas.create_window(10,640, window=note_text,anchor="w")
    
    ############################################### End of ContactDetails Frame ##########################################

    #----------------------------------------------------- Entry display ---------------------------------------------------

    EntryDisplay_frame = Frame(main_application, bd=3, relief=RIDGE)
    EntryDisplay_frame.pack(fill=BOTH, side=RIGHT, expand=True)

    canvas2= Canvas(EntryDisplay_frame,bg=fg_color,scrollregion=(0,0,0,8000), highlightbackground='white', bd=0, highlightthickness=0)
    canvas2.pack(side=LEFT,fill=BOTH,expand=True)

    scrollbar2=Scrollbar(EntryDisplay_frame,orient=VERTICAL)
    scrollbar2.pack(side=RIGHT,fill=Y)

    #Attach scrollbar to canvas2
    canvas2.config(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=canvas2.yview)

    #Binding MouseWheel to the canvas2
    def on_mousewheel(event):
        canvas2.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas2.bind("<MouseWheel>", on_mousewheel)
    
    #MAIN DISPLAY...

     #Headings
    k=0.1
    FirstName_label=    Label(canvas2,text="First Name  ",font=("Arial BOLD", 12),bg=fg_color,fg=bg_color)
    canvas2.create_window(k*120,0, window=FirstName_label, anchor="nw")
    k+=1
    MiddleName_label=   Label(canvas2,text="Middle Name  ",font=("Arial BOLD", 12),bg=fg_color,fg=bg_color)
    canvas2.create_window(k*120,0, window=MiddleName_label, anchor="nw")
    k+=1
    LastName_label=     Label(canvas2,text="Last Name  ",font=("Arial BOLD", 12),bg=fg_color,fg=bg_color)
    canvas2.create_window(k*120,0, window=LastName_label, anchor="nw")
    k+=1
    DOB_label=          Label(canvas2,text="Birth Day  ",font=("Arial BOLD", 12),bg=fg_color,fg=bg_color)
    canvas2.create_window(k*120,0, window=DOB_label, anchor="nw")
    k+=1
    Phone1_label=       Label(canvas2,text="Phone 1  ",font=("Arial BOLD", 12),bg=fg_color,fg=bg_color)
    canvas2.create_window(k*120,0, window=Phone1_label, anchor="nw")
    k+=1
    Phone2_label=       Label(canvas2,text="Phone 2  ",font=("Arial BOLD", 12),bg=fg_color,fg=bg_color)
    canvas2.create_window(k*120,0, window=Phone2_label, anchor="nw")
    k+=1
    Email1_label=       Label(canvas2,text="Email 1  ",font=("Arial BOLD", 12),bg=fg_color,fg=bg_color)
    canvas2.create_window(k*120,0, window=Email1_label, anchor="nw")
     #Headings end

     #Query the Database:
    def create_canvas2():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM contactsdata ORDER BY firstname COLLATE NOCASE ASC") #COLLATE NOCASE ASC: Collate the data in acending order without being "case sensitive"<--VIMP... for descending add: DESC instead of ASC
        result=mycursor.fetchall()
        for index,x in enumerate(result):
            col=0.1
            for y in range(len(x)):
                if(y==1 or y==2 or y==3 or y==6 or y==12 or y==13 or y==15):
                        lookup_label = Label(canvas2,text=x[y],bg=fg_color,fg=bg_color)
                        canvas2.create_window(col*120,25*(index+1),window=lookup_label, anchor="nw")
                        col+=1
                        
    create_canvas2()
    
    ################################################## End of Entry display ################################################
    change_theme() #calling for the updation of checkbutton in menubar as well as colors from database
    main_application.mainloop()

if __name__ == "__main__":                  #To run the main program indiviually, very necessary to execute the whole application at starting
    mainapplication()
