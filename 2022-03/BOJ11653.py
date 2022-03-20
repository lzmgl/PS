import sys
num = int(sys.stdin.readline())
'''
if num==1:
    quit()
p_factor=1
while p_factor!=num:
    p_factor+=1
    while num%p_factor==0:
        if num==p_factor:
            break
        print(p_factor)
        num=num//p_factor
        p_factor=2
print(num)
'''
p_factor=2
while num>1:
    if num%p_factor:
        p_factor+=1
    else :
        print(p_factor)
        num/=p_factor