# 1991번 트리 순회
# https://www.acmicpc.net/problem/1991
import sys, os
sys.stdin = open('{}/BOJ1991.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
tree = {}
for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    tree[node] = [left, right]

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')