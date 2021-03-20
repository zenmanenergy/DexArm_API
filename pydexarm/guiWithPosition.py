# guiWithPosition.py
# Steve Nelson 3/20/2021
# This creates a very simple graphical interface for the Rotrics dexarm
# It displays instructions providing a way to move the arm using the keyboard input
# It displays the current position of the arm

from pydexarm import Dexarm

# this is a library for creating a graphical user interface
from tkinter import * 


# this is the dexarm instance
dexarm = Dexarm(port="COM5")
# This is the tkinter GUI library 
window = Tk()
window.title("Dexam gui with position information")
window.geometry('600x400')



data=Label(window,text='Not connected', font = ("Helvetica",18), bg="yellow", 
         bd=1,relief="solid",
         width=50, anchor="w",
         justify="left")
data.grid(column=0,row=0,columnspan=4)

# text instructions
instructions = """Use these keys to move the arm with the keyboard:
pgup - move up
pgdn - move down
right arrow - right
left arrow - left
up arrow - forward
down arrow - backward.
home - move to home position"""
instructions=Label(window, 
		 text=instructions,
		 font = ("Helvetica",18),
         bd=1,relief="solid",
         width=50, anchor="w",
         justify="left")
instructions.grid(column=0,row=1,columnspan=4)

def armPositionData():
    postionData = "X:" + str(dexarm.x) + " Y:" +str(dexarm.y) + " Z:"+str(dexarm.z)
    postionData += " module:" + dexarm.module_type + ":" + dexarm.module_status
    print(data.cget('text'))
    data.config(text=postionData)
    

# the following functions are for handling keyboard input
def leftKey(event):
    print("left")
    dexarm.move_to(dexarm.x-1, dexarm.y, dexarm.z)
    armPositionData()

def rightKey(event):
    print("right")
    dexarm.move_to(dexarm.x+1, dexarm.y, dexarm.z)
    armPositionData()

def upKey(event):
    print("upKey")
    dexarm.move_to(dexarm.x, dexarm.y+1, dexarm.z)
    armPositionData()

def downKey(event):
    print("downKey")
    dexarm.move_to(dexarm.x, dexarm.y-1, dexarm.z)
    armPositionData()

def pageUpKey(event):
    print("pageUpKey")
    dexarm.move_to(dexarm.x, dexarm.y, dexarm.z+1)
    armPositionData()

def pageDownKey(event):
    print("pageDownKey")
    dexarm.move_to(dexarm.x, dexarm.y, dexarm.z-1)
    armPositionData()

def plusKey(event):
    print("plusKey")
    dexarm.air_picker_pick()
    armPositionData()
    
def minusKey(event):
    print("minusKey")
    dexarm.air_picker_place()
    armPositionData()

def homeKey(event):
    print("home")
    dexarm.go_home()
    armPositionData()



armPositionData()


# sets the height and width of the window
canvas = Canvas(window, width=600, height=400)






# This binds the keyboard presses to the functions above
window.bind('<Left>', leftKey)
window.bind('<Right>', rightKey)
window.bind('<Up>', upKey)
window.bind('<Down>', downKey)
window.bind('<Prior>', pageUpKey)
window.bind('<Next>', pageDownKey)
window.bind('<Home>', homeKey)
window.bind('<plus>', plusKey)
window.bind('<minus>', minusKey)





window.mainloop()


