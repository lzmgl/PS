# 16677번 악마 게임
# https://www.acmicpc.net/problem/16677
import sys, os

sys.stdin = open("{}/BOJ16677.txt".format(os.path.dirname(os.path.realpath(__file__))))
m = sys.stdin.readline().strip()

N = int(sys.stdin.readline())
gab = ""
max_jam = 0
for i in range(N):
    idx = 0
    mc = m[idx]
    tmp, jam = sys.stdin.readline().strip().split()
    for c in tmp:
        if c == mc:
            idx += 1
            if idx == len(m):
                break
            mc = m[idx]
    else:  # not in
        continue
    if max_jam < int(jam) / (len(tmp) - len(m)):
        max_jam = int(jam) / (len(tmp) - len(m))
        gab = tmp
print(gab if max_jam else "No Jam")
