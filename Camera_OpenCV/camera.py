# Processamento de vídeo

import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,220,250)
    
    kernel_size = 5
    blur_g = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

    low_threshold = 100
    high_threshold = 200
    edges = cv2.Canny(blur_g, low_threshold, high_threshold)

    rho = 1 # distance resolution in pixels of the Hough grid
    theta = np.pi / 180 # angular resolution in radians of the Hough grid
    threshold = 15 # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 80 # minimum number of pixels making up a line
    max_line_gap = 10 # maximum gap in pixels between connectable line segments
    line_image = np.copy(frame) * 0 # creating a blank to draw lines on
    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
    min_line_length, max_line_gap)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)
    # Draw the lines on the image
    lines_edges = cv2.addWeighted(frame, 0.8, line_image, 1, 0)

    cv2.imshow('frame1',frame)
    cv2.imshow('frame Canny',lines_edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()