from PIL import Image
im = Image.open(r'/home/jonesy/Desktop/Nw66t.jpg')
rgb_im=im.convert('RGBA')
pixels = rgb_im.load()

def get_pixel(rgb_im, i, j):
    # Inside image bounds?
    width, height = rgb_im.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = rgb_im.getpixel((i, j))
    return pixel

for i in range(rgb_im.size[0]):
    for j in range(rgb_im.size[1]):
      pixel = get_pixel(rgb_im, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      #gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

      # Set Pixel in new image
      pixels[i, j] = (red,red,blue)

rgb_im.show()
rgb_im.save("out.tif") 
rgb_im.close()
