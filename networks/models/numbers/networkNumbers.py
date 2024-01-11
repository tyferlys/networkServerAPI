import torch
from ultralytics import YOLO

def predictNumbers(image):

    model = YOLO('./networks/models/numbers/weights/best.pt')
    results = model(image, imgsz=300, device="cpu")

    for result in results:
        print(result.boxes.cls)
        return result.boxes.cls.to(torch.int).tolist()
