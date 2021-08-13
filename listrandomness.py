import random
import tkinter 
  
# list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown'] 

timeleft = 30

def startGame(event): 
      
    if timeleft == 30: 
          
        # start the countdown timer. 
        countdown() 

def countdown(): 
  
    global timeleft 
  
    # if a game is in play 
    if timeleft > 0: 
  
        # decrement the timer. 
        timeleft -= 1
          
        # update the time left label 
        timeLabel.config(text = "Time left: "
                               + str(timeleft))
        random.shuffle(colours) 
        instructions.config(text=colours[2])                         
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown)


# create a GUI window 
root = tkinter.Tk() 
  
# set the title 
root.title("COLORGAME") 
  
# set the size 
root.geometry("375x200") 
  
# add an instructions label 
instructions = tkinter.Label(root, text = "Type in the colour"
                        "of the words, and not the word text!", 
                                      font = ('Helvetica', 12)) 
instructions.pack()  
  
# add a score label 
scoreLabel = tkinter.Label(root, text = "Press enter to start", 
                                      font = ('Helvetica', 12)) 
scoreLabel.pack() 
  
# add a time left label 
timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12)) 
                
timeLabel.pack() 
  
# add a label for displaying the colours 
label = tkinter.Label(root, font = ('Helvetica', 60)) 
label.pack() 
  
# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root) 
  
# run the 'startGame' function  
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack() 
  
# set focus on the entry box 
e.focus_set() 
  
# start the GUI 
root.mainloop() 