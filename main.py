import cv2
import numpy as np
from ultralytics import YOLO
from src.rules.angles import calculer_angle
model = YOLO ("yolo11n-pose.pt")
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
if cap.isOpened() is False:
    cap = cv2.VideoCapture(1, cv2.CAP_MSMF)
if cap.isOpened() is False:
    raise IOError("Cannot open webcam")
print ("press q to exit")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    result = model (frame, verbose=False, device="cuda:0")
    annotated_frame = result[0].plot()
    if result[0].keypoints is not None and len(result[0].keypoints.xy) > 0:
        points = result[0].keypoints.xy[0].cpu().numpy()
        if len(points) > 11:
            shoulder_droit = points[6]
            elbow_droit = points[8]
            poignet_droit = points[10]
            if elbow_droit[0] > 0 and shoulder_droit[0] > 0 and poignet_droit[0] > 0:
                angle_elbow = calculer_angle(shoulder_droit, elbow_droit, poignet_droit)
                elbow_x, elbow_y = int(elbow_droit[0]), int(elbow_droit[1])

                cv2.putText(annotated_frame,
                            f"{int(angle_elbow)} deg",
                            (elbow_x - 40, elbow_y - 20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 255, 0),
                            2,
                            cv2.LINE_AA
                            )

    cv2.imshow("frame", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
