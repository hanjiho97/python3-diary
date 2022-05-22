import sys
input = sys.stdin.readline
N = int(input())
factor = sorted(map(int, input().split()))


print(factor[0]*factor[-1])