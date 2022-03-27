import tkinter as tk
from tkinter import messagebox

class Window():    
    def __init__(self, QA):
        self.window = tk.Tk()
        self.var = tk.IntVar()   #Var to store score

        self.QA = QA        #All the question and answers
        self.questionNo=0   #To increment everytime for next question
        #First QnA from QA:        
        self.q_txt  = self.QA[self.questionNo][0]
        self.answer = self.QA[self.questionNo][1]
        
        self.window.title('Guess if you can')
        self.window.config(padx = 50, pady = 50, bg = '#130f4a')
        self.window.minsize(width = 400, height = 300)
        
        self.score = tk.Label(text = 'Score: 0',fg = 'white' ,bg = "#130f4a", font = ('Ariel', 12, 'bold'))
        self.score.grid(row = 0, column = 1)
        
        self.true = tk.PhotoImage(file = '_tick.png')
        self.false = tk.PhotoImage(file = '_cross.png')
        
        self.cnvs = tk.Canvas(self.window, width = 300, height= 250, bg = 'white', highlightthickness = 0)
        self.cnvs_txt = self.cnvs.create_text(300//2, 250//2, text = self.q_txt, font = ('Times 20 italic bold', 15), width = 200)
        self.cnvs.grid(row = 1, column = 0, columnspan = 2, pady = 20)


        self.tick_btn = tk.Button(self.window, image = self.true, highlightthickness = 0, bg = 'white', command = lambda:self.check_answer(True))
        self.tick_btn.grid(row = 2, column = 0, pady = 5)
        
        self.cross_btn = tk.Button(self.window, image = self.false, highlightthickness = 0, bg = 'white', command = lambda:self.check_answer(False))
        self.cross_btn.grid(row = 2, column = 1, pady =5)

        self.window.mainloop()

    def check_answer(self, val):
        #all questions done!
        if self.questionNo >= len(self.QA):
            print("Done!")
            messagebox.showinfo("Done!", "You have attempted all the questions.")
        else:
            if (val == True and self.answer == "true") or (val == False and self.answer == "false"):
                print("Correct")
                self.var.set(self.var.get()+1) #works as self.var+=1
                self.score["text"] = 'Score: '+str(self.var.get())
            else:
                #negative marking or do nothing
                print("Wrong")
                #I am  just blinking the screen background:
                self.window["bg"] = 'red'
                self.window.after(100, self.window_bg_normal)

            #Now move to next question
            self.questionNo+=1
            if self.questionNo < len(self.QA):
                self.q_txt = self.QA[self.questionNo][0]
                self.answer = self.QA[self.questionNo][1]
                self.cnvs.itemconfig(self.cnvs_txt, text = self.q_txt)
            else:   #last question done
                print("Your final score is "+str(self.var.get()))
                messagebox.showinfo("Done!", "Your final score is "+str(self.var.get()))

    def window_bg_normal(self):
        self.window["bg"] = '#130f4a'
        
