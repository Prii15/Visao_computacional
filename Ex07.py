import cv2
import numpy as np

cap = cv2.VideoCapture("baiacu.mp4")

'''
history = número de frames usados para construir o modelo estatístico do plano de fundo. Quanto menor o valor,
mais rápidas as alterações no plano de fundo serão consideradas pelo modelo.
varThreshold = Limiar na distância quadrada de Mahalanobis entre o pixel e o modelo para 
decidir se um pixel está bem descrito pelo modelo de fundo.
detectShadows = Se True, as sombras serão apresentadas na imagem.
'''

mog = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=10, detectShadows=True)

while(cap.isOpened()):
    ret, frame = cap.read()
    fgmask = mog.apply(frame)
    cv2.imshow('frame movimento',fgmask )
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()