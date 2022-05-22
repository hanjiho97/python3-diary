import sys
input = sys.stdin.readline
N, C = map(int, input().split())
loc=[int(input()) for _ in range(N)]
loc.sort()
def binseach(start, end):
    while start<=end:
        mid=(start+end)//2
        count=1
        distance=loc[0]
        for d in loc:
            if d>=distance+mid:
                distance=d
                count+=1
        if count>=C: start=mid+1
        else: end=mid-1
    return start-1
print(binseach(1, (loc[-1]-loc[0])//(C-1)+1))