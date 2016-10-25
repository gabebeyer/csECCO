from Tkinter import *
import tkFont
import tkMessageBox
import random
import time



class App:
    def __init__(self, master):       
        self.master = master
        self.customFont = tkFont.Font(family="Helvetica", size=44)
        self.turn = 0
        self.gamemode = 2

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
        newx = self.master.winfo_x()
        newy = self.master.winfo_y()
        tkMessageBox.showinfo("Winner", "The winner is: " + winner + "!!!", parent = self.master)
        self.canvas.delete("all")
        self.master.destroy()
        main(newx,newy)


    def check_for_winner(self):        
        square1,square2,square3 = self.square_info[1][3],self.square_info[2][3],self.square_info[3][3]        
        square4,square5,square6 = self.square_info[4][3],self.square_info[5][3],self.square_info[6][3]
        square7,square8,square9 = self.square_info[7][3], self.square_info[8][3],self.square_info[9][3]    
        if square1 == square2 == square3 != '': self.end_game(square1)
        if square4 == square5 == square6 != '': self.end_game(square4)
        if square7 == square8 == square9 != '': self.end_game(square7)
        if square1 == square4 == square7 != '': self.end_game(square1)
        if square2 == square5 == square8 != '': self.end_game(square2)
        if square3 == square6 == square9 != '': self.end_game(square3)
        if square1 == square5 == square9 != '': self.end_game(square5)
        if square7 == square5 == square3 != '': self.end_game(square5)

        self.testNum = 0
        for x in xrange(1,10):
            self.testNum +=  self.square_info[x][2]
        if self.testNum == 9:
            self.end_game("(=ↀωↀ=)")

    def cpu_turn(self, *args):

        threats = [[self.square_info[1],self.square_info[2],self.square_info[3]],
                    [self.square_info[4],self.square_info[5],self.square_info[6]],
                    [self.square_info[7],self.square_info[8],self.square_info[9]],
                    [self.square_info[1],self.square_info[4],self.square_info[7]],
                    [self.square_info[2],self.square_info[5],self.square_info[8]],
                    [self.square_info[3],self.square_info[6],self.square_info[9]],
                    [self.square_info[1],self.square_info[2],self.square_info[3]],
                    [self.square_info[1],self.square_info[2],self.square_info[3]]]

        for threat in threats:
            number = 0
            for box in threat:
                if box[2] == 1 and box[3] == 'x':
                    number += 1 
            if number == 2:
                for box in threat:
                    if box[2] == 0:
                        for key in self.square_info.keys():
                            if  self.square_info[key] == box :
                                self.draw_mark('o',key)
                                self.square_info[key][2] = 1
                                self.square_info[key][3] = 'o'
                                return
        #center
        if self.square_info[5][2] == 0:
            self.draw_mark('o',5)
            self.square_info[5][2] = 1
            self.square_info[5][3] = 'o'
            return
        
        #corners
        for i in [1,3,7,9]:
            if self.square_info[i][2] == 0:
                self.draw_mark('o',i)
                self.square_info[i][2] = 1
                self.square_info[i][3] = 'o'            
                return
      
        #edges
        for i in [2,4,6,8]:
            if self.square_info[i][2] == 0:
                self.draw_mark('o',i)
                self.square_info[i][2] = 1
                self.square_info[i][3] = 'o'
                return
            
    def mouse_click(self,event):
        square = self.coord_to_square(event.x, event.y)
        if self.gamemode == 1:
            if self.turn == 0 and self.square_info[square][2] == 0:
                self.draw_mark('x',square)
                self.square_info[square][2] = 1
                self.square_info[square][3] = 'x'
                self.turn = 1
            elif self.turn == 1 and self.square_info[square][2] == 0:
                self.draw_mark('o',square)
                self.square_info[square][2] = 1
                self.square_info[square][3] = 'o'
                self.turn = 0
        elif self.gamemode == 2:
            if self.square_info[square][2] == 0:
                self.draw_mark('x', square)
                self.square_info[square][2] = 1
                self.square_info[square][3] = 'x'
                self.check_for_winner()
                self.cpu_turn(self)
        self.check_for_winner()


    def draw_level(self):    
        self.canvas.create_line(0, 66, 200, 66)
        self.canvas.create_line(0, 133, 200, 133)
        self.canvas.create_line(66, 0, 66, 200)
        self.canvas.create_line(133, 0, 133, 200)

    def coord_to_square(self,x,y):
        if x > 0 and x < 66:
            if y > 0 and y < 66: return 1
            elif y >= 66 and y < 133: return 4
            elif y >= 133 and y < 200:return 7
        if x >= 66 and x < 133:
            if y > 0 and y < 66: return 2
            elif y >= 66 and y < 133: return 5
            elif y >= 133 and y < 200: return 8
        if x >=133 and x < 200:
            if y > 0 and y < 66: return 3
            elif y >= 66 and y < 133: return 6
            elif y >= 133 and y < 200:return 9

def main(x,y):
    root = Tk()
    root.geometry("+"+str(x)+"+"+str(y))
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main(200,100)


