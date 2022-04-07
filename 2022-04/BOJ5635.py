import sys
N=int(sys.stdin.readline())
arr=[]
for _ in range(N):
    name, day, month, year = sys.stdin.readline().split()
    month=month.zfill(2)
    day=day.zfill(2)
    year=year.zfill(4)
    birth=int(year+month+day)
    arr.append(list(name, birth))
maxN=0
for i in range(N):
    maxN=max(maxN, arr[0][i])
    if arr[i][1]==maxN:
        res=arr[i][0]
print(res)