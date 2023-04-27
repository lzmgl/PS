# 1197번 최소 스패닝 트리 MST 크루스칼
# https://www.acmicpc.net/problem/1197
import sys, os
sys.stdin = open('{}/BOJ1197.txt'.format(os.path.dirname(os.path.realpath(__file__))))

def ancestor(node):
    if parent[node] == node:
        return node
    else:
        parent[node]=ancestor(parent[node]) #경로 압축
        return parent[node]

v, e = map(int,input().split())
data = sorted([list(map(int,input().split())) for _ in range(e)], key=lambda x:x[2])
#가중치로 sorting
parent = [i for i in range(v + 1)]

answer = 0
for a,b,c in data:
    parent_a, parent_b = ancestor(a), ancestor(b)
    #부모 다르면 노드 합류
    if parent_a != parent_b:
        answer += c

        #기준 하나로 노드합류
        if parent_a > parent_b:
            parent[parent_a] = b
            continue
        parent[parent_b] = a
        
print(answer)