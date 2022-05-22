import sys
input = sys.stdin.readline

N = int(input())
num = []

#소수 반출
def cal(n):
    for i in range(2, int(n**0.5)+1):
        if(n%i==0):
            return i, int(n/i)
        if(n==i):
            return -1, n
    return -1, n


if(N!=1):
    while True:
        a, b=cal(N)
        if(a==-1):
            print(b)
            break
        else:
            print(a)
            N=b