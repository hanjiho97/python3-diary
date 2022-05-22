import sys
input = sys.stdin.readline
ca = ['=', '-', 'dz=', 'lj', 'nj']
S = input().rstrip()
sum = len(S)
for c in ca:
    sum-=S.count(c)
print(sum)