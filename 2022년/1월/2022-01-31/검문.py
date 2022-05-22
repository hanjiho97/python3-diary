import sys
input = sys.stdin.readline

N = int(input())
num=[int(input()) for _ in range(N)]

def GCD(a, b):
    if a%b:
        return GCD(b, a%b)
    else:
        return b

K=abs(num[1]-num[0])
for i in range(1, N-1):
    K=GCD(K, abs(num[i+1]-num[i]))

i=2
rest=set([K])
while i*i<=K:
    if not K%i:
        rest.add(i)
        rest.add(K//i)
    i+=1
print(*sorted(list(rest)))