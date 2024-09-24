# Processamento de vídeo

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# define o range do blue em HSV, onde a primeiro e H, o segundo S e o terceiro V
lower_blue= np.array([78,158,124])
upper_blue = np.array([138,255,255])

while(cap.isOpened()):
    ret, frame = cap.read()
    
    # Converte BGR para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold do HSV para obter apenas a mascara da cor determinada pelos limites do range
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    result = cv2.bitwise_and(frame, frame, mask=mask)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 5000:  # Tamanho mínimo do contorno para evitar ruído
            x, y, w, h = cv2.boundingRect(contour)  
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Desenhar o retângulo verde
    
    if cv2.waitKey(1) * 0xFF ==ord('q'):
        break
    
    cv2.imshow('Original with Detection', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Detected Object', result)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()