import sys
input=sys.stdin.readline

N=int(input())
l=sorted(map(int, input().split()))

s,e=0,N-1
dif=10**10
while s<e:
    temp=abs(l[s]+l[e])
    if temp==0: one,two=l[s],l[e]; break
    elif temp<dif: one,two=l[s],l[e]; dif=temp
    if abs(l[s])<abs(l[e]): e-=1
    else: s+=1
print('%d %d'%(one,two))