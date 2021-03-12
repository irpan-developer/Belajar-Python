from tkinter import Frame, Tk, BOTH, Text, Menu, END, filedialog

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
        self.buatTempatText()

    def buatMenubar(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.bukaFile)
        menubar.add_cascade(label="File", menu=fileMenu)

    def buatTempatText(self):
        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def bukaFile(self):
        tipeFile = [('Python files', '*.py'), ('All files', '*')]
        bukaFile = filedialog.Open(self, filetypes=tipeFile)
        isiFile = bukaFile.show()

        if isiFile != '':
            teks = self.bacaFile(isiFile)
            self.txt.insert(END, teks)

    def bacaFile(self, namaFile):
        f = open(namaFile, "r")
        teks = f.read()
        return teks

if __name__ == '__main__':
    root = Tk()
    ex = MembukaFile(root)
    root.mainloop()

