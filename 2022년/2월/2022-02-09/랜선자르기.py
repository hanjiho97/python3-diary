import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lan=[]
for _ in range(K):
    lan.append(int(input()))

def binsearch(data, target, start, end):
    while start<=end:
        mid=(start+end)//2
        n=0
        for d in data:
            n+=d//mid
        if n<target:
            end=mid-1
        else:
            start=mid+1
    return start-1

print(binsearch(lan, N, 1, max(lan)))