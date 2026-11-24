"""Face detection/recognition-style demo using pretrained OpenCV Haar cascade.
This detects faces, not identities. For identity recognition, enroll consented
subjects and use an appropriate face-embedding model and access controls.
"""
import cv2

image = cv2.imread("input.jpg")
if image is None:
    raise FileNotFoundError("Place an image named input.jpg beside this script.")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(cascade_path)
faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imwrite("faces_detected.jpg", image)
print("Faces detected:", len(faces), "- saved faces_detected.jpg")
