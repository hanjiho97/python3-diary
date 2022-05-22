import sys
input = sys.stdin.readline

def Binarysearch(data, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if data[mid]==target:
            return 1
        elif data[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return 0
            

N = int(input())
num = sorted(map(int, input().split()))
M = int(input())
tar = list(map(int, input().split()))

for t in tar:
    print(Binarysearch(num, t, 0, N-1))