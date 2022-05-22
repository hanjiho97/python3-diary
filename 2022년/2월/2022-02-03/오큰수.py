import sys
input = sys.stdin.readline

N = int(input())
series=list(map(int, input().split()))

ans=[-1]*N
stack=[0]

for i in range(1,N):
    if series[stack[-1]]>=series[i]:
        stack.append(i)
    else:
        while True:
            ans[stack.pop()]=series[i]
            if not stack:
                stack.append(i)
                break
            elif series[stack[-1]]>=series[i]:
                stack.append(i)
                break

print(*ans)