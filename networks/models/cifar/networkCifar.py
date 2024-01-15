import os
import pathlib
import platform
from pathlib import Path

import torch
from ultralytics import YOLO

classesCifar = {
    0: 'яблоко', 1: 'аквариумная рыбка', 2: 'младенец', 3: 'медведь', 4: 'бобр', 5: 'кровать', 6: 'пчела', 7: 'жук',
    8: 'велосипед', 9: 'бутылка', 10: 'чаша', 11: 'мальчик', 12: 'мост', 13: 'автобус', 14: 'бабочка', 15: 'верблюд',
    16: 'банка', 17: 'замок', 18: 'гусеница', 19: 'крупный рогатый скот', 20: 'стул', 21: 'шимпанзе', 22: 'часы',
    23: 'облако', 24: 'таракан', 25: 'диван', 26: 'краб', 27: 'крокодил', 28: 'чашка', 29: 'динозавр', 30: 'дельфин',
    31: 'слон', 32: 'плоская рыба', 33: 'лес', 34: 'лиса', 35: 'девочка', 36: 'хомяк', 37: 'дом', 38: 'кенгуру',
    39: 'клавиатура', 40: 'лампа', 41: 'газонокосилка', 42: 'леопард', 43: 'лев', 44: 'ящерица', 45: 'омар', 46: 'человек',
    47: 'клен', 48: 'мотоцикл', 49: 'гора', 50: 'мышь', 51: 'гриб', 52: 'дуб', 53: 'апельсин', 54: 'орхидея', 55: 'выдра',
    56: 'пальма', 57: 'груша', 58: 'пикап', 59: 'сосна', 60: 'равнина', 61: 'тарелка', 62: 'мак', 63: 'дикобраз',
    64: 'опоссум', 65: 'кролик', 66: 'енот', 67: 'скат', 68: 'дорога', 69: 'ракета', 70: 'роза', 71: 'море', 72: 'тюлень',
    73: 'акула', 74: 'полевка', 75: 'скунс', 76: 'небоскреб', 77: 'улитка', 78: 'змея', 79: 'паук', 80: 'белка', 81: 'трамвай',
    82: 'подсолнух', 83: 'сладкий перец', 84: 'стол', 85: 'танк', 86: 'телефон', 87: 'телевизор', 88: 'тигр', 89: 'трактор',
    90: 'поезд', 91: 'форель', 92: 'тюльпан', 93: 'черепаха', 94: 'гардероб', 95: 'кит', 96: 'ива', 97: 'волк', 98: 'женщина',
    99: 'червь'
}

plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

def predictCifar(fileName):
    model = YOLO(Path('./networks/models/cifar/weights/best.pt').resolve())
    results = model(fileName, imgsz=32, save=True, device="cpu")

    for result in results:
        classesTrue = [classesCifar[key] for key in result.probs.top5 if key in classesCifar]

    subfolders = [f for f in os.listdir("./runs/classify") if os.path.isdir(os.path.join("./runs/classify", f))]
    latest_subfolder = max(subfolders, key=lambda x: os.path.getmtime(os.path.join("./runs/classify", x)))

    for result in results:
        return {
            "array": classesTrue,
            "image": f"./runs/classify/{latest_subfolder}/{fileName.split('/')[2]}"
        }
