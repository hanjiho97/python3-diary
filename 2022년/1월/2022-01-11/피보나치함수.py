import sys
input = sys.stdin.readline

count1=[0]*41
count2=[0]*41

count1[0]=1
count2[1]=1

for i in range(2, 41):
    count1[i]=count1[i-1]+count1[i-2]
    count2[i]=count2[i-1]+count2[i-2]

for _ in range(int(input())):
    N=int(input())
    print("%d %d"%(count1[N], count2[N]))