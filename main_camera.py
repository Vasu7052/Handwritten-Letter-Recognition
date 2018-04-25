# Python program for Detection of a
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np
from resizeimage import resizeimage
from PIL import Image
from keras.models import model_from_json
import operator


# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0)

marker_width = marker_height = 15
marker_radius = 15

blank_image = np.zeros((int(cap.get(4)),int(cap.get(3)),3), np.uint8)

blank_image[:,:] = (0,0,0)

render_drawing = False

alphabets = {
    1 : "A" ,
    2 : "B" ,
    3 : "C" ,
    4 : "D" ,
    5 : "E" ,
    6 : "F" ,
    7 : "G" ,
    8 : "H" ,
    9 : "I" ,
    10 : "J" ,
    11 : "K" ,
    12 : "L" ,
    13 : "M" ,
    14 : "N" ,
    15 : "O" ,
    16 : "P" ,
    17 : "Q" ,
    18 : "R" ,
    19 : "S" ,
    20 : "T" ,
    21 : "U" ,
    22 : "V" ,
    23 : "W" ,
    24 : "X" ,
    25 : "Y" ,
    26 : "Z"
}

letter = ''

while (1):
    _, frame = cap.read()

    frame = cv2.flip(frame , 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([110, 50, 50])
    upper_red = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    #res = cv2.bitwise_and(frame, frame, mask=mask)

    if render_drawing:
        cv2.putText(frame, "Drawing Enabled", (10, 40), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, "Drawing Disabled", (10, 40), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('Blank', blank_image)
    #cv2.imshow('res', res)

    if cv2.waitKey(10) == 32:
        #print("Space Pressed")
        if render_drawing:
            render_drawing = False
            print("Prediction Started")
            cv2.imwrite("image.png", blank_image)
            
        else:
            render_drawing = True
        blank_image[:, :] = (0, 0, 0)

    elif cv2.waitKey(10) == ord('q'):
        print("Quit Pressed")
        cap.release()
        cv2.destroyAllWindows()
        break