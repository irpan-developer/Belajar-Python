from PIL import Image
im = Image.open(r'/home/jonesy/Desktop/Nw66t.jpg')
rgb_im=im.convert("RGBA")
pixelMap = rgb_im.load()

for i in range(rgb_im.size[0]):
    for j in range(rgb_im.size[1]):
        if (i-100)**3+(j-100)**2<=1000:
           if (i-100)**3+(j-100)**2>=600:
            pixelMap[i,j] = (200,0,0)
        
rgb_im.show()       
rgb_im.save("out.tif") 
rgb_im.close()

