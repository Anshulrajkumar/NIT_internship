from ultralytics import YOLO
import cv2
model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)
if not cap.isOpened():
    print("Error")
    exit()
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
cap.release()
cv2.destroyAllWindows()
