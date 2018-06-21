import cv2
import mss
import os
import numpy as np
import count_img

sct = mss.mss()

coordinates = {
        'top': 93,
        'left': 4,
        'height': 658,
        'width': 414
        }

img_paths = []

frame_num = 0

if not os.path.exists(r'./images/'):
    os.mkdir(r'./images/')
else:
    for img in os.listdir(r'./images/'):
        if img.endswith('.jpg'):
            img_paths.append(img)
    frame_num = (count_img.count()) - 1

def capture():
   global frame_num
   frame = np.array(sct.grab(coordinates))
   cv2.imwrite( r'images/img_{}.jpg'.format(frame_num), frame)
   frame_num += 1
   print('Written. Total Images: {}'.format(frame_num))

