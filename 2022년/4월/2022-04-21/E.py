import sys
input=sys.stdin.readline

def count(counter):
    num=0
    for i in range(11):
        sum=0
        for j in range(11):
            n=counter[i][j]
            sum+=n
            if n>1:
                num-=n*(n-1)//2
        num+=sum*(sum-1)//2
    return num

for _ in range(int(input())):
    n=int(input())
    counter=[[0]*11 for _ in range(11)]
    for _ in range(n):
        s=input().rstrip()
        counter[ord(s[0])-97][ord(s[1])-97]+=1
    ans=0
    ans+=count(counter)
    counter=list(map(list, zip(*counter)))
    ans+=count(counter)
    print(ans)