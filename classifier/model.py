import keras
from keras.models import Sequential 
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import os
import cv2
import numpy as np
from collections import deque
from processing import start

def preprocess_data():
    """
    preprocesses image data and labels
    """

    # input
    X = []
    # class
    Y = []

    # load labels 
    with open(r'./y_labels.txt') as f:
        n_label = 0
        for label in f:
            Y.append(int(label.rstrip()))

    print('TOTAL LABELS: {}'.format(len(Y)))

    sorted_images = start()
    print(sorted_images[0:10])
    # load images
    for img in sorted_images:
        image = cv2.imread(r'./images/{}'.format(img))
        resize_image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
        final_image = np.array(resize_image)
        img_shape = final_image.shape
        X.append(final_image)
        if len(X) % 1000 == 0:
            print('IMAGES READ: {}'.format(len(X)))
    print('TOTAL IMAGES: {}'.format(len(X)))


    # adjust data distribution
    print('Adjusting class distribution..')
    print('HOT: {0}, NOT: {1}'.format(Y.count(1), Y.count(0)))
    X = X[0:len(Y)]
    while Y.count(0) > Y.count(1):
        val = np.random.randint(0, high=len(Y))
        if Y[val] == 0:
            del Y[val]
            del X[val]
            print(Y.count(1), Y.count(0))

    #for i, l in enumerate(Y):
    #    #if l is 1:
    #    #    cv2.imshow('HOT', X[i])
    #    if l is 0:
    #        cv2.imshow('NOT', X[i])
    #    cv2.waitKey(0)

    # shuffle data
    X = np.array(X)
    Y = np.array(Y)
    X, Y = shuffle(X, Y, random_state=0)

    # split into train and test set
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.2, random_state=0)

    return x_train, x_test, y_train, y_test, img_shape


def build_model(input_shape):
    """
    input_shape = (img_x, img_y, channels)
    return: model
    """

    print('Building model..')

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(64, (5, 5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(1000, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    print(model.summary())
    return model


if __name__ == '__main__':

    epochs = 300
    batch_size = 128

    x_train, x_test, y_train, y_test, img_size = preprocess_data()

    model = build_model(img_size)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test))
