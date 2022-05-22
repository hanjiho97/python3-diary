import sys
input=sys.stdin.readline

def check(s):
    check=[0]*2
    for i in range(len(s)):
        if s[i]=='B': check[0]=1
        else: check[1]=1
    if check[0] and check[1]: return True
    else: return False

for _ in range(int(input())):
    n=int(int(input()))
    S=input().rstrip().split('W')
    flag=True
    for s in S:
        if not s: continue
        if not check(s):
            flag=False
            break
    if flag: print('Yes')
    else: print('No')