import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l, r = map(int, input().split())
    a = list(map(int, input().split()))
    cnt=[0]*17
    for i in range(len(a)):
        s=format(a[i], 'b')
        for i in range(len(s)-1, -1, -1):
            if s[len(s)-i-1]=='1': cnt[i]+=1
    n=r-l+1
    ans=''
    for i in range(16, -1, -1):
        if cnt[i]>n-cnt[i]: ans+='1'
        else: ans+='0'
    print(int(ans, 2))