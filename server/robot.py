from point import Point


class Robot:
    def __init__(self, x, y, orientation, angleRandom, velocity, vector):
        self.point = Point(x, y)
        self.orientation = orientation
        self.angleRandom = angleRandom
        self.velocity = velocity
        self.vector = vector

    def set(self, point, orientation, angleRandom, velocity, vector):
        self.point = point
        self.orientation = orientation
        self.angleRandom = angleRandom
        self.velocity = velocity
        self.vector = vector


my_robot = Robot(0, 0, 90, 90, 30, [0, 1])
