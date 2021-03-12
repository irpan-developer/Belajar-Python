import tkinter
from tkinter import *
from tkinter import filedialog

def select_image():
	
	path = filedialog.askopenfilename()
	image = PhotoImage(path)
	label = Label(image=image)
	label.pack()


root = Tk()
btn = Button(tkinter, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
	

root.mainloop()
