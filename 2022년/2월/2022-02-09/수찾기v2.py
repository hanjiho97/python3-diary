import sys
input = sys.stdin.readline

N = int(input())
num = set(map(int, input().split()))
M = int(input())
tar = list(map(int, input().split()))

for t in tar:
    if t in num:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')