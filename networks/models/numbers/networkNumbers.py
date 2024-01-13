import os
from pathlib import Path

import torch
from ultralytics import YOLO


def predictNumbers(fileName):
    model = YOLO(Path('./networks/models/numbers/weights/best.pt').resolve())
    results = model(fileName, imgsz=300, save=True, device="cpu")

    subfolders = [f for f in os.listdir("./runs/detect") if os.path.isdir(os.path.join("./runs/detect", f))]
    latest_subfolder = max(subfolders, key=lambda x: os.path.getmtime(os.path.join("./runs/detect", x)))

    for result in results:
        return {
            "array": result.boxes.cls.to(torch.int).tolist(),
            "image": f"./runs/detect/{latest_subfolder}/{fileName.split('/')[2]}"
        }
