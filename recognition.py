import cv2 as cv
import numpy as np
import math
from color_filter import *
from images_stack import *   
from control import *
from game import *

# Pass camera source as 0 for built-in webcam, 1 for external camera
capture = cv.VideoCapture(0)

# Starting the Game
game_start()

hsv_trackbars_create("Color Filter")
while True:

    # Obtain frame from camera capture
    _, frame = capture.read()

    # Horizontally flip the frame
    frame = cv.flip(frame, 1)

    # Define region of interest
    square_side_length = 300
    upper_left = 300
    lower_left = 100
    upper_right = upper_left + square_side_length
    lower_right = lower_left + square_side_length
    roi = frame[lower_left:lower_right, upper_left:upper_right]
    cv.rectangle(frame, (upper_left, lower_left),
                 (upper_right, lower_right), (252, 0, 0), 0)

    # convert roi to HSV and filter hand color
    roi_hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

    lower_bound, upper_bound = hsv_trackbars_pos(name="Color Filter")[0]
    mask = cv.inRange(roi_hsv, lowerb=lower_bound, upperb=upper_bound)
    roi_masked = cv.bitwise_and(roi, roi, mask=mask)

    # Morphological operations
    kernel_9 = cv.getStructuringElement(cv.MORPH_RECT, (9, 9))
    kernel_7 = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))

    # Remove Noise
    mask_opened = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel_9)
    # Close Gaps
    mask_closed = cv.morphologyEx(mask_opened, cv.MORPH_CLOSE, kernel_7)
    # Blur
    mask_blurred = cv.medianBlur(mask_closed, 5)

    # Compute the contours
    contours, _ = cv.findContours(
        mask_blurred, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Find contour of max area (hand)


    # Slack and show
    color_extraction_stack = stack_images(0.8, [[roi, mask], [roi_hsv, mask_blurred]])
    cv.imshow("Color Extraction Stack", color_extraction_stack)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
capture.release() 
