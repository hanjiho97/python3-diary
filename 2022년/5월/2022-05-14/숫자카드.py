import sys
input=sys.stdin.readline

N=int(input())
num=set(input().split())
M=int(input())
for n in input().split():
    if n in num: print('1', end=' ')
    else: print('0', end=' ')