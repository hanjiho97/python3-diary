import sys
input = sys.stdin.readline

for _ in range(int(input())):
    kind={}
    for _ in range(int(input())):
        name=list(input().rstrip().split())[-1]
        if name not in kind:
            kind[name]=1
        else:
            kind[name]+=1
    total=1
    for key, value in kind.items():
        total*=(value+1)
    print(total-1)