from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

# Override the settings of the window
root.configure(bg="gray")
root.geometry(f'{settings.width}x{settings.height}')
root.resizable(False,False)
root.title("MINESWEEPER  GAME")


top_frame=Frame(
    root,
    bg= 'gray',
    width= settings.width,
    height=utils.height_prct(25)
)
game_title=Label(
    top_frame,
    bg='gray',
    fg='White',
    text= "MINESWEEPER GAME",
    font=("ROBOTA",48)
)
game_title.place(
    x=utils.width_prct(25),
    y=0
)

top_frame.place(x=0,y=0)

left_frame=Frame(
    root,
    bg= 'gray',
    width= utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0,y=utils.height_prct(25))

center_frame=Frame(
    root,
    bg='gray',
    width=utils.width_prct(75),
    height= utils.height_prct(75)

)
center_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c=Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column= x, row= y
        )

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame )
Cell.cell_count_label_object.place(
    x=0, y=0
)


Cell.randomize_mines()


# Run the Window
root.mainloop()