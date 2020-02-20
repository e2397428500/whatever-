import random
from PIL import Image, ImageTk

root = Tk()
root.title("Studying plan")
root.geometry("600x440") # set starting size of window

(practice, notes, get_help, goclass) = input("enter the how important (practice, notes, getting help) 5and go to class to you in percentage") 
def display_checked() :
     red = red_var.get()# practice
     grey = grey_var.get() #Notes 
     green = green_var.get()# get help 
     blue = blue_var.get()# go to class

     score = red* practice + grey * notes + green * get_help + blue * goclass  
     likehood = score * 100
     return likehood
def likehood():
     chance = display_checked()
     lb1['text'] = 'My work help me to understand ' + str(chance) + "% of calculus  " 
     lb1.grid(row= 7, column = 2) 
     label = Label(root, text="I am just a random ", padx=20, pady=10)
     return chance
def goingtotest():
     if likehood() + random.randint(1,20) - random.randint(1,20) < 70:
          image = Image.open("2.png")
          zoom = 0.2
          pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])
          img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y))) 
          label = Label(root, image=img)
          label.image = img
          label.grid(row = 8,column =2)
          lb1['text'] = 'All these years of laziness will not pay off '
     else:
          image = Image.open("1.png")
          zoom = 1
          pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])
          img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y))) 
          label = Label(root, image=img)
          label.image = img
          label.grid(row = 10,column =2)
          lb1['text'] = 'All these years of hard work will pay off'
   
     
     
          
     
label = Label(root, text="I am just a random small program", padx=20, pady=10)
label.grid(row = 0, column = 2)
lb1 = Label(root)



red_var = IntVar()
b1= Checkbutton(root, width=10, text="practice",variable=red_var,  bg="red")
b1.grid(row=1, column = 1)
grey_var = IntVar()
b2 = Checkbutton(root, width=10, text="taking notes", variable=grey_var , bg="grey")
b2.grid(row=1, column = 3)
green_var = IntVar()
b3 = Checkbutton(root, width=10, text="get help",variable=green_var, bg="green")
b3.grid(row=2, column = 1)
blue_var = IntVar()
b4 = Checkbutton(root, width=10, text="go the class" ,variable=blue_var, bg="blue")
b4.grid(row=2, column = 3 )

Button(root, text="start reviewing", command=display_checked).grid(row=5)
Button(root, text="reflection", command=likehood).grid(row=6)
Button(root, text="testdate", command=goingtotest).grid(row=7)
mainloop() 

