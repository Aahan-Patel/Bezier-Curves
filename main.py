import math

distancePoints = lambda p0, p1: math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)


def closestPoint(p0, bezier):
    closestDist = distancePoints(p0, bezier[0])
    closestPoint = (0, 0)
    for i, j in enumerate(bezier):
        dist = distancePoints(p0, j)
        if dist < closestDist:
            closestPoint = j
    return closestPoint


def lerp(p0, p1, t):
    x = (1 - t) * p0[0] + t * p1[0]
    y = (1 - t) * p0[1] + t * p1[1]
    p = (x, y)
    return p


def cubicBezier(p0, p1, p2, p3, t):
    A = lerp(p0, p1, t)
    B = lerp(p1, p2, t)
    C = lerp(p2, p3, t)
    D = lerp(A, B, t)
    E = lerp(B, C, t)
    P = lerp(D, E, t)
    return P


bezier1 = []
bezier2 = []

numPoints = 10
for i in range(0, numPoints):
    bezier1.append(cubicBezier((1, 0), (2, 1), (3, 1), (4, 0), i / numPoints))
for j in range(0, numPoints):
    bezier2.append(cubicBezier((5, 0), (6, 1), (7, 1), (8, 0), j / numPoints))

p0 = bezier1[-1]
p1 = bezier2[0]
xdist = p0[0] - p1[0]
ydist = p0[1] - p1[1]
t1 = (p0[0] - (xdist / 3), p0[1] - (ydist / 3))
t2 = (p1[0] + (xdist / 3), p1[1] - (ydist / 3))
print(str(t1) + "," + str(t2))
points = []
for k in range(0, numPoints):
    points.append(cubicBezier(p0, t1, t2, p1, k / numPoints))

print(bezier1 + points + bezier2)
