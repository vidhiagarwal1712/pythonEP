from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def getTime():      
    t=strftime('%H %M %S : %p')
    label.config(text=t)
    label.after(1000,getTime)   


label= Label(root,font=('ds-digital',80),background="black",foreground="cyan")
label.pack(anchor='center')

getTime()

mainloop()



import cv2
    
# path
path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
    
# Reading an image in default mode
image = cv2.imread(path)
    
# Window name in which image is displayed
window_name = 'Image'
  
# font
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
   
# Using cv2.putText() method
image = cv2.putText(image, 'OpenCV', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
   
# Displaying the image
cv2.imshow(window_name, image) 



# Center coordinates
center_coordinates = (120, 50)
 
# Radius of circle
radius = 20
  
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
  
# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness)
  
# Displaying the image
cv2.imshow(window_name, image)