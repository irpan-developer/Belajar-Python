import tkinter

def hapus(event):
    c.delete(event.widget)
    print(event.widget)

top=tkinter.Tk()

c=tkinter.Canvas(top,bg="cyan",height=600,width=1000)
coord=10,50,240,210,300,300
coord2=50,50,310,200

line=c.create_line(coord)

tombol=tkinter.Button(c,text="delete",command=hapus)
# arc=c.create_arc(coord2,start=0,extent=300,fill="red")


c.pack()
print(type(line))
# print(arc)
a=c.find_all()

for i in a:
    koor=c.coords(a)
    # print(c.coords(arc))



top.bind('<Button-1>',hapus)
c.update()
y1=int(c.winfo_reqheight())
x1=int(c.winfo_reqwidth())
x1=x1/2

tombol.place(x=-10,y=y1-30)

top.title("Kanvas")
top.mainloop()