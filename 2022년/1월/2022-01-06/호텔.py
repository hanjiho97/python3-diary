import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    Y=(N-1)%H+1
    X=(N-1)//H+1
    print(str(Y)+str(X).rjust(2,'0'))