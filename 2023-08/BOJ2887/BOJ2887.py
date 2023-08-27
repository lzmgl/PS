# 2887번 행성 터널
# https://www.acmicpc.net/problem/2887
import sys, os

sys.stdin = open("{}/BOJ2887.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())
parent = [i for i in range(N)]
ans = 0
data = []
edges = []


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    parent[y] = x


for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    data.append((x, y, z, i))
# edge 생성
for i in range(3):
    data.sort(key=lambda x: x[i])
    for j in range(1, N):
        edges.append((abs(data[j - 1][i] - data[j][i]), data[j - 1][3], data[j][3]))
# edge 정렬
edges.sort()

# 다른 set이면 합침
for i in range(len(edges)):
    if find(parent, edges[i][1]) != find(parent, edges[i][2]):
        union(parent, edges[i][1], edges[i][2])
        ans += edges[i][0]

print(ans)
