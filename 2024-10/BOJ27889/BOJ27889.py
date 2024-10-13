# 27889번 특별한 학교 이름
# https://www.acmicpc.net/problem/27889
import sys, os

sys.stdin = open("{}/BOJ27889.txt".format(os.path.dirname(os.path.realpath(__file__))))
dic = {
    "NLCS": "North London Collegiate School",
    "BHA": "Branksome Hall Asia",
    "KIS": "Korea International School",
    "SJA": "St. Johnsbury Academy",
}
print(dic[sys.stdin.readline().strip()])
