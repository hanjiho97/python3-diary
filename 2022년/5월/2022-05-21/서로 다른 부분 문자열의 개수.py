import sys
input=sys.stdin.readline

count=set()
S=input().rstrip()
for i in range(1,len(S)+1):
    for j in range(len(S)-i+1):
        count.add(S[j:j+i])
print(len(count))