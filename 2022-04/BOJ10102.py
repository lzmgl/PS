v=int(input())
a=input().count('A')
print('Tie' if v/2==a else 'AB'[a<v/2])