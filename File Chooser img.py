from PIL import Image
from IPython.display import display

#MyImg = Image.new( 'RGB', (250,250), "black")
MyImg = Image.open('/home/jonesy/Desktop/wint_sky.gif') 
#use the commented code to import from our own computer
pixels = MyImg.load() # creates the pixel map
display(MyImg)        # displays the black image
#for i in range(MyImg.size[0]):    
#    for j in range(MyImg.size[1]):  
#        pixels[i,j] = (i, j, 100)
        
display(MyImg)
display.show()
