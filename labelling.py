import cv2
import numpy as np


##Importando imágenes
image_path = 'path/to/your/image.jpg'
img = cv2.imread(image_path)
original_image = img.copy() # Keep a copy to redraw on
drawing = False # Flag to indicate if we are drawing
current_shape = [] # Store points for the current shape
labels = [] # List to store labels for the image

#Definir funcion Callback Function:

def draw_shape(event, x, y, flags, param):
    global drawing, current_shape, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        current_shape = [(x, y)] # Start a new shape with the first point

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img = original_image.copy() # Redraw the original image
            # Draw a temporary shape based on the points collected so far
            if len(current_shape) > 0:
                start_point = current_shape[0]
                cv2.line(img, start_point, (x, y), (0, 255, 0), 2) # Example: draw a line

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        current_shape.append((x, y))
        # Finalize the drawing of the shape and store the coordinates/parameters
        if len(current_shape) == 2: # Example: for a line, we need two points
            start_point = current_shape[0]
            end_point = current_shape[1]
            cv2.line(img, start_point, end_point, (0, 0, 255), 3)
            labels.append({'type': 'line', 'start': start_point, 'end': end_point})
            current_shape = []

    cv2.imshow('Label Image', img)


#Imágen de la ventana

cv2.namedWindow('Label Image')
cv2.setMouseCallback('Label Image', draw_shape)
cv2.imshow('Label Image', img)