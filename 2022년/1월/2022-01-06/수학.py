import sys
input = sys.stdin.readline

for i in range(int(input())):
    x, y = map(int, input().split())
    target = y-x
    ans=1
    i=int(target**0.5)
    while True:
        sum=i*i
        ans=i*2-1
        if(target>sum):
            if(target<=sum+i):
                ans+=1
                break
            else:
                i+=1
                continue
        else:
            break
    print(ans)