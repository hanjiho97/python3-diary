from re import T
import sys
input = sys.stdin.readline

#그리디 알고리즘 정렬 후 큰 수와 작은 수를 엮는다
data=[]
a=0
b=-1
ans=0
for _ in range(int(input())):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x: x[1])

while data[a][0]>0:
    ans=max(ans, data[a][1]+data[b][1])
    pair=min(data[a][0], data[b][0])
    data[a][0]-=pair
    data[b][0]-=pair
    if not data[a][0]:
        a+=1
    if not data[b][0]:
        b-=1
print(ans)