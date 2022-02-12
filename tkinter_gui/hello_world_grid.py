from tkinter import *

# creates root widget comes first in any tkinter app
root = Tk()

# creates label widget called myLabel usin Label function, in the () it uses the root widget defined at the start text of the label is hello world
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="This is my second label")
myLabel3 = Label(root, text="Space")

# uses .grid to display on the gui using row and column to tell where to display the labels it will ignore empty columns and rows
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myLabel3.grid(row=1, column=1)
# uses root widget with mainloop which displays the gui and keeps it looping till closed
root.mainloop()
