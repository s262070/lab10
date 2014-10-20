##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
#House outline
drawpad.create_rectangle(280,230,520,430)
drawpad.create_line(280,230,400,110)
drawpad.create_line(520,230,400,110)
#Square Windows and a Door
drawpad.create_rectangle(320,270,350,300)
drawpad.create_rectangle(440,270,470,300)
drawpad.create_rectangle(410,430,380,350)
drawpad.create_rectangle(320,380,350,410)
drawpad.create_rectangle(440,380,470,410)

root.mainloop()