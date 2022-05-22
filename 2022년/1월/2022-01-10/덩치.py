import sys
input = sys.stdin.readline

N=int(input())

data=[]
for i in range(N):
    data.append(list(map(int, input().split())))
    
for i in range(N):
    ans = 1
    for j in range(N):
        if(i==j):
            continue
        elif(data[i][0]<data[j][0] and data[i][1]<data[j][1]):
            ans+=1
    print(ans, end=' ')