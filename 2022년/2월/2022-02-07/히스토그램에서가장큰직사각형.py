import sys
input = sys.stdin.readline

def bigrec(rec):
    N=len(rec)
    if N==1: return rec[0]
    return max(bigrec(rec[:N//2]), bigrec(rec[N//2:]), combine(rec))

def combine(rec):
    N=len(rec)
    start, end = N//2-1, N//2
    h , w = min(rec[start], rec[end]), 2 
    area = h*w
    while start>=0 and end<=N-1:
        if start==0 and end==N-1: break
        elif start==0: end+=1
        elif end==N-1: start-=1
        else:
            if rec[start-1]>=rec[end+1]: start-=1
            else: end+=1
        h=min(rec[start], rec[end], h)
        w+=1
        area=max(area, h*w)
    return area

data = list(map(int, input().split()))
while data[0]:
    rec = data[1:]
    print(bigrec(rec))
    data = list(map(int, input().split()))