from PIL import Image
import numpy as np
from colorsys import hsv_to_rgb
[startX, endX, startY, endY]= [-2,.5,-1.25,1.25]
#Change the amount of iterations in render
maxIterations = 50
domainLength=endX-startX
rangeLength = endY-startY

startX -= (1920-1080)/1080/2*domainLength 
endX += (1920-1080)/1080/2*domainLength
domainLength *=1920/1080

#Change image size
width = int(1920)
height = int(1080)
def renderMandelbrot(output):
   pixels = [[color(mandlebrotValue(px,py)) for px in range(width)] for py in range(height)]
   # for px in range(0,width):
   #    for py in range(0,height):
   #       #pixels[px][py]=(px,py,100)
   #       print("test")
   array = np.array(pixels, dtype=np.uint8)
   img = Image.fromarray(array)

   img.save(output)
def mandlebrotValue(px,py):
   point = pixelToPoint(px,py)
   x2 = 0
   y2 = 0
   w = 0
   iteration = 0
   while(x2+y2 <= 4 and iteration<maxIterations):
      x = x2 - y2 + point[0]
      y = w -x2 - y2 + point[1]
      x2 = x*x
      y2=y*y
      w = (x+y)*(x+y)
      iteration += 1
   return iteration/maxIterations
def pixelToPoint(px,py):
   point=[500,500]
   point[0]= startX + px/width*domainLength
   point[1]= startY+ py/height*rangeLength
   return point
def color(lightness):
   if(lightness ==1):
      return (0,0,0)
   return tuple([255*x for x in hsv_to_rgb(lightness,1,1)])
print("Rendering...")
#Enter name of image output
renderMandelbrot('render.png')
print("Done!")