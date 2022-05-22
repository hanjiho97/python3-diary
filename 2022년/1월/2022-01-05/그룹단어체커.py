import sys
input = sys.stdin.readline

N = int(input())
ans=0
for i in range(N):
    S = input().rstrip()
    bw=''
    C = ''
    for i in range(len(S)):
        if S[i]==bw:
            continue
        elif C.find(S[i])==-1:
            C+=S[i]
        else:
            ans-=1
            break
        bw=S[i]

ans+=N
print(ans)    