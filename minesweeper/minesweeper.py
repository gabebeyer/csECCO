from Tkinter import * 
import tkMessageBox 
import random
import functools
import numpy as np


class Minesweeper():
    """docstring for minesweeper"""
    def __init__(self, master):
        
        self.master = master

        self.buttons = [] 

        self.bombPercent = 20

        #add buttons array
        #along with info about button
        # button , isBomb , location
        for x in range(8):
            row = []
            for i in range(8):           
                row.append([Button(master, text=str((x,i))) ,
                            1 if random.randint(0,100) < self.bombPercent else 0,
                            (x,i)
                    ])
            self.buttons.append(row)


        rowVar = 0
        #put buttons on screen
        #and sets up function for buttons
        for row in self.buttons:
            colVar = 0
            for button in row:
                x = (rowVar , colVar)

                button[0].grid(row = rowVar, column = colVar)
                
                self.buttons[rowVar][colVar][0].bind('<Button-1>',functools.partial(self.lClickWrap,param=self.buttons[rowVar][colVar]))

                colVar += 1
            rowVar += 1


    def lClickWrap(self,event,param):
        print "hello " + str(param[2])



 



def main():
    global root
    root = Tk()
    root.title("Minesweeper")
    minesweeper = Minesweeper(root)
    root.mainloop()

if __name__ == "__main__":
    main()