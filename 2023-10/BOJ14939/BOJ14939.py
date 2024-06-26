# 14939번 불 끄기
# https://www.acmicpc.net/problem/14939
import sys, os

sys.stdin = open("{}/BOJ14939.txt".format(os.path.dirname(os.path.realpath(__file__))))
sys.setrecursionlimit(10**8)
# 앞으로 상하좌우 탐색은 이렇게 해야겠다.
in_range = lambda y, x: 0 <= y < 10 and 0 <= x < 10
board = [[0 for _ in range(10)] for _ in range(10)]
dy = [0, 0, 1, 0, -1]
dx = [0, 1, 0, -1, 0]


def press(b, y, x):
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        if in_range(ny, nx):
            b[ny][nx] = (b[ny][nx] + 1) % 2


for i in range(10):
    line = input()
    for j in range(len(line)):
        if line[j] == "O":
            board[i][j] = 1

first_line_press_case = [101] * (1 << 10)
for case in range(1 << 10):
    tmp_board = [board[i][:] for i in range(10)]  # copy board to tmp board
    cnt = 0

    # set case
    mask = 1
    for j in range(9, -1, -1):
        if case & mask:
            press(tmp_board, 0, j)
            cnt += 1
        mask <<= 1

    # 2번 줄부터 끝까지
    for i in range(1, 10):
        for j in range(10):
            if tmp_board[i - 1][j]:  # 현재 위치 위에 전구가 켜져있으면
                press(tmp_board, i, j)  # 현재 위치 press
                cnt += 1

    # 만일 마지막줄 전구 다 꺼져있으면 성공!
    if sum(tmp_board[9]) == 0:
        first_line_press_case[case] = cnt

print(min(first_line_press_case))
