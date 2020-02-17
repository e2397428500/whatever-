import tkinter as tk
import random

#FIRST: Implement and test your Pokemon class below

     
#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        self.initial = 0 
        tk.Frame.__init__(self, master)
        master.minsize(width=700, height=400)
        master.maxsize(width=700, height=400)
        master.title("Studying results text")
        self.createWidgets()

    def createWidgets(self):
        self.studyButton = tk.Button(self)
        self.studyButton["text"] = "studying"
        self.studyButton.pack()
##    def notstudy(self):
##        
##    def effi_study(self):
##        figscore = random.randint(50,100)
##        self.intial += figscore
##        #next page
##    def ineffi_study(self):
##        figscore = random.randint(10,70)
##        self.intial += figscore
##        #next page

app = SafariSimulator(tk.Tk())
app.mainloop()
