import sys
input = sys.stdin.readline

N = int(input())
data=list(map(int, input().split()))
sortdata=sorted(list(set(data)))

dic={sortdata[i]: i for i in range(len(sortdata))}

for d in data:
    sys.stdout.write('%d '%(dic[d]))