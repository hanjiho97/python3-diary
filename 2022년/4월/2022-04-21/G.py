import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    grid=[input().rstrip() for _ in range(n)]
    grid=list(map(list, zip(*grid)))
    for i in range(m):
        temp=''
        stone=0
        blank=0
        for j in range(n):
            if grid[i][j]!='o':
                if grid[i][j]=='*': stone+=1
                else: blank+=1
            else: 
                temp+='.'*blank+'*'*stone+'o'
                stone=0
                blank=0
        grid[i]=temp+'.'*blank+'*'*stone
    grid=list(map(list, zip(*grid)))
    for g in grid:
        print(''.join(g))