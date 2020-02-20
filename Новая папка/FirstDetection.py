from imageai.Detection import ObjectDetection
import os
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

execution_path = os.getcwd()

detector = ObjectDetection()

detector.setModelTypeAsRetinaNet()

detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))

detector.loadModel()
while 1:
    flag, img = cap.read()
    print(type(img))

    if cv2.waitKey(5) & 0xFF == ord('q'):						#выход
        quit()
    
    print("\n[!] STARTING DETECTION\n")

    img, detections = detector.detectObjectsFromImage(output_type="array", input_type="array", input_image=img)

    for eachObject in detections:
        print(eachObject)
        x, y = (eachObject["box_points"][0], eachObject["box_points"][2]), (eachObject["box_points"][2], eachObject["box_points"][3])
        cv2.rectangle(img, x, y, (255, 255, 0), 2)
        
    cv2.imshow('result', img)

cap.release()
cv2.destroyAllWindows()
input()