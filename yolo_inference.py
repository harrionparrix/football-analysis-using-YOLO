from ultralytics import YOLO
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

model = YOLO('yolov8x').to(device)

res = model.predict('./08fd33_4.mp4',save=True)

print(res[0])

for box in res[0].boxes:
    print(box)


