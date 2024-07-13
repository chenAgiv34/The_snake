import math


@staticmethod
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({float(self.x)}, {float(self.y)})"


def cmp(p1, p2):
    return False if p1.x != p2.x or p1.y != p2.y else True


def my_round(point):
    return Point(round(point.x, 1), round(point.y, 1))


def distance(point1, point2):
    return math.sqrt((float(point2.x) - float(point1.x)) ** 2 + (float(point2.y) - float(point1.y)) ** 2)


def find_point_B(A, C, BC):
    direction_vector_x = A.x - C.x
    direction_vector_y = A.y - C.y
    length_AC = distance(A, C)
    direction_vector_x /= length_AC
    direction_vector_y /= length_AC
    B = Point(C.x + direction_vector_x * BC, C.x + direction_vector_y * BC)
    return B

# point1 = Point(0, 0)
# point2 = Point(3, 8)
# point3 = Point(3, 8)
#
# print(distance(point3, point2))


# מחשבת את ווקטור התזוזה
def displacement_vector(point1, point2):
    # חישוב גודל וקטור ההפרש
    # חישוב וקטור היחידה
    # print(f"point1: {point1.x} ,{point1.y}")
    # print(f"x: {point2.x}, y: {point2.y}")

    vx = float(point1.x) - float(point2.x)
    vy = float(point1.y) - float(point2.y)
    vp = Point(vx, vy)
    return vp


def calculateAnAngleUsingPoint(point):
    angle_radians = math.atan2(point.y, point.x)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees

#אחרונה
def calculate_rotation_angle(robot_pos, target_pos, current_angle):
    # חישוב השיפוע
    m = 0 if (target_pos.x - robot_pos.x) == 0 else (target_pos.y - robot_pos.y) / (target_pos.x - robot_pos.x)

    # חישוב הזווית בין הקו המחבר את הנקודות לציר ה-X
    theta = math.degrees(math.atan(m))
    # הזווית הנוכחית של הרובוט
    # current_angle = my_robot.orientation
    # חישוב זווית ההסתובבות הנדרשת
    rotation_angle = current_angle - theta if current_angle > theta else theta - current_angle

    return rotation_angle


def unit_vector(point1, point2):
    vp = displacement_vector(point1, point2)
    v = distance(point1, point2)
    vp.x = vp.x / v
    vp.y = vp.y / v
    return vp


def add(point1, my_robot_point):
    point1.x = float(my_robot_point.x) + float(point1.x)
    point1.y = float(my_robot_point.y) + float(point1.y)
    return point1
# p1 = Point(-2, 6)
# p2 = Point(-7, 7)
# j = displacement_vector(p1, p2)
# print(j.x, j.y)

# def updatePoint():
