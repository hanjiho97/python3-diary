N,M=map(int, input().split())
s=set()
ans=0
for _ in range(N):
    s.add(input())
for _ in range(M):
    target=input()
    if target in s: ans+=1
print(ans)