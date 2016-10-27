#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import * 
import tkMessageBox 
import random
import functools
import numpy as np

class Minesweeper():
    """docstring for minesweeper"""
    def __init__(self, master):
        self.master = master
        self.fieldSize = int(raw_input("field size"))
        self.buttons = [] 
        self.bombPercent = 20

        # button , isBomb , location
        for x in range(self.fieldSize):
            row = []
            for i in range(self.fieldSize):           
                row.append([Button(master, text="■") ,
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
                self.buttons[rowVar][colVar][0].bind('<Button-1>',functools.partial(self.lClickWrap,button=self.buttons[rowVar][colVar]))
                colVar += 1
            rowVar += 1


    def lClickWrap(self,event,button):
        
        if button[1] == 1:
            print 'bomb'
        else:
            print "button is at: " + str(button[2])
            
            self.surrounding(button)


    def surrounding(self,button):  
        neighbors = []
        centerx,centery = button[2][0] , button[2][1]       
        for x in range(centerx-1,centerx+2):
            for y in range(centery-1,centery+2):     
                if (x,y) >= (0,0) and x < self.fieldSize and y < self.fieldSize:        
                    neighbors.append(self.buttons[x][y])        
        neighbors.remove(self.buttons[centerx][centery])           
        return neighbors

 
def main():
    global root
    root = Tk()
    root.title("Minesweeper")
    minesweeper = Minesweeper(root)
    root.mainloop()

if __name__ == "__main__":
    main()