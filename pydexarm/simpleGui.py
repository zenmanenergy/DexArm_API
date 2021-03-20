# simpleGui.py
# Steve Nelson 3/20/2021
# This is to create a very simple graphical interface for the Rotrics dexarm
# It ONLY displays instructions and provides a way to move the arm using the keyboard input

from pydexarm import Dexarm

# this is a library for creating a graphical user interface
import tkinter


# this is the dexarm instance
dexarm = Dexarm(port="COM5")



# the following functions are for handling keyboard input
def leftKey(event):
    print("left")
    dexarm.move_to(dexarm.x-1, dexarm.y, dexarm.z)

def rightKey(event):
    print("right")
    dexarm.move_to(dexarm.x+1, dexarm.y, dexarm.z)

def upKey(event):
    print("upKey")
    dexarm.move_to(dexarm.x, dexarm.y+1, dexarm.z)

def downKey(event):
    print("downKey")
    dexarm.move_to(dexarm.x, dexarm.y-1, dexarm.z)

def pageUpKey(event):
    print("pageUpKey")
    dexarm.move_to(dexarm.x, dexarm.y, dexarm.z+1)

def pageDownKey(event):
    print("pageDownKey")
    dexarm.move_to(dexarm.x, dexarm.y, dexarm.z-1)

def plusKey(event):
    print("plusKey")
    dexarm.air_picker_pick()
    
def minusKey(event):
    print("minusKey")
    dexarm.air_picker_place()

def homeKey(event):
    print("home")
    dexarm.go_home()



# This is the tkinter GUI library 
root = tkinter.Tk()

# sets the height and width of the window
canvas = tkinter.Canvas(root, width=600, height=400)



# text instructions
instructions = """Use these keys to move the arm with the keyboard:
pgup - move up
pgdn - move down
right arrow - right
left arrow - left
up arrow - forward
down arrow - backward.
home - move to home position"""
tkinter.Label(root, 
		 text=instructions,
		 font = ("Helvetica",18),
         bd=1,relief="solid",
         width=50, anchor="w",
         justify="left").pack(pady=20, ipady=10, ipadx=10)



# This binds the keyboard presses to the functions above
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)
root.bind('<Prior>', pageUpKey)
root.bind('<Next>', pageDownKey)
root.bind('<Home>', homeKey)
root.bind('<plus>', plusKey)
root.bind('<minus>', minusKey)





root.mainloop()


