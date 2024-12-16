from PIL import Image
import numpy as np
import random
import colorsys
[startX, endX, startY, endY]= [-0.76303941125246,-0.76272491751166,0.0825324955705,0.0828469893113]
maxIterations = 100
domainLength=endX-startX
rangeLength = endY-startY
c1 = []
width = 1000
height = 1000
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
   return tuple([255*x for x in colorsys.hsv_to_rgb(lightness,1,1)])
print("Rendering...")
renderMandelbrot('render.png')
print("Done!")