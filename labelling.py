import cv2
import numpy as numpy

image_path = "img/loomis1.jpg"

img = cv2.imread(image_path)
original_image = img.copy()
drawing = False 
current_shape = []
labels = []

#Defining a Mouse Callback Funtion:
def draw_shape(event, x, y, flags, param):
    global drawing, current_shape, img

    if event == cv2.EVENT_