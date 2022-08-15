from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all=[]
    cell_count_label_object = None
    cell_count=settings.cells_count
    def __init__(self, x,y,is_mine=False):
        self.is_mine= is_mine
        self.is_opened= False
        self.cell_btn_object= None
        self.is_mine_candidate = False

        self.x=x
        self.y=y

        # append cell.all attribute
        Cell.all.append(self)
    def create_btn_object(self, location):
        btn= Button(
            location,
            height= 3,
            width=8,
        )
        btn.bind('<Button-1>', self.left_click_action) # LEFT CLICK
        btn.bind('<Button-3>', self.right_click_action) # RIGHT CLICK
        self.cell_btn_object=btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location ,
            bg='gray',
            fg='black',
            text=f"Cells Left:{Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label_object= lbl


    def left_click_action(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length==0:
                for cell_obj in self.surrounded_cell:
                    cell_obj.show_cell()
            self.show_cell()
            # If mines count is equal to cell not clicked
            if Cell.cell_count== settings.mines_count:
                ctypes.windll.user32.MessageBoxW(0, 'CONGRATULATIONS!!!', "YOU WON", 0)

        # Cancel Left and Right Click Action if cell is open
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
    def get_cell_by_axis(self,x,y):
        # Return a cell object based on the value of x and y
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell

    @property
    def surrounded_cell(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),

        ]
        cells = [cell for cell in cells if cell is not None]

        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter=0
        for cell in self.surrounded_cell:
            if cell.is_mine:
                counter+=1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -=1
            self.cell_btn_object.configure(text = self.surrounded_cells_mines_length)
            # Replace with newer number
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text= f"Cells Left:{Cell.cell_count}"
                )
            # If this is a mine candidate then to get back to the original state
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
        # Marked the cell as opened
        self.is_opened= True

    def show_mine(self):
        # A logic to itterturp
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'You clicked on a MINE!!!', "GAME  OVER",0)
        sys.exit()
    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate= True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate=False


    @staticmethod
    def randomize_mines():
        picked_cells= random.sample(
            Cell.all, settings.mines_count
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine= True
