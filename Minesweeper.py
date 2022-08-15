from tkinter import *

root = Tk()

# Override the settings of the window
root.configure(bg="black")
root.geometry('1440x720')
root.resizable(False,False)
root.title("MINESWEEPER  GAME")


top_frame=Frame(
    root,
    bg= 'gray',# can be changed
    width= 1440,
    height=90
)
top_frame.place(x=0,y=0)

left_frame=Frame(
    root,
    bg= 'yellow',
    width= 100,
    height=720
)
left_frame.place(x=0,y=90)
# Run the Window
root.mainloop()