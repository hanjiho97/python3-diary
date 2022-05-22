import sys
from collections import Counter
input = sys.stdin.readline


def check(s):
    if len(s)%2: return False
    for i in range(0,len(s)-1, 2):
        if s[i]!=s[i+1]: return False
    return True

for _ in range(int(input())):
    s=input().rstrip()
    count=dict(Counter(s))
    target=[]
    ans=0
    for key, value in count.items():
        if value==1: target.append(key)
    for t in target:
        s=s[:s.find(t)]+s[s.find(t)+1:]
        count.pop(t)
        ans+=1
    print(s)