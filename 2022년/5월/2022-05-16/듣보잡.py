import sys
input=sys.stdin.readline
N,M=map(int, input().split())

heard=set()
ans=[]
for _ in range(N):
    heard.add(input())
for _ in range(M):
    see=input()
    if see in heard: ans.append(see)
ans.sort()
print(len(ans))
for a in ans:
    print(a.rstrip())