from tkinter import *

# creates root widget comes first in any tkinter app
root = Tk()

# define a fuction to tell the button what to do
def myClick():
    myLabel = Label(root, text="i have been clicked")
    myLabel.pack()


# creates a button named myButton tell it where you want the button i:e root and what text to display
# use state to tell what state its in i:e state=DISABLED
# padx and pady will determine the size of the button i:e padx=50, pady=50
# fg changes foreground colour and bg changes background colour
# use command and the function you want the button to use to tell the button its command
myButton = Button(root, text="Click Me", command=myClick)

# uses .pack function which will push it to the gui with no control as to look and size
myButton.pack()







# uses root widget with mainloop which displays the gui and keeps it looping till closed
root.mainloop()
