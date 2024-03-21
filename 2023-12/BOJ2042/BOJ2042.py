# 2042번 구간 합 구하기
# https://www.acmicpc.net/problem/2042
import sys, os

sys.stdin = open("{}/BOJ2042.txt".format(os.path.dirname(os.path.realpath(__file__))))

N, M, K = map(int, sys.stdin.readline().split())

l = []


for _ in range(N):
    l.append(int(sys.stdin.readline()))
segment_tree = [0] * (N * 4)


# 1. 트리 만들기
def init(start, end, idx):
    # start와 end가 같다면 리프노드이다.
    if start == end:
        segment_tree[idx] = l[start]
        return segment_tree[idx]

    # 현재 노드는 왼쪽 아래 노드와 오른쪽 아래 노드를 더한 값이다.
    mid = (start + end) // 2
    segment_tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return segment_tree[idx]


init(0, N - 1, 1)


# 2. 트리에서 값 찾기
def find(start, end, idx, left, right):
    # 찾으려는 범위가 start~end 범위보다 클 경우
    if start > right or end < left:
        return 0

    # 찾으려는 범위가 segment tree 노드안에 구현되어 있을 경우
    if start <= left and end >= right:
        return segment_tree[idx]

    # 코드를 동작시키기 위한 기본 코드
    # 현재 노드는 왼쪽아래 + 오른쪽아래 노드이다.
    mid = (left + right) // 2
    sub_sum = find(start, end, idx * 2, left, mid) + find(
        start, end, idx * 2 + 1, mid + 1, right
    )
    return sub_sum


# 3. 트리 값 바꿔주기
def update(left, right, idx, update_idx, update_data):
    # update 하려는 범위가 초과될 경우
    if left > update_idx or right < update_idx:
        return

    if left == right == update_idx:
        segment_tree[idx] = update_data
        return

    # 내가 관여하고 있는 노드들을 찾아서 바꿔준다 -> 재귀함수로 구현
    mid = (left + right) // 2

    update(left, mid, idx * 2, update_idx, update_data)
    update(mid + 1, right, idx * 2 + 1, update_idx, update_data)

    segment_tree[idx] = segment_tree[idx * 2] + segment_tree[idx * 2 + 1]


for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c)

    else:
        print(find(b - 1, c - 1, 1, 0, N - 1))
