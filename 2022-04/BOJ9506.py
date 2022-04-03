import sys
while (num:=int(sys.stdin.readline()))>-1:
    arr=[1]
    p_factor=2
    while p_factor!=num:
        if num%p_factor:
            p_factor+=1
        else :
            arr.append(p_factor)
            p_factor+=1
    if (sum(arr))==num:
        print(str(num)+' = ',end='')
        for i in range(len(arr)-1):
            print(arr[i],end=' + ')
        print(arr[-1])
    else:
        print(str(num)+' is NOT perfect.')