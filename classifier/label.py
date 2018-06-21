import cv2
import os
import keyboard

def main():
    hot = 0
    not_hot = 0
    with open('labels.txt', 'w') as f:
        for img in os.listdir(r'./images'):
            if img.endswith('.jpg'):
                pic = cv2.imread(r'./images/{}'.format(img))
                cv2.imshow('PIC', pic)
                hot_or_not = input('h/n: ')
                if hot_or_not.lower() == 'h':
                    f.write('{0}, {1}\n'.format(img, 1))
                    hot += 1
                    print('HOT. TOTAL HOT: {}'.format(hot))
                    continue
                elif hot_or_not.lower() == 'n':
                    not_hot += 1
                    print('NOT HOT. TOTAL NOT HOT {}'.format(img, 0))
                    continue
                cv2.waitKey(0)
        f.close()

if __name__ == '__main__':
    main()
    
        
