import sys
input = sys.stdin.readline

N = int(input())
card = sorted(map(int, input().split()))
M = int(input())
tar = list(map(int, input().split()))

def first(data, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if data[mid]==target and (mid==0 or data[mid-1]<target):
            return mid
        elif data[mid]>=target:
            end=mid-1
        else:
            start=mid+1
    return 0

def last(data, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if data[mid]==target and (mid==N-1 or data[mid+1]>target):
            return mid+1
        elif data[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return 0

for t in tar:
    print(last(card, t, 0, N-1)-first(card, t, 0, N-1), end=' ')