import os
from pathlib import Path

import torch
from ultralytics import YOLO

classesVisDrone = {0: 'пешеход', 1: 'люди', 2: 'велосипед', 3: 'автомобиль', 4: 'фургон', 5: 'грузовик', 6: 'трехколесный велосипед', 7: 'трехколесный велосипед с навесом', 8: 'автобус', 9: 'мотоцикл'}

def predictVisDrone(fileName):
    model = YOLO(Path('./src/networks/models/visDrone/weights/best.pt').resolve())
    results = model(fileName, imgsz=200, save=True, device="cpu")

    subfolders = [f for f in os.listdir("./runs/detect") if os.path.isdir(os.path.join("./runs/detect", f))]
    latest_subfolder = max(subfolders, key=lambda x: os.path.getmtime(os.path.join("./runs/detect", x)))

    for result in results:
        classesTrue = [value for key, value in classesVisDrone.items() if key in result.boxes.cls.to(torch.int).tolist()]

        return {
            "array": classesTrue,
            "image": f"./runs/detect/{latest_subfolder}/{fileName.split('/')[3]}"
        }
