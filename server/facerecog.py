


import random
import numpy as np
import cv2
import os

from data import threshold

# סף מרחק מותר עבור אלגוריתם זיהוי פנים


# טען את Haar Cascade לזיהוי פנים
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade.empty():
    raise IOError("נכשל לטעון את Haar Cascade מ-'haarcascade_frontalface_default.xml'")

# פונקציה לחיתוך פנים מתמונה
def cut_faces(image, faces_coord):
    faces = []
    for (x, y, w, h) in faces_coord:  # חתוך חלקי פנים
        w_rm = int(0.2 * w / 2)
        faces.append(image[y: y + h, x + w_rm: x + w - w_rm])
    return faces  # החזר את הקואורדינטות של הפנים

# פונקציה לזיהוי פנים בתמונה סטטית
def recognize_image(image_path):
    images = []
    labels = []
    arrFaces = []
    labels_dic = {}
    people = [person for person in os.listdir("people_folder") if os.path.isdir(os.path.join("people_folder", person))]

    # טען נתוני אימון
    for i, person in enumerate(people):
        labels_dic[i] = person
        for img in os.listdir(f"people_folder/{person}"):
            image = cv2.imread(f'people_folder/{person}/{img}', 0)
            if image is not None:
                images.append(image)
                labels.append(i)

    if not images:
        raise ValueError("לא נמצאו תמונות אימון. ודא שהתיקייה 'people_folder' מכילה תמונות.")

    labels = np.array(labels)
    rec_lbhp = cv2.face.LBPHFaceRecognizer_create()  # צור מזהה פנים LBHP
    rec_lbhp.train(images, labels)  # אימן את המודל

    # טען את התמונה
    frame = cv2.imread(image_path)
    if frame is None:
        # print("לא זוהו פנים")
        return
    try:
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)  # קבל קואורדינטות פנים במסגרת
    except cv2.error as e:
        # print("לא זוהה אדם בתמונה")
        return

    if len(faces) == 0:
        # print("לא זוהו פנים")
        return []

    for (x, y, w, h) in faces:
        cut_face = frame[y: y + h, x: x + w]
        face = cv2.cvtColor(cut_face, cv2.COLOR_BGR2GRAY)
        face = cv2.equalizeHist(face)  # היסטוגרם השוואתי
        face = cv2.resize(face, (100, 100), interpolation=cv2.INTER_CUBIC)  # שינוי גודל תמונת הפנים

        collector = cv2.face.StandardCollector_create()
        rec_lbhp.predict_collect(face, collector)
        conf = collector.getMinDist()  # מצא את ההתאמה הקרובה ביותר

        pred = collector.getMinLabel()
        if conf < threshold:  # אם נמצאה התאמת פנים
            txt = labels_dic[pred].upper()  # קבל את שם האדם
        else:
            txt = 'Unknown'  # אם לא זוהה, תייג כ'לא ידוע'
        arrFaces.append(txt)
    return arrFaces

def facerecog():
    rand = random.randint(1, 7)
    image_path = f"C:\\Users\\chena\\OneDrive\\The_snake\\client\\public\\face\\{rand}.jpg"
    return recognize_image(image_path), rand
