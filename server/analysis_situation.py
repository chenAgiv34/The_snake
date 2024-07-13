import threading
from threading import Thread, Lock
import mapDB
import point
from data import minDistanceForCameraDetection, angleRangeOfTheMiddleOfTheImage, progressPoint
from data_inquires import data_inquiries
from directions import placeInq, directions, angleTest, directions2
from facerecog import facerecog
from mov import move, angle_between_vectors
from point import cmp, Point
from robot import my_robot, Robot
from stackInq import stack_Inq
from yolov5 import yolo_function_to_detect

inq = data_inquiries()
locations = {
            'abducted': mapDB.abducted,
            'terrorists': mapDB.terrorists
            }

def identify_inquiries(walls):
    # walls = orderWalls(walls)
    inqMidArr = []
    progress = directions(Point(0, progressPoint), my_robot.angleRandom)
    my_robot_point = directions(Point(my_robot.point.x - progress.x, my_robot.point.y - progress.y), my_robot.angleRandom)
    p1 = directions(walls[0][0], my_robot.angleRandom)
    p2 = directions(walls[-1][-1], my_robot.angleRandom)
    if p1.y != my_robot_point.y:
        p1 = Point(p1.x, my_robot_point.y)
        p1 = directions(p1, my_robot.angleRandom)
        i = [p1, walls[0][0]]
        inqMidArr = addInquiriesToStack(i, inqMidArr)
    if p2.y != my_robot_point.y:
        p2 = Point(p2.x, my_robot_point.y)
        p2 = directions(p2, my_robot.angleRandom)
        i = [p2, walls[0][0]]
        inqMidArr = addInquiriesToStack(i, inqMidArr)

    for i in range(len(walls) - 1):
        if not cmp(walls[i][1], walls[i + 1][0]):
            i = [walls[i][1], walls[i + 1][0]]
            inqMidArr = addInquiriesToStack(i, inqMidArr)
    return inqMidArr

#VVV
def addInquiriesToStack(i, inqMidArr):
    dire = placeInq(i)
    p = Point(float((float(i[0].x) + float(i[1].x)) / 2),
              float((float(i[0].y) + float(i[1].y)) / 2))
    if inq.add_inquiries(p):
        inqValue = stack_Inq(p, dire)
        # c = inqValue.point
        return insert_sorted(inqMidArr, inqValue)

#VVV
def insert_sorted(points, new_point):
    try:
        new_point_distance = point.distance(new_point.point, my_robot.point)
        # חיפוש בינארי למצוא את המיקום להוספת הנקודה החדשה
        low, high = 0, len(points)
        while low < high:
            mid = (low + high) // 2
            if point.distance(points[mid].point, my_robot.point) < new_point_distance:
                high = mid
            else:
                low = mid + 1

        # הוספת הנקודה החדשה במקום המתאים
        points.insert(low, new_point)
    except TypeError:
        points = []
    return points


def mine_detection(points, returnToPoint, obstaclesList, lock):
    point_obst = points[0]
    point_obst = directions2(point_obst, my_robot.angleRandom)
    # print(point_obst)
    # temp = directions(point_obst, my_robot.angleRandom)
    # point_obst = point.add(temp, my_robot.point)
    part_robot = Robot(my_robot.point.x, my_robot.point.y, my_robot.orientation, my_robot.angleRandom,
                       my_robot.velocity, my_robot.vector)
    j = 0
    while j < len(points):
        if point.distance(point_obst, part_robot.point) > minDistanceForCameraDetection:
            # X מטר לפני
            point_obst = point.find_point_B(part_robot.point, point_obst, minDistanceForCameraDetection)
            move(point_obst, part_robot, obstaclesList)
        else:
            vp = point.displacement_vector(part_robot.point, point_obst)
            part_robot.orientation = angleTest(part_robot.orientation, angle_between_vectors([vp.x, vp.y], part_robot.vector))
        angles = yolo_function_to_detect()
        j += 3
    move(returnToPoint, part_robot, obstaclesList)
    for angle in angles:
        if angle is not None and -angleRangeOfTheMiddleOfTheImage < int(angle) < angleRangeOfTheMiddleOfTheImage:
            with lock:
                mapDB.mines.append((round(point_obst.x, 2), round(point_obst.y, 2)))


def person_detection(points, returnToPoint, obstaclesList, lock):
    point_person = points[0]
    # temp = directions(point_person, my_robot.angleRandom)
    # point_person = point.add(temp, my_robot.point)
    point_person = directions2(point_person, my_robot.angleRandom)
    part_robot = Robot(my_robot.point.x, my_robot.point.y, my_robot.orientation, my_robot.angleRandom,
                       my_robot.velocity, my_robot.vector)
    if point.distance(point_person, part_robot.point) > minDistanceForCameraDetection:
        # X מטר לפני
        point_obst = point.find_point_B(part_robot.point, point_person, minDistanceForCameraDetection)
        move(point_obst, part_robot, obstaclesList)

    arrFaces, numImg = facerecog()
    move(returnToPoint, part_robot, obstaclesList)

    if arrFaces:
        with lock:
            for face in arrFaces:
                key = 'abducted' if face != 'Unknown' else 'terrorists'
                locations[key].append(
                    ((round(point_person.x, 2), round(point_person.y, 2)), face) if key == 'abducted' else (
                    round(point_person.x, 2), round(point_person.y, 2)))
        # else:
        #     with lock:
        #         mapDB.unrecognizedFace.append((point_person.x, point_person.y))
    with lock:
        mapDB.arrNumImg.append((numImg, (round(point_person.x, 2), round(point_person.y, 2))))


def analysis_obstacles_person(obstacles, person, obstaclesList):
    threads = []
    lock = Lock()
    returnToPoint = my_robot.point
    # num_threads = len(obstacles) + len(person)  # או קבלת מספר התהליכונים באופן דינמי
    for i in range(len(obstacles)):
        thread = threading.Thread(target=mine_detection,
                                  args=(point := obstacles[i], returnToPoint, obstaclesList, lock))
        threads.append(thread)
        # Start the thread
        thread.start()
    for i in range(len(person)):
        thread = threading.Thread(target=person_detection,
                                  args=(point := person[i], returnToPoint, obstaclesList, lock))
        threads.append(thread)
        # Start the thread
        thread.start()
    for thread in threads:
        thread.join()


def analysis_situation(walls, obstacles, obstaclesList, person):
    analysis_obstacles_person(obstacles, person, obstaclesList)
    inqs = identify_inquiries(walls)
    return inqs
