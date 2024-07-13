import torch
from PIL import Image

# טעינת המודל שעבר הכשרה (המודל צריך להיות כאן באותה התיקייה)
model = torch.load('yolov5x.pt')
# טעינת התמונה
image_path = "data/images/2.jpg"
image = Image.open(image_path).convert("RGB")

# ניתוח
results = model(image)

# הדפסת התוצאות
results.print()

# אם יש זיהויים, הדפס "yes", אחרת הדפס "no"
if any(results.xyxy[0]):
    print("yes")
else:
    print("no")

#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
