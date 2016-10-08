from Tkinter import *
import tkFont
import sys
import os
import time



class App:
    def __init__(self, master):       
        self.master = master
        self.customFont = tkFont.Font(family="Helvetica", size=44)
        self.turn = 0
                    #center
        # square : [ x, y , filled , owner]
        self.square_info = {1: [33,33,0,''],
                            2: [100,33,0,''],
                            3: [166,33,0,''],
                            4: [33,100,0,''],
                            5: [100,100,0,''],
                            6: [166,100,0,''],
                            7: [33,166,0,''],
                            8: [100,166,0,''],
                            9: [166,166,0,'']}       
        self.canvas = Canvas(master, width=200, height=200)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.pack()
        self.draw_level()
        mainloop()

    def draw_mark(self,mark,square):
        if mark == 'o':
            self.canvas.create_text(
                self.square_info[square][0],
                self.square_info[square][1], 
                text = 'O',
                font = self.customFont)
        elif mark == 'x':
            self.canvas.create_text(
                self.square_info[square][0],
                self.square_info[square][1],
                text = 'X',
                font = self.customFont)
    
    ##full restart
    def end_game(self,winner):

        self.canvas.delete("all")

        self.master.destroy()

        main()


    def check_for_winner(self):        
        square1,square2,square3 = self.square_info[1][3],self.square_info[2][3],self.square_info[3][3]        
        square4,square5,square6 = self.square_info[4][3],self.square_info[5][3],self.square_info[6][3]
        square7,square8,square9 = self.square_info[7][3], self.square_info[8][3],self.square_info[9][3]
    
        if square1 == square2 == square3 != '':
            self.end_game(square1)
        if square4 == square5 == square6 != '':
            self.end_game(square4)
        if square7 == square8 == square9 != '':
            self.end_game(square7)

        if square1 == square4 == square7 != '':
            self.end_game(square1)
        if square2 == square5 == square8 != '':
            self.end_game(square2)
        if square3 == square6 == square9 != '':
            self.end_game(square3)

        if square1 == square5 == square9 != '':
            self.end_game(square5)
        if square7 == square5 == square3 != '':
            self.end_game(square5)

    def mouse_click(self,event):

        square = self.coord_to_square(event.x, event.y)
            
        if self.turn == 0 and self.square_info[square][2] == 0:
            self.draw_mark('x',square)
            self.square_info[square][2] = 1
            self.square_info[square][3] = 'x'
            self.turn = 1       
        elif self.turn == 1 and self.square_info[square][2] == 0:
            self.draw_mark('o',square)
            self.square_info[square][3] = 'o'
            self.turn = 0 

        self.check_for_winner()    

    def draw_level(self):    
        self.canvas.create_line(0, 66, 200, 66)
        self.canvas.create_line(0, 133, 200, 133)
        self.canvas.create_line(66, 0, 66, 200)
        self.canvas.create_line(133, 0, 133, 200)

    def coord_to_square(self,x,y):
        if x > 0 and x < 66:
            if y > 0 and y < 66:
                return 1
            elif y >= 66 and y < 133:
                return 4
            elif y >= 133 and y < 200:
                return 7
        if x >= 66 and x < 133:
            if y > 0 and y < 66:
                return 2
            elif y >= 66 and y < 133:
                return 5
            elif y >= 133 and y < 200:
                return 8
        if x >=133 and x < 200:
            if y > 0 and y < 66:
                return 3
            elif y >= 66 and y < 133:
                return 6
            elif y >= 133 and y < 200:
                return 9

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()


