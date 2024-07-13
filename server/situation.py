import point

from analysis_situation import analysis_situation
from data import progressPoint
from directions import directions
from mov import move
from random_situation import random_situation
from robot import my_robot


class Situation:

    def __init__(self):
        self.stackInq = []
        self.obstaclesList = []

    def randomSituation(self):
        wall, self.obstaclesList, person = random_situation()

        progress = point.Point(0, progressPoint)
        progress = directions(progress, my_robot.angleRandom)
        progress = point.add(progress, my_robot.point)
        move(progress, my_robot, self.obstaclesList)
        self.stackInq = analysis_situation(wall, self.obstaclesList, self.obstaclesList, person)






