import math
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def compareX(a, b):
    return a.x - b.x


def compareY(a, b):
    return a.y - b.y


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def bruteForce(P, n):
    min_dist = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_dist:
                min_dist = dist(P[i], P[j])
    return min_dist


def min(x, y):
    return x if x < y else y


def stripClosest(strip, size, d):
    min_dist = d
    strip = sorted(strip, key=lambda point: point.y)

    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j].y - strip[i].y) >= min_dist:
                break
            if dist(strip[i], strip[j]) < min_dist:
                min_dist = dist(strip[i], strip[j])
    return min_dist


def closestUtil(P, n):
    if n <= 3:
        return bruteForce(P, n)
    mid = n // 2
    midPoint = P[mid]
    dl = closestUtil(P, mid)
    dr = closestUtil(P[mid:], n - mid)
    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])
    return min(d, stripClosest(strip, len(strip), d))


def closest(P, n):
    P = sorted(P, key=lambda point: point.x)
    return closestUtil(P, n)


P = []
for i in range(0, 10):
    x = random.randint(0, 30)
    y = random.randint(0, 30)
    P.append(Point(x, y))
n = len(P)
print("Points :")
for i, point in enumerate(P):
    print(f"[{point.x}, {point.y}]")
print("The smallest distance is", closest(P, n))
