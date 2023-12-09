# 2162번 선분 그룹
# https://www.acmicpc.net/problem/2162
import sys, os

sys.stdin = open("{}/BOJ2162.txt".format(os.path.dirname(os.path.realpath(__file__))))


from collections import Counter


def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


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
    return ccwA <= 0 and ccwB <= 0


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    parent = [i for i in range(N)]
    lines = []
    for i in range(N):
        tmp = list(map(int, sys.stdin.readline().split()))
        tmp = [(tmp[0], tmp[1]), (tmp[2], tmp[3])]
        lines.append(tmp)
    for i in range(N):
        for j in range(i + 1, N):
            if check(lines[i][0], lines[i][1], lines[j][0], lines[j][1]):
                union(parent, i, j)
    parent = [find(parent, x) for x in parent]

    cnt = Counter(parent)
    print(len(cnt))
    print(max(cnt.values()))
