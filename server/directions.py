import math
import point

angles = {0: 180, 180: 0, 270: 270, 90: 90}

def directions(point_0, angle):
    # שזה יסתדר מיחוץ לפונקציה
    if angle == 90:
        return point_0
    elif angle == 0:
        return point.Point(point_0.y, -point_0.x)
    elif angle == 180:
        return point.Point(-point_0.y, point_0.x)
    elif angle == 270:
        return point.Point(-point_0.x, -point_0.y)


def directions2(p, angle):
    return directions(p, angles[angle])






def angleTest(initial_angle, delta_angle):
    new_angle = initial_angle + delta_angle
    normalized_angle = new_angle % 360
    if normalized_angle < 0:
        normalized_angle += 360

    return normalized_angle


def angle_vector(myPoint):
    base = abs(myPoint.x)
    # צלע (גובה)
    height = abs(myPoint.y)
    if myPoint.x == 0:
        return 0 if myPoint.y > 0 else 180
    if point.y == 0:
        return 90 if myPoint.x > 0 else 270
    # חישוב הזווית (במעלות)
    angle_degrees = math.degrees(math.atan(height / base))
    return 90 - angle_degrees



def placeInq(inq):
    try:
        inqStart, inqEnd = inq[0], inq[1]
        vector = point.unit_vector(inqEnd, inqStart)
        v = int(vector.x), int(vector.y)
        angle = {(1, 0): 270, (-1, 0): 90, (0, 1): 0, (0, -1): 180}
        return angle[v]
    except KeyError:
        print(KeyError)



