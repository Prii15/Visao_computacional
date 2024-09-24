import cv2

cap = cv2.VideoCapture("baiacu.mp4")
                       
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,100)
    cv2.imshow('frame1',frame)
    cv2.imshow('frame Canny',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()