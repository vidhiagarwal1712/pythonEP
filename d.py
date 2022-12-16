import cv2
import os
path = 'Images'
images = os.listdir(path)
newImages = []
for x in images:
    fileName = path +'/'+ x
    newImages.append(fileName)
frame = cv2.imread(newImages[0])
height,width,channels = frame.shape
out = cv2.VideoWriter('Sunrise.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,(width,height))
count = len(newImages)
for i in range(count - 1,0,-1):
    frame = cv2.imread(newImages[i])
    out.write(frame)
out.release()