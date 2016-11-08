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
        self.bombPercent = 10
        
        #make button: button , isBomb , location, revealed
        for x in range(self.fieldSize):
            row = []
            for i in range(self.fieldSize):           
                row.append([Button(master, text="■") ,
                            1 if random.randint(0,100) < self.bombPercent else 0,
                            (x,i),
                            0
                    ])
            self.buttons.append(row)
        
        #put buttons on screen
        #and sets up click function for buttons
        rowVar = 0
        for row in self.buttons:
            colVar = 0
            for button in row:
                x = (rowVar , colVar)
                button[0].grid(row = rowVar, column = colVar)      
                self.buttons[rowVar][colVar][0].bind(
                    '<Button-1>',
                    functools.partial(self.lClickWrap,
                        button=self.buttons[rowVar][colVar])
                    )
                colVar += 1
            rowVar += 1


    def lClickWrap(self,event,button):         
        if button[1] == 1:           
            print "you lose!"
        else:
            self.reveal(button)

    def reveal(self,button):
        button[0].config(text = ' ')
        button[3] = 1
        print "you clicked " + str(button[2])
        for neighbor in self.surrounding(button):
            if neighbor[3] == 0: 
                bombs = 0
                for subneighbor in self.surrounding(neighbor):
                   if subneighbor[1] == 1:
                        bombs += 1
                if neighbor[1] == 0:                           
                    if bombs > 0 :
                         neighbor[0].config(text = str(bombs))  
                    else:
                        neighbor[0].config(text = ' ')
                if bombs == 0 and neighbor[3] == 0:          
                   self.reveal(neighbor)

       

    def surrounding(self,button):  
        neighbors = []
        centerx,centery = button[2][0] , button[2][1]       
        for x in range(centerx-1,centerx+2):
            for y in range(centery-1,centery+2):     
                if x >= 0 and y >=0 and x < self.fieldSize and y < self.fieldSize:        
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