# 6439번 교차
# https:#www.acmicpc.net/problem/6439
import sys, os

sys.stdin = open("{}/BOJ6439.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())


def ccw(a, b, c):
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (c[0] - a[0], c[1] - a[1])
    res = v1[0] * v2[1] - v1[1] * v2[0]
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0


def check(w, z, x, y):
    a = (x[0], x[1])
    b = (y[0], y[1])

    r1 = (w[0], w[1])
    r2 = (z[0], z[1])

    ccwA = ccw(a, b, r1) * ccw(a, b, r2)
    ccwB = ccw(r1, r2, a) * ccw(r1, r2, b)

    if ccwA == 0 and ccwB == 0:
        if r1[0] == r2[0]:
            if max(a[1], b[1]) < min(r1[1], r2[1]) or max(r1[1], r2[1]) < min(
                a[1], b[1]
            ):
                return 0
        elif r1[1] == r2[1]:
            if max(a[0], b[0]) < min(r1[0], r2[0]) or max(r1[0], r2[0]) < min(
                a[0], b[0]
            ):
                return 0

    return ccwA <= 0 and ccwB <= 0


def determine(data):
    x1, y1, x2, y2 = data[:4]  # line
    minx = min(x1, x2)
    miny = min(y1, y2)
    maxx = max(x1, x2)
    maxy = max(y1, y2)
    p1 = (x1, y1)
    p2 = (x2, y2)

    a, b, c, d = data[4:]  # rect
    xl = min(a, c)
    xr = max(a, c)
    yt = max(b, d)
    yb = min(b, d)

    r1 = (xl, yt)
    r2 = (xl, yb)
    r3 = (xr, yt)
    r4 = (xr, yb)

    if xl <= minx and maxx <= xr and yb <= miny and maxy <= yt:
        return "T"
    if (
        check(r1, r2, p1, p2)
        or check(r1, r3, p1, p2)
        or check(r3, r4, p1, p2)
        or check(r2, r4, p1, p2)
    ):
        return "T"

    return "F"


for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    print(determine(data))
