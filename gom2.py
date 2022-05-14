import sys
import math
n=int(sys.stdin.readline())
cnt=0
s=sys.stdin.readline().rstrip()
num=s.count('C')
spliter=n-num+1
try:
    print(math.ceil(num/spliter))
except:
    print(num)