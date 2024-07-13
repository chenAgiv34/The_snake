import math
import random
import subprocess
import time

import numpy as np
from threading import Thread, Lock

from data import sensorSize, theFocalLengthOfTheLens, imageSizeWinds, imageSizeHeight, timeSleepYolo


def field_of_vision():
    #גודל חיישן (מימיד אופקי) = H
    #אורך המוקד של העדשה = f
    H = sensorSize
    f = theFocalLengthOfTheLens
    afov = 2 * math.atan(H / (2 * f))
    return afov
def numOfExp():
    lock = Lock()
    filepath = "C:\\Users\\chena\\OneDrive\\The_snake\\server\\numExp.txt"
    with open(filepath, "r+") as f:
        with lock:
            # קריאת הערך הנוכחי
            current_value = int(f.read())
            # עדכון הערך ב-1
            new_value = current_value + 1
            # החלפת הערך בקובץ
            f.seek(0)  # חזרה לתחילת הקובץ
            f.write(str(new_value))
            return current_value if current_value != 1 else ""


def calculate_object_angle(box, img_width, img_height):
    # שדה הראייה האופקי במצלמה (במקרה זה π רדיאנים)
    fov_x = math.pi

    # מרכז התיבה ב-י ו-x (box הוא tuple בצורת (label, x_center, y_center, width, height))
    x_center = box[1]
    y_center = box[2]

    # חישוב מיקום מרכז התיבה בפיקסלים
    x_pixel = x_center * img_width
    y_pixel = y_center * img_height

    # חישוב ההפרש בין מיקום מרכז התיבה למרכז התמונה
    delta_x = x_pixel - (img_width / 2)

    # חישוב הזווית שכל פיקסל מייצג
    angle_per_pixel = fov_x / img_width

    # חישוב הזווית של האובייקט יחסית למרכז המצלמה
    angle = delta_x * angle_per_pixel

    return angle


def detect_function(rand):
    time.sleep(timeSleepYolo)
    boxes = []
    angleMines = []
    data = numOfExp()
    try:
        file_path = "C:\\Users\\chena\\OneDrive\\The_snake\\server\\yolov5\\yolov5-master\\runs\\detect\\"
        current_path = file_path + "exp" + str(data)
        file_path = current_path + "\\labels\\" + str(rand) + ".txt"

        with open(file_path, 'r') as file:
            # קורא שורה בקובץ
            for line in file:
                # פיצול השורה של הליבל לכמה משתנים
                parts = line.split()
                # שמירת הסוג של האובייקט
                class_id = int(parts[0])
                # הוספת האובייקט למחסנית
                boxes.append(parts)
            # print(boxes)
            for box in boxes:
                data_numpy = np.array(box, dtype=np.float64)
                angel_radian = calculate_object_angle(data_numpy, imageSizeWinds, imageSizeHeight)
                angleMines.append(math.degrees(angel_radian))
                # print(math.degrees(angel_radian))
    except FileNotFoundError:
        angleMines.append(None)
    return angleMines


def yolo_function_to_detect():
    rand = random.randint(1, 10)
    command = fr'python "C:\Users\chena\OneDrive\The_snake\server\yolov5\yolov5-master\detect.py" --weights "C:\Users\chena\OneDrive\The_snake\server\yolov5\yolov5-master\runs\train\exp4\weights\last.pt" --imgsz 640 --save-txt --nosave --conf-thres 0.25 --source "C:\Users\chena\OneDrive\The_snake\server\yolov5\{rand}.png"'
    process = subprocess.Popen(command, shell=True)
    process.wait()
    return detect_function(rand)



