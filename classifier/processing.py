import cv2
import os
import numpy as np
import sys

class Processing:
    def __init__(self, path):
        # placeholder array
        self.path = path
        self.sorted_images = [None for img in os.listdir(path) if img.endswith('.jpg')]


    def total_images(self):
        print('TOTAL IMAGES: {}'.format(len(self.sorted_images)))
        return self.sorted_images


    def _index_split(self, img):
        split_one = img.split('_')[1]
        index = split_one.split('.jpg')[0]
        return int(index)
    
    
    def order_images(self):
        for img in os.listdir(self.path):
            index = self._index_split(img)
            self.sorted_images[index] = img


def start():
    processor = Processing(r'./images/')
    processor.order_images()
    processor.total_images()
    return processor.sorted_images


if __name__ == '__main__':
    start()
