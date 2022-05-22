from collections import deque
K=int(input())

rec=deque()
count=[0,0,0,0,0]
for _ in range(6):
    d,m=map(int, input().split())
    count[d]+=1
    rec.append((d,m))
    
if count[1]==1:
    if count[3]==1:
        while rec[0][0]!=3:
            rec.rotate()
    else:
        while rec[0][0]!=1:
            rec.rotate()
else:
    if count[4]==1:
        while rec[0][0]!=4:
            rec.rotate()
    else:
        while rec[0][0]!=2:
            rec.rotate()

print((rec[0][1]*rec[1][1]-rec[3][1]*rec[4][1])*K)