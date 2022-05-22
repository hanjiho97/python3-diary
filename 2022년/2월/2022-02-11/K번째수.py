N = int(input())
k = int(input())
def binserach(start, end):
    while start<=end:
        mid=(start+end)//2
        count=N*(mid//N)
        count+=sum([mid//i for i in range(mid//N+1, N+1)])
        if count>=k: end=mid-1
        else: start=mid+1
    return start
print(binserach(1, N**2))