"""Object detection using a pre-trained YOLOv8 model.
Install ultralytics; place an image named input.jpg beside this script.
"""
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # downloads pretrained weights on first run
results = model.predict(source="input.jpg", save=True, conf=0.25)
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        print(model.names[class_id], "confidence:", round(float(box.conf[0]), 3))
print("Annotated image saved in runs/detect/predict/")
