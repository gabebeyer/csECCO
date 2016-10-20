from Tkinter import * 
import tkMessageBox 
import random
import numpy as np


class Minesweeper():
    """docstring for minesweeper"""
    def __init__(self, master):
        
        self.master = master

        self.buttons = [] 

        #add buttons to array
        for x in range(8):

            row = []

            for i in range(8):
                
                row.append( [Button(master, text=str((x,i)) ) ])

            self.buttons.append(row)


        rowVar = 0
        #put buttons on screen
        for row in self.buttons:
            
            colVar = 0
            
            for button in row:
                
                button[0].grid(row = rowVar, column = colVar)

                colVar += 1

            rowVar += 1
        
        for row in self.buttons:
            
            for b in row:

                print(b[0].config('text'))


def main():
    global root
    root = Tk()
    root.title("Minesweeper")
    minesweeper = Minesweeper(root)
    root.mainloop()

if __name__ == "__main__":
    main()