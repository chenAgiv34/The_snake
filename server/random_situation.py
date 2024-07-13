import math
import os
import directions
import mapDB
from data import objectWidthMin, objectWidthMax, widthRobot
from mov import angle_between_vectors
from point import Point
from robot import my_robot
import point
import random

# הגרלת קירות
def randomWell():
    # מערך קירות בסיטואציה הנוכחית
    walls = []
    # כל wall מכיל start ו end שבתוכו יש x ו y
    rand = random.randint(1, 5)

    # print(f" angelRandom: {my_robot.angelRandom}")
    print(rand)
    filepath = os.path.join("C:\\Users\\chena\\OneDrive\\The_snake\\server", f"situation_{rand}.txt")
    f = open(filepath, 'r')
    line = f.readline().strip()
    while line:
        wall = []
        for i in range(2):
            arr = line.split(",")
            pointWall = point.Point(int(arr[0]), int(arr[1]))
            wall.append(pointWall)
            line = f.readline().strip()
            pointWallMap = point.Point(int(arr[0]), int(arr[1]))
            temp = directions.directions(pointWallMap, my_robot.angleRandom)
            pointWallMap = point.add(temp, my_robot.point)
            mapDB.walls.append((pointWallMap.x, pointWallMap.y))
        walls.append(wall)

    return walls


def compare_points(item):
    return item[0].x


def insideTheSquare(walls, countRand):
    randPoints = []
    maxY = maxWallY(walls)

    for rand in range(countRand + 2):
        x = random.randint(int(walls[-1][-1].x) + 1, int(walls[0][0].x) - 1)
        y = random.randint(0, maxY - 1)
        rand_p = Point(x, y)
        rand_p = directions.directions(rand_p, my_robot.angleRandom)
        rand_p = point.add(rand_p, my_robot.point)
        random_width = round(random.uniform(objectWidthMin, objectWidthMax), 2)
        vp = point.displacement_vector(rand_p, my_robot.point)

        angle_obs = angle_between_vectors(my_robot.vector, [vp.x, vp.y])

        def get_key(obj):
            return obj[0].x

        def binary_search(arr, key):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if get_key(arr[mid]) < key:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        # print(f"beffor{rand_p}")
        rand_p = directions.directions(rand_p, my_robot.angleRandom)
        # print(f"after{rand_p}")
        index = binary_search(randPoints, rand_p.x)
        randPoints.insert(index, [rand_p, random_width, angle_obs])
        # print(f"Inserted at index {index}: {randPoints[index]}")  # Debug print
        j = 1
        l = 0
        pointIndexLeft = Point(randPoints[index][0].x - (randPoints[index][1] / 2), randPoints[index][0].y)
        pointIndexRight = Point(randPoints[index][0].x + (randPoints[index][1] / 2), randPoints[index][0].y)

        while index - j >= 0 and l < len(randPoints[index - j]) and pointIndexLeft.x - (
                randPoints[index - j][-3].x + (randPoints[index - j][-2] / 2)) < widthRobot:
            if point.distance(
                    Point(randPoints[index - j][l].x + randPoints[index - j][l + 1] / 2, randPoints[index - j][l].y),
                    pointIndexLeft) < widthRobot:
                randPoints[index - j] += randPoints[index]
                del randPoints[index]
                index -= j
                l = 0
            elif l + 4 < len(randPoints[index - j]):
                l += 3
            else:
                j += 1
        j = 1
        l = 0
        while 0 < index + j < len(randPoints) and l + 1 < len(randPoints[index + j]) and (
                randPoints[index + j][l].x - randPoints[index + j][l + 1] / 2 - pointIndexRight.x) < widthRobot:
            if point.distance(
                    Point(randPoints[index + j][l].x - randPoints[index + j][l + 1] / 2, randPoints[index + j][l].y),
                    pointIndexRight) < widthRobot:
                randPoints[index] += randPoints[index + j]
                del randPoints[index + j]
                index += j
                l = 0
            elif l + 3 != len(randPoints[index + j]):
                l += 3
            else:
                j += 1

    print(randPoints)
    return randPoints



# הגרלת מכשולים
def randomObstacles(walls):
    arr = [0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1]  # כמות מכשולים
    rand = random.randint(0, len(arr) - 1)
    obs = insideTheSquare(walls, arr[rand])
    return obs


def maxWallY(walls):
    maxY = 0
    for wall in walls:
        for point in wall:
            if maxY < int(point.y):
                maxY = int(point.y)
    return maxY


# הגרלת בני אדם
def randomPerson(walls):
    arr = [0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1]  # כמות מכשולים
    rand = random.randint(0, len(arr) - 1)
    return insideTheSquare(walls, 5)


# הגרלות
def random_situation():
    walls = randomWell()
    obstaclesList = randomObstacles(walls)
    person = randomPerson(walls)
    for i in range(len(walls)):
        for j in range(len(walls[i])):
            walls[i][j] = point.add(directions.directions(walls[i][j], my_robot.angleRandom), my_robot.point)
    return walls, obstaclesList, person
