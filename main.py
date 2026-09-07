import cv2
from ultralytics import YOLO
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
        if len(points) > 7:
            shoulder_gauche = points[5]
            shoulder_droit = points[6]
            if shoulder_gauche[0] > 0 and shoulder_droit[0] > 0:
                print(
                    f"épaule gauche: x ={shoulder_gauche[0]:.1f}, y = {shoulder_gauche[1]:.1f} "
                    f"droit droit: x = {shoulder_droit[0]:.1f}, y = {shoulder_droit[1]:.1f} "
                )
    cv2.imshow("frame", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
