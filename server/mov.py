import sys

import numpy as np

from data import widthRobot
from directions import angleTest
from point import displacement_vector, Point, distance


class Circle:
    def __init__(self, center, radius):
        self.center = np.array([center.x, center.y])
        self.radius = radius

class Parallelogram:
    def __init__(self, vertices):
        self.vertices = [np.array([v.x, v.y]) for v in vertices]

def move(pointTarget, robot, obstaclesList):
    p1 = Point(robot.point.x - widthRobot, robot.point.y)
    p2 = Point(robot.point.x + widthRobot, robot.point.y)
    p3 = Point(pointTarget.x - widthRobot, pointTarget.y)
    p4 = Point(pointTarget.x + widthRobot, pointTarget.y)
    parallelogram = Parallelogram([p1, p2, p3, p4])

    flag = False
    pointOnTheParallelogram = []
    for i in obstaclesList:
        lenBlock = len(i)
        if i[0].x - i[1] / 2 <= p4.x and i[lenBlock - 3].x + i[lenBlock - 2] / 2 >= p1.x:
            # נבדוק את הנקודה במקבלית
            count = 0
            while count < lenBlock and not flag:
                circle = Circle(i[count], i[count + 1])
                flag = is_circle_intersecting_parallelogram(circle, parallelogram)
                count = count + 3
        elif i[0].x - i[1] / 2 > p4.x:
            movezooz(pointTarget, robot)
            return
        if flag:
            maxY = 0
            minY = sys.float_info.max
            k = 0
            while k < len(i):
                maxY = i[k].y + i[k + 1] / 2 if maxY < i[k].y + i[k + 1] / 2 else maxY
                minY = i[k].y - i[k + 1] / 2 if minY > i[k].y - i[k + 1] / 2 else minY
                k += 3
            pointOnTheParallelogram.append((Point(i[0].x - i[1] / 2 - widthRobot / 2, i[0].y),
                                            Point(i[lenBlock - 3].x + i[lenBlock - 2] / 2, i[0].y), Point(i[0].x, minY),
                                            Point(i[0].x, maxY)))
    if not flag:
        movezooz(pointTarget, robot)
    else:
        moveVectorsNew(pointOnTheParallelogram, robot, pointTarget)


def angle_between_vectors(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    # חישוב גודל הווקטורים
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0
    # מכפלה סקלרית
    dot_product = np.dot(v1, v2)
    # חישוב ערך הקוסינוס של הזוית בין הווקטורים עי חלוקת מכפלת הסקלר במכפלת הגדלים של הווקטור
    cos_angle = dot_product / (magnitude_v1 * magnitude_v2)
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    # הגבלת הערך בין 1 ל -1
    angle_rad = np.arccos(cos_angle)
    cross_product = np.cross(v1, v2)
    angle_deg = np.degrees(angle_rad)
    if np.all(cross_product == 0):
        return angle_deg
    elif cross_product < 0:
        angle_deg = -angle_deg
    # לבדוק אם הזוית היא בכיוון השעון או נגד

    return angle_deg


def movezooz(pointTarget, robot):
    vp = displacement_vector(pointTarget, robot.point)
    vpInList = [vp.x, vp.y]
    angleBetweenVectors = angle_between_vectors(robot.vector, vpInList)
    robot.vector = vpInList
    robot.orientation = angleTest(robot.orientation, angleBetweenVectors)
    print(f"x_robot: {robot.point.x:.2f}, y_robot: {robot.point.y:.2f}")
    robot.point.x = robot.point.x + vp.x
    robot.point.y = robot.point.y + vp.y
    print(f"x_pointTarget: {pointTarget.x:.2f}, y_pointTarget: {pointTarget.y:.2f}")
    print(f" orientation: {robot.orientation}")


# def is_circle_intersecting_parallelogram(circle, parallelogram):
#     # בדיקה אם מרכז המעגל נמצא בתוך המקבילית
#     if (parallelogram.x_min <= circle.center.x <= parallelogram.x_max and
#             parallelogram.y_min <= circle.center.y <= parallelogram.y_max):
#         return True
#
#     # בדיקה אם נקודה כלשהי על המעגל חותכת את המלבן
#     # חישוב הנקודה הקרובה ביותר על המלבן למרכז המעגל
#     closest = Point(max(parallelogram.x_min, min(circle.center.x, parallelogram.x_max)), max(parallelogram.y_min, min(circle.center.y, parallelogram.y_max)))
#     # אם המרחק קטן מרדיוס המעגל, יש חיתוך
#
#     return distance(circle.cente, closest) <= (circle.radius ** 2)

def moveVectorsNew(pointOnTheParallelogram, robot, pointTarget):
    pointOnTheParallelogram = sorted(pointOnTheParallelogram, key=lambda x: x[2].y)
    for i in range(len(pointOnTheParallelogram)):
        movezooz(pointOnTheParallelogram[i][2], robot)
        movezooz(pointOnTheParallelogram[i][0], robot)
        movezooz(pointOnTheParallelogram[i][3], robot)
        movezooz(pointTarget, robot)


def point_in_parallelogram(p, parallelogram):
    A, B, C, D = parallelogram
    AB = B - A
    AD = D - A
    AP = p - A

    dot00 = np.dot(AB, AB)
    dot01 = np.dot(AB, AD)
    dot02 = np.dot(AB, AP)
    dot11 = np.dot(AD, AD)
    dot12 = np.dot(AD, AP)
    #מבטא את הגורם המשותף המשולש בין הווקטורים
    denominator = dot00 * dot11 - dot01 * dot01
    if denominator == 0:
        return False

    invDenom = 1 / denominator
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom

    return (u >= 0) and (v >= 0) and (u + v <= 1)

def closest_point_on_segment(p, v, w):
    l2 = np.dot(w - v, w - v)
    if l2 == 0:
        return v
    t = np.clip(np.dot(p - v, w - v) / l2, 0, 1)
    projection = v + t * (w - v)
    return projection

def is_circle_intersecting_parallelogram(circle, parallelogram):
    # קבלת רשימת קודקודים של המקבילית
    vertices = parallelogram.vertices

    # בדיקה אם מרכז המעגל נמצא בתוך המקבילית
    if point_in_parallelogram(circle.center, vertices):
        return True

    closest_distance_squared = float('inf')
    for i in range(4):
        v = vertices[i]
        w = vertices[(i + 1) % 4]
        closest_point = closest_point_on_segment(circle.center, v, w)
        distance_squared = np.sum((circle.center - closest_point) ** 2)
        closest_distance_squared = min(closest_distance_squared, distance_squared)

    return closest_distance_squared <= circle.radius ** 2



