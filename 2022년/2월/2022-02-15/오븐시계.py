import sys
input = sys.stdin.readline
A, B = map(int, input().split())
C = int(input())
print((A+(C+B)//60)%24, end=' ')
print((C+B)%60)