from PIL import Image
import numpy as np
from colorsys import hsv_to_rgb
import cv2
import os
[startX, endX, startY, endY]= [-2,.5,-1.25,1.25]
#Change the amount of iterations in render
maxIterations = 50
domainLength=endX-startX
rangeLength = endY-startY
indent = 0
#Change image size
width = 64
height = width
renderPreffix = "frame_"
frames = 64
FPS = 20
def renderMandelbrot(output):
   pixels = [[color(mandlebrotValue(px,py)) for px in range(width)] for py in range(height)]
   # for px in range(0,width):
   #    for py in range(0,height):
   #       #pixels[px][py]=(px,py,100)
   #       print("test")
   array = np.array(pixels, dtype=np.uint8)
   img = Image.fromarray(array)

   img.save("/Users/Period2/Desktop/VSCode/Mandelbrot-py/movie/"+output+".png","JPEG")
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
   return tuple([255*x for x in hsv_to_rgb(lightness+indent,1,1)])
def zoom(arr,factor):
   cut = (1-factor)/2
   global domainLength
   global rangeLength
   domainLength=arr[1]-arr[0]
   rangeLength = arr[3]-arr[2]
   arr = [arr[0]+cut*domainLength,arr[1]-cut*domainLength,arr[2]+cut*rangeLength,arr[3]-cut*rangeLength]
   domainLength=arr[1]-arr[0]
   rangeLength = arr[3]-arr[2]
   return arr
print("Rendering...")
#Enter name of image output
for i in range(0,frames):
   indent+=1/frames
   [startX, endX, startY, endY] = zoom([startX, endX, startY, endY],1)
   renderMandelbrot(renderPreffix+str(i))

image_folder = "/Users/Period2/Desktop/VSCode/Mandelbrot-py/movie"
images = [(image_folder+"/"+renderPreffix+str(i)+".png") for i in range(0,frames)]
video_name = "render.mp4"
first_image = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = first_image.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 format
video = cv2.VideoWriter(video_name, fourcc, FPS, (width, height))
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)
    os.remove(image)
# Release the video writer
video.release()
cv2.destroyAllWindows()
print("Done!")