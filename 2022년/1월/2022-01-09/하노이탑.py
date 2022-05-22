import sys
input = sys.stdin.readline
N = int(input())
print(2**N-1)

def hanoi(N, start, temp, target):
    if(N==1):
        print("%d %d"%(start, target))
        return
    else:
        hanoi(N-1, start, target, temp)
        print("%d %d"%(start, target))
        hanoi(N-1, temp, start, target)

hanoi(N, 1, 2, 3)