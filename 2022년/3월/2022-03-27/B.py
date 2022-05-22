import sys
from itertools import permutations
input = sys.stdin.readline

dp=[1]*501
for i in range(2,501):
    dp[i]=(dp[i-1]*(i**2))%998244353

for _ in range(int(input())):
    n=int(input())
    if n%2:
        print(0)
    else:
        print(dp[n//2])