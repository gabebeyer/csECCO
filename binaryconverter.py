from Tkinter import *

def decimalToBinary(decimalNumber): 
	
	if decimalNumber == 0:
		return '0'
	else:
		return decimalToBinary(decimalNumber/2) + str(decimalNumber%2)

def binaryToDecimal(binaryNumber):

	positional = len(binaryNumber) - 1
	decimal = 0

	for x in binaryNumber:
		decimal += int(x) * (2**positional)
		positional -= 1

	return int(decimal)

class App:
    
    def __init__(self, master):

        frame = Frame(master,height = 100, width = 100)
        frame.pack()

        self.currentInput = StringVar()
        self.binarystore = ''

        self.entryField = Entry(frame, textvariable = self.currentInput)
        self.entryField.pack(fill = BOTH)

        self.binDecButton = Button(frame,text="bin->dec",command =lambda: self.binaryToDecimalPrinter(self.currentInput.get()))
        self.binDecButton.pack()

        self.decBinButton = Button(frame, text="dec->bin",command =lambda: self.decimalToBinaryPrinter(self.currentInput.get()))
        self.decBinButton.pack()

        self.outputDisplay = Label(frame,text='', background = 'grey')	
        self.outputDisplay.pack(side=BOTTOM, fill = BOTH, expand = 1)

    def decimalToBinaryPrinter(self,decimalNumber):       
        o = decimalToBinary(int(decimalNumber))
        self.outputDisplay.config(text=o)
        print o
    
    def binaryToDecimalPrinter(self,binaryNumber):       
        o = binaryToDecimal(str(binaryNumber))
        self.outputDisplay.config(text=o)
        print o

def main():
	root = Tk()
	app = App(root)
	root.mainloop()
	root.destroy()

if __name__ == '__main__':
	main()

