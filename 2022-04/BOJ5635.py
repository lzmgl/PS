import sys
N=int(sys.stdin.readline())
arr=[]
for _ in range(N):
    name, day, month, year = sys.stdin.readline().split()
    month=month.zfill(2)
    day=day.zfill(2)
    year=year.zfill(4)
    birth=int(year+month+day)
    tmp = [name, birth]
    arr.append(tmp)
maxN=0
minN=99999999
for i in range(N):
    maxN=max(maxN, arr[i][1])
    minN=min(minN, arr[i][1])
    if arr[i][1]==maxN:
        res=arr[i][0]
    if arr[i][1]==minN:
        res2=arr[i][0]
print(res)
print(res2)