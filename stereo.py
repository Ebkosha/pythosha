import numpy as np
import cv2

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)

while(True):
    # Capture frame-by-frame
    ret, frame1 = cap1.read()
    ret, frame2 = cap2.read()
q
    # Display the resulting frame
    cv2.imshow('Cam1',frame1)
    cv2.imshow('Cam2',frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()