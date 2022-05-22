import sys
input=sys.stdin.readline

S=input().rstrip()
prefix=[[0]*26]
for i in range(len(S)):
    temp=prefix[-1][:]
    temp[ord(S[i])-97]+=1
    prefix.append(temp)
for _ in range(int(input())):
    a,l,r=input().split()
    print(prefix[int(r)+1][ord(a)-97]-prefix[int(l)][ord(a)-97])