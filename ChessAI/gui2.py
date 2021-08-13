from tkinter import *

root = Tk()
class Interface():
    def __init__(self, window):
        self.window = window
        window.title("Sudoku Solver")

        font = ('Arial', 20)
        color = 'white'

        # Create solve and clear button and link them to Solve and Clear methods
        solve = Button(window, text = 'Solve', command = None)
        solve.grid(column=3,row=20)
        clear = Button(window, text = 'Clear', command = None)
        clear.grid(column = 5,row=20)

        # Initialise empty 2D list
        self.board  = []
        for row in range(9):
            self.board += [["","","","","","","","",""]]

        for row in range(9):
            for col in range(9):
                # Change color of cells depending on position in grid
                if (row < 3 or row > 5) and (col < 3 or col > 5):
                    color = 'white' 
                elif (row >= 3 and row < 6) and (col >=3 and col < 6):
                    color = 'white'
                else:
                    color = 'grey'
                
                # Make each cell of grid a entry box and store each user entry into the filledBoard 2D list
                self.board[row][col] = Entry(window, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 2,
                                          highlightcolor = 'yellow', highlightthickness = 0, highlightbackground = 'black')
                self.board[row][col].grid(row = row, column = col)

Interface(root)
root.mainloop()