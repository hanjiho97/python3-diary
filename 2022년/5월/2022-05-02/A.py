import sys
input=sys.stdin.readline

for _ in range(int(input())):
    x,y=map(int, input().split())
    if y%x: print('%d %d'%(0,0))
    else: print('%d %d'%(1, y//x))