from tkinter import *
from os import system
from platform import system as platform

def focus_hack():
    if platform() == 'Darwin':  # How Mac OS X is identified by Python
        system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

root = Tk()

root.title("Sample App")
window_height = 400
window_width = 400
root.resizable(False, False)
display_offset_x = 140
display_offset_y = 60

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
x_cordinate = x_cordinate - display_offset_x
y_cordinate = int((screen_height/2) - (window_height/2))
y_cordinate = y_cordinate - display_offset_y


root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

lbl = Label(root, text="Hello")

lbl.place(x=160, y=50)

btn = Button(root, text="Click Me")
btn.place(x=160, y=100)

#Bring Window to front
#root.grab_set()
root.attributes('-topmost',True)
root.focus_set()
focus_hack()
root.lift()
root.mainloop()