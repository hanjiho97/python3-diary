import sys
input = sys.stdin.readline

pn=[False, False]+[True]*9999

#소수찾기
for i in range(2, 101):
    if pn[i]:
        for j in range(2*i, 10000, i):
            pn[j]=False

for i in range(int(input())):
    n = int(input())
    a = pn.index(True, n//2)
    while True:
        if pn[n-a]:
            print("%d %d"%(n-a, a))
            break
        else:
            a = pn.index(True, a+1)