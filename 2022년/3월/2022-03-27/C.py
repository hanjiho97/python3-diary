import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    num = data.count(1)
    if num!=1:
        print('NO')
        continue
    data.append(data[0])
    flag=0
    for i in range(len(data)-1):
        if data[i+1]-data[i]>1: flag=1; break
    if flag: print('NO')
    else: print('YES')