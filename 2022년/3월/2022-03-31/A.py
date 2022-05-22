import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a and b or not b:
        print(a*1+b*2+1)
    elif not a:
        print(1)