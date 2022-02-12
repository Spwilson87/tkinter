from tkinter import *

# creates root widget comes first in any tkinter app
root = Tk()

# entry creates an input field  to type in
# use width and height for size of input field, also us fg and bg to change colours
# borderwidth makes the border of the box wider
inputBox = Entry(root, width=50)
inputBox.pack()
# insert will display the text in the box 0=index number,
# inputBox.insert(0, "Enter Your Name")
# get function will get what you have typed in the input field i:e inputBox.get()

# define a fuction to tell the button what to do
def myClick():
    # uses .get and displays what you put in the inputBox and concats hello with .get
    hello = "Hello " + inputBox.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


# creates a button named myButton tell it where you want the button i:e root and what text to display
# use state to tell what state its in i:e state=DISABLED
# padx and pady will determine the size of the button i:e padx=50, pady=50
# fg changes foreground colour and bg changes background colour
# use command and the function you want the button to use to tell the button its command
myButton = Button(root, text="Enter Your Name", command=myClick)

# uses .pack function which will push it to the gui with no control as to look and size
myButton.pack()







# uses root widget with mainloop which displays the gui and keeps it looping till closed
root.mainloop()
