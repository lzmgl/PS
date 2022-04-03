import sys
arr1 = [0]*1001
arr2 = [0]*1001
for i in range(3):
    a1, b1 = map(int,sys.stdin.readline().split())
    arr1[a1]+=1
    arr2[b1]+=1
print(arr1[arr1>1])
print(arr2[arr2>1])