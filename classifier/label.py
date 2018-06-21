from processing import Processing
import cv2
import os
import keyboard
import numpy as np

def label(dir_path, img_arr):
    hot = 0
    not_hot = 0
    with open('labels.txt', 'w') as f:
        for img in img_arr:
            frame = cv2.imread('{}{}'.format(dir_path, img))
            cv2.imshow('FRAME', np.array(frame))
            cv2.waitKey(0)

    f.close()

if __name__ == '__main__':
    
    processing = Processing()
    processing.order_images(r'../images/')
    processing.total_images()

    label(r'../images/', processing.sorted_images)
    
        
