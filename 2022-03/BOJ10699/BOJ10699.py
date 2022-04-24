# 10699번 오늘 날짜
# https://www.acmicpc.net/problem/10699
import sys, os, datetime
sys.stdin = open('{}/BOJ10699.txt'.format(os.path.dirname(os.path.realpath(__file__))))
d=datetime.datetime.utcnow() + datetime.timedelta(hours=9)
m='{:02d}'.format(d.month)
print(f"{d.year}-{m}-{d.day}")