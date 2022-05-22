import sys
input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()
dp=[0]*len(second)

for i in range(len(first)):
    check=0
    for j in range(len(second)):
        if check<dp[j]:
            check=dp[j]
        elif first[i]==second[j]:
            dp[j]=check+1
print(max(dp))