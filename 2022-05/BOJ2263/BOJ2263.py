# 2263번 트리의 순회
# https://www.acmicpc.net/problem/2263
import sys, os
sys.setrecursionlimit(100001)
sys.stdin = open('{}/BOJ2263.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
inorder=list(map(int, sys.stdin.readline().split()))
postorder=list(map(int, sys.stdin.readline().split()))
preorder=[]

idx_list=[0]*(N+1)

for i in range(N):
    idx_list[inorder[i]]=i

def preTree(instart, inend, poststart, postend):
    if instart>inend or poststart>postend:
        return
    root = postorder[postend]
    preorder.append(root)
    i = idx_list[root]
    left = i-instart
    preTree(instart, i-1, poststart, poststart + left - 1)
    preTree(i + 1, inend, poststart + left, postend - 1)

preTree(0, N-1, 0, N-1)

print(*preorder)

# inoder - 왼쪽 젤 바깥에서부터 쭉
#  1 2 3
#  2
# 1 3
# 프리오더는 - 젤 위에서부터야. <- postoder의 마지막부터, 
# 젤 위 레벨부터, 왼쪽으로 내려오는 순서.
# postoder - 1 3 2 왼쪽 젤 밑에서부터 level부터 오른쪽 순회 후 위로.
# postorder의 마지막 - root고, 인오더에서 루트가 나오기 전이 왼, 후가 오른쪽.
