import sys
input = sys.stdin.readline

n = int(input())
check=0
stack=[]
ans=[]
flag=1

for _ in range(n):
    arrival=int(input())
    if check<arrival:
        for i in range(check+1, arrival+1):
            stack.append(i)
            ans.append("+")
        stack.pop()
        ans.append("-")
        check=arrival
    else:
        if arrival==stack.pop():
            ans.append("-")
        else:
            flag=0
if flag:
    for a in ans:
        print(a)
else:
    print("NO")