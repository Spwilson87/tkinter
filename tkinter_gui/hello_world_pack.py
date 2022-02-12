from tkinter import *

# creates root widget comes first in any tkinter app
root = Tk()

# creates label widget called myLabel usin Label function, in the () it uses the root widget defined at the start text of the label is hello world
myLabel = Label(root, text="Hello World")

# uses myLabel with .pack function which will push it to the gui with no control as to look and size
myLabel.pack()

# uses root widget with mainloop which displays the gui and keeps it looping till closed
root.mainloop()
