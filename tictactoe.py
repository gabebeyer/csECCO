from Tkinter import *
import tkFont


class App:
    
    def __init__(self, master):
        self.customFont = tkFont.Font(family="Helvetica", size=44)
        self.square_info = {1: [33,33,0],  # x , y, filled
                            2: [100,33,0],
                            3: [166,33,0],
                            4: [33,100,0],
                            5: [100,100,0],
                            6: [166,100,0],
                            7: [33,166,0],
                            8: [100,166,0],
                            9: [166,166,0]}

       
        self.canvas = Canvas(master, width=200, height=200)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.pack()  
      
        self.draw_level()                    

        
        mainloop()


    def mouse_click(self,event):
        print "clicked at", event.x, event.y
        print "you clicked", self.coord_to_square(event.x, event.y)
        self.draw_mark('x',self.coord_to_square(event.x, event.y))


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
	root.destroy()

if __name__ == '__main__':
	main()