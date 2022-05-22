import sys
from collections import Counter
input = sys.stdin.readline

data=[int(input()) for _ in range(int(input()))]
data.sort()
c = dict(Counter(data))

#최빈값 구하기
c=sorted(c.items(), key=lambda x:x[1], reverse=True)

print(round(sum(data)/len(data)))
print(data[len(data)//2])
try:
    if(c[0][1]==c[1][1]):
        print(c[1][0])
    else:
        print(c[0][0])
except:
    print(c[0][0])
print(data[-1]-data[0])