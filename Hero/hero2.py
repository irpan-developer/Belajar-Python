from tkinter import Frame, Menu, filedialog
from tkinter import *  
import tkinter 
from PIL import ImageTk
from PIL import Image  
import cv2
import numpy as np

class MembukaFile(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.window = parent
        self.initUI()

    def initUI(self):
        self.window.title("File dialog")
        self.pack(fill=BOTH, expand=1)
        self.window.geometry("300x250")
        self.buatMenubar() 
        
    def buatMenubar(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        fileMenu = Menu(menubar)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open", command=self.bukaFile)
        fileMenu.add_command(label="Cek Wajah", command=self.cek)
        fileMenu.add_command(label="Cetak Wajah", command=self.cetak)
        
    def bukaFile(self):
        global panelA,Rawimage
        tipeFile = [('gambar', '*.jpeg'),('Python files', '*.py'), ('All files', '*')]
        path=filedialog.askopenfilename(filetypes=tipeFile)
        Rawimage=cv2.imread(path)
       
        
        widht=800
        height=int(800*Rawimage.shape[0]/Rawimage.shape[1])
        dim=(widht,height)
        Rawimage=cv2.resize(Rawimage,dim,interpolation = cv2.INTER_AREA)
        
        image = cv2.cvtColor(Rawimage, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)        
        if panelA is None:
                  # the first panel will store
                  panelA = Label(image=image)
                  panelA.image = image
                  panelA.pack(anchor="nw", padx=10, pady=10)
        else:
                  # update the pannels	
                  panelA.configure(image=image)
                  panelA.image = image

    def cek(self):
        global faces,x,y,w,h
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        gray= cv2.cvtColor(Rawimage, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 2)
        
        
        for (x, y, w, h) in faces:
             cv2.rectangle(Rawimage, (x, y), (x+w, y+h), (255, 0, 0), 2)     	     
             Raw=cv2.cvtColor(Rawimage,cv2.COLOR_BGR2RGB)
             thumb=Image.fromarray(Raw)
             thumb=thumb.crop((x,y,x+w,y+h))
             thumb = ImageTk.PhotoImage(thumb)
             panel=Label(image=thumb)
             panel.image=thumb
             panel.pack(side="right")
             panel.configure(image=thumb)
             panel.image=thumb
             
             
        image = cv2.cvtColor(Rawimage, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        panelA.configure(image=image)
        panelA.image = image
                
        
    def cetak(self):
        Raw=cv2.cvtColor(Rawimage,cv2.COLOR_BGR2RGB)
        thumb=Image.fromarray(Raw)
        thumb=thumb.crop((x,y,x+w,y+h))
        thumb = ImageTk.PhotoImage(thumb)
        panel=Label(image=thumb)
        panel.image=thumb
        panel.pack(side="right")
        panel.configure(image=thumb)
        panel.image=thumb
        


if __name__ == '__main__':
    root = Tk()
    panelA= None
    
    ex = MembukaFile(root)
    root.mainloop()

