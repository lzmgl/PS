import sys
data=[]
scores = []
for i in range(5):
    tmp = int(sys.stdin.readline())
    if tmp<40:
        tmp=40
    scores.append(tmp)
print(int(sum(scores)/len(scores)))