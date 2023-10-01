# 9328번 열쇠
# https://www.acmicpc.net/problem/9328
import sys, os

sys.stdin = open("{}/BOJ9328.txt".format(os.path.dirname(os.path.realpath(__file__))))
T = int(sys.stdin.readline())
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    c = [[0] * (w + 2) for _ in range(h + 2)]
    q.append([x, y])
    c[x][y] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if not c[nx][ny]:
                    if data[nx][ny] == ".":
                        c[nx][ny] = 1
                        q.append([nx, ny])
                    elif data[nx][ny].islower():
                        door[ord(data[nx][ny]) - ord("a")] = 1
                        q = deque()
                        c = [[0] * (w + 2) for _ in range(h + 2)]
                        data[nx][ny] = "."
                        q.append([nx, ny])
                    elif data[nx][ny].isupper():
                        if door[ord(data[nx][ny]) - ord("A")]:
                            c[nx][ny] = 1
                            data[nx][ny] = "."
                            q.append([nx, ny])
                    elif data[nx][ny] == "$":
                        c[nx][ny] = 1
                        cnt += 1
                        data[nx][ny] = "."
                        q.append([nx, ny])
    print(cnt)


for _ in range(T):
    data = []
    h, w = map(int, sys.stdin.readline().split())
    data = [list(sys.stdin.readline().strip()) for _ in range(h)]
    keys = list(sys.stdin.readline().strip())
    door = [0] * 26

    for i in data:
        i.insert(0, ".")
        i.append(".")
    data.insert(0, ["."] * (w + 2))
    data.append(["."] * (w + 2))

    for key in keys:
        if key != "0":
            door[ord(key) - ord("a")] = 1

    for i in range(h):
        for j in range(w):
            if ord("A") <= ord(data[i][j]) <= ord("Z"):
                if door[ord(data[i][j]) - ord("A")]:
                    data[i][j] = "."
    bfs(0, 0)
