import cv2
import os
import keyboard
import numpy as np
import pyautogui
from processing import Processing

def post_press(label, index):
    global hot
    global not_hot
    with open('y_labels.txt', 'a') as f:
        if label == 'h':
            f.write('1\n')
            hot += 1
        elif label == 'n':
            f.write('0\n')
            not_hot += 1
    f.close()

    pyautogui.press('0')
    print('FRAME NUM: {}'.format(index))
    print('TOTALS ----- HOT {0}, NOT HOT {1}'.format(hot, not_hot))

def label(dir_path, img_arr):
        for index, img in enumerate(img_arr):
            frame = cv2.imread('{}{}'.format(dir_path, img))
            cv2.imshow('FRAME', np.array(frame))

            keyboard.on_press_key('h', lambda _: post_press('h', index), suppress=True)
            keyboard.on_press_key('n', lambda _: post_press('n', index), suppress=True)

            cv2.waitKey(0)

if __name__ == '__main__':
    # sort images
    processing = Processing()
    processing.order_images(r'../images/')
    processing.total_images()

    # apply labels
    hot = 0
    not_hot = 0
    label(r'../images/', processing.sorted_images)
    
        
