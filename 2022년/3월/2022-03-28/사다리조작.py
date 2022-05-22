import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder=[[0]*(N+1) for _ in range(H+1)]
line=[0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b],ladder[a][b+1] = b+1, b
    line[b+1]+=1

def check(ladder):
    for i in range(1, N+1):
        y=i
        for j in range(1, H+1):
            if ladder[j][y]:
                y=ladder[j][y]
        if y!=i: return False
    return True

ans=4
def dfs(ladder, count, x, y):
    global ans
    if count>=ans:
        return
    elif check(ladder):
        ans=min(ans, count)
        return
    odd=0
    for l in line:
        if l%2: odd+=1
    if odd>3-count: return
    for i in range(x, H+1):
        for j in range(1, N):
            if i==x and j<y: continue
            if ladder[i][j]==0 and ladder[i][j+1]==0:
                ladder[i][j], ladder[i][j+1] = j+1,j
                line[j+1]+=1
                dfs(ladder, count+1, i, j)
                ladder[i][j], ladder[i][j+1] = 0,0
                line[j+1]-=1
    return

dfs(ladder, 0, 1, 1)

if ans>3: print(-1)
else: print(ans)