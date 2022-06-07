import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ans=0
    x1,y1,x2,y2=map(int, input().split())
    for _ in range(int(input())):
        xc,yc,r=map(int, input().split())
        if (((x1-xc)**2+(y1-yc)**2-r**2)*((x2-xc)**2+(y2-yc)**2-r**2))<0: ans+=1
    print(ans)