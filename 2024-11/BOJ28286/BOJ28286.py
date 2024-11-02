# 28286번 재채점을 기다리는 중
# https://www.acmicpc.net/problem/28286
import sys, os

sys.stdin = open("{}/BOJ28286.txt".format(os.path.dirname(os.path.realpath(__file__))))
N, K = map(int, sys.stdin.readline().split())
answer = list(map(int, sys.stdin.readline().split()))
data = list(map(int, sys.stdin.readline().split()))


def compare(answer, data):
    cnt = 0
    for i in range(len(answer)):
        if answer[i] == data[i]:
            cnt += 1
    return cnt


def push(data, i):
    tmp = data.copy()
    tmp.insert(i, 0)
    return tmp


def pull(data, i):
    tmp = data.copy()
    tmp.pop(i)
    tmp.append(0)
    return tmp


maxN = 0


def dfs(n, arr):
    global maxN
    maxN = max(compare(answer, arr), maxN)
    if n < K:
        for i in range(N):
            dfs(n + 1, push(arr, i))
            dfs(n + 1, pull(arr, i))


dfs(0, data)
print(maxN)
