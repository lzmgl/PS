# 1018번 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
black_board=[]
word_dic={0:'B', 1:'W'}
for i in range(8):
    tmp=[]
    for j in range(8):
        tmp.append(word_dic[(i+j)%2])
    black_board.append(tmp)
answer=65

def comp(x, y):
    ans_b=0
    comp88=[]
    for i in range(x, x+8):
        tmp=[]
        for j in range(y, y+8):
            tmp.append(chess[i][j])
        comp88.append(tmp)
    for i in range(8):
        for j in range(8):
            if comp88[i][j]!=black_board[i][j]:
                ans_b+=1
    return min(ans_b, 64-ans_b)
    
import sys
N, M=map(int,sys.stdin.readline().rstrip().split())
chess=[ list(sys.stdin.readline().rstrip()) for _ in range(N)]

for i in range(N-7):
    for j in range(M-7):
        answer=min(answer,comp(i, j))
print(answer)