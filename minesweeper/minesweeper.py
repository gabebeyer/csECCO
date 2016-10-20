from Tkinter import * 
import tkMessageBox 
import random


class Minesweeper():
    """docstring for minesweeper"""
    def __init__(self, master):
        

        frame = Frame(master)
        frame.pack()

def main():
    global root
    root = Tk()
    root.title("Minesweeper")
    minesweeper = Minesweeper(root)
    root.mainloop()

if __name__ == "__main__":
    main()