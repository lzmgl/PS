# 5525번 IOIOI
# https://www.acmicpc.net/problem/5525
import sys, os
sys.stdin = open('{}/BOJ5525.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
S=sys.stdin.readline().strip()
cnt=0
Pn = 'O'* (2*N + 1)
Pn=list(Pn)
for i in range(len(Pn)):
    if i%2 == 0:
        Pn[i]='I'
Pn=''.join(Pn)
cnt=0

def computeLPS(pat, lps):
    leng = 0  # length of the previous longest prefix suffix

    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            # 일치하지 않는 경우
            if leng != 0:
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                leng = lps[leng-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[i] = 0
                i += 1

def KMP(pat, txt):
    global cnt
    Pi=[0]*len(pat)

    computeLPS(pat, Pi)
    i,j=0,0
    while i<len(txt):
        if pat[j]==txt[i]:
            i+=1
            j+=1
        elif pat[j] != txt[i]:
            if j!=0:
                j=Pi[j-1]
            else:
                i+=1
        if j==len(pat):
            cnt+=1
            j=Pi[j-1]

KMP(Pn, S)
print(cnt)