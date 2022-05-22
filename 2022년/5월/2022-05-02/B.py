import sys
input=sys.stdin.readline

for _ in range(int(input())):
    s=input().rstrip()
    if s[0]>s[1]: index=(ord(s[0])-97)*25+(ord(s[1])-96)
    else: index=(ord(s[0])-97)*25+(ord(s[1])-97)
    print(index)