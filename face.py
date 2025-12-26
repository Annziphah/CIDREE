import cv2
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        tz_x = x + int(w * 0.25)
        tz_y = y
        tz_w = int(w * 0.5)
        tz_h = int(h * 0.6)

        # T-zone rectangle (blue)
        cv2.rectangle(
            frame,
            (tz_x, tz_y),
            (tz_x + tz_w, tz_y + tz_h),
            (255, 0, 0),
            2
        )
    cv2.imshow("Face Detection with T-Zone", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
