import cv2
import mediapipe as mp

from calculer_angle import calculer_angle
from evaluer_angle import evaluer_angle

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1, 
    smooth_landmarks=True, 
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
if not cap.isOpened():
    cap = cv2.VideoCapture(1, cv2.CAP_MSMF)
if not cap.isOpened():
    raise IOError("Impossible d'ouvrir la webcam")


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("Appuyez sur 'q' pour quitter")

angle_lisse = None
alpha = 0.5 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)


    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )


    if results.pose_world_landmarks and results.pose_landmarks:
        world = results.pose_world_landmarks.landmark
        lm_2d = results.pose_landmarks.landmark


        epaule = [world[12].x, world[12].y, world[12].z]
        coude = [world[14].x, world[14].y, world[14].z]
        poignet = [world[16].x, world[16].y, world[16].z]

        angle_brut = calculer_angle(epaule, coude, poignet)

        if angle_lisse is None:
            angle_lisse = angle_brut
        else:
            angle_lisse = alpha * angle_brut + (1 - alpha) * angle_lisse

        statut, couleur = evaluer_angle(angle_lisse, posture="kumite", body_part="garde")

        cx, cy = int(lm_2d[14].x * w), int(lm_2d[14].y * h)

        cv2.putText(frame, f"{int(angle_lisse)} deg", (cx - 40, cy - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, couleur, 2, cv2.LINE_AA)

        cv2.putText(frame, f"STATUT: {statut}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, couleur, 2, cv2.LINE_AA)

    cv2.imshow("Biomecanique Kyokushin 3D", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
