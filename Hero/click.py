import tkinter as tk
 
root = tk.Tk()
 
WIDTH = HEIGHT = 400
 
x1 = y1 = WIDTH / 2
 
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

root.counter=0
 
c1 = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)
c2 = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)

 
def draw_rect():
    global c2
    canvas.delete(c2)
    c2 = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="green")
 
 
def del_rect():
    canvas.delete(c1)
    canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="white")
 
 
def move(event):
    global x1, y1
    if event.char == "a":
        del_rect()
        x1 -= 10
    elif event.char == "d":
        del_rect()
        x1 += 10
    elif event.char == "w":
        del_rect()
        y1 -= 10
    elif event.char == "s":
        del_rect()
        y1 += 10
    # draw_rect()
    draw_rect()
 
def peta(event):
    global kunci, koorsblm, koorssdh
    root.counter+=1
    i=root.counter
    if i==0:
    	koorssdh=0,0
    elif i%2 == 0 :
    	koorsblm=event.x,event.y
    	koor=koorssdh,koorsblm	
    else:
    	koorssdh=event.x,event.y
    	koor=koorsblm,koorssdh
    c3=canvas.create_line(koor)
    kunci=event.x,event.y
    delimiter=','.join(map(str,kunci))
    f = open("koordinat.txt", "a")
    f.write(delimiter)
    f.write(";")
    f.close()
    
    


root.bind("<Key>", move)
root.bind("<Button-1>", peta) 
root.mainloop()
