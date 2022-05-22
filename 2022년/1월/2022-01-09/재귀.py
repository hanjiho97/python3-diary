import sys
input = sys.stdin.readline

N = int(input())

#기본적인 형태 만들기
s=[]
for i in range(N):
    b=[]
    for j in range(N+1):
        if(j==N):
            b.append('\n')
        else:
            b.append(' ')
    s.append(b)

def star(n, x, y):
    if(n==1):
        s[y][x]='*'
        return
    else:
        n=n//3
        return star(n,x,y), star(n, x, y+n), star(n, x, y+2*n), star(n, x+n, y), star(n, x+n, y+2*n), star(n, x+2*n, y), star(n, x+2*n, y+n), star(n, x+2*n, y+2*n)

star(N, 0, 0)

for i in range(N):
    for j in range(N+1):
        print(s[i][j], end='')