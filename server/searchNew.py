import point
from directions import angleTest
from mov import move
from robot import my_robot
from situation import Situation
from stackInq import stack_Inq

stackSituation = []


def searchNew():
    if not stackSituation:
        return
    situationNew = Situation()
    situationNew.randomSituation()
    stackSituation.append(situationNew)
    if not situationNew.stackInq:
        stackSituation.pop()
        popStack()
        return
    else:
        stackSituation[-1].stackInq[-1].flag = 1
        move(stackSituation[-1].stackInq[-1].point, my_robot, stackSituation[-1].obstaclesList)
        my_robot.angleRandom = stackSituation[-1].stackInq[-1].angleRandom
        searchNew()


def popStack():
    my_robot.angleRandom = angleTest(180, my_robot.angleRandom)
    while stackSituation and stackSituation[-1].stackInq[-1].flag:
        move(stackSituation[-1].stackInq[-1].point, my_robot, stackSituation[-1].obstaclesList)
        stackSituation[-1].stackInq.pop()
        if not stackSituation[-1].stackInq:
            # stackSituation.pop()
            del stackSituation[-1]  # משחרר את האובייקט
            # return

    if stackSituation and not stackSituation[-1].stackInq[-1].flag:
        move(stackSituation[-1].stackInq[-1].point, my_robot, stackSituation[-1].obstaclesList)
        stackSituation[-1].stackInq[-1].flag = 1
        my_robot.angleRandom = stackSituation[-1].stackInq[-1].angleRandom
        searchNew()
    return


def start():
    startPoint = point.Point(0, 0)
    my_robot.set(startPoint, 90, 90, 30, [0, 1])
    first = Situation()
    startPoint = point.Point(0, 0)
    startInq = stack_Inq(startPoint, 90)
    startInq.flag = 1
    first.stackInq.append(startInq)
    stackSituation.append(first)
    searchNew()

