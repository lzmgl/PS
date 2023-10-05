# 14927번 전구 끄기
# https://www.acmicpc.net/problem/14927
import sys, os

sys.stdin = open("{}/BOJ14927.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())

sys.setrecursionlimit(10**8)

in_range = lambda y, x: 0 <= y < N and 0 <= x < N

board = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().strip().split()))
    board.append(row)
dy = [0, 0, 1, 0, -1]
dx = [0, 1, 0, -1, 0]


def press(b, y, x):
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        if in_range(ny, nx):
            b[ny][nx] = (b[ny][nx] + 1) % 2


first_line_press_case = [1234] * (1 << N)
for case in range(1 << N):
    tmp_board = [board[i][:] for i in range(N)]  # copy board to tmp board
    cnt = 0

    # set case
    mask = 1
    for j in range(N - 1, -1, -1):
        if case & mask:
            press(tmp_board, 0, j)
            cnt += 1
        mask <<= 1

    # 2번 줄부터 끝까지
    for i in range(1, N):
        for j in range(N):
            if tmp_board[i - 1][j]:  # 현재 위치 위에 전구가 켜져있으면
                press(tmp_board, i, j)  # 현재 위치 press
                cnt += 1

    # 만일 마지막줄 전구 다 꺼져있으면 성공!
    if sum(tmp_board[N - 1]) == 0:
        first_line_press_case[case] = cnt
ans = min(first_line_press_case)
print(ans if ans != 1234 else -1)
