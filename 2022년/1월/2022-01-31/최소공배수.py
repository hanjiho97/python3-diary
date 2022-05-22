import sys
input = sys.stdin.readline

def GCD(a, b):
    if a%b:
        return GCD(b, a%b)
    else:
        return b

for _ in range(int(input())):
    A, B = sorted(map(int, input().split()))
    print(A*B//GCD(B, A))