import sys
input = sys.stdin.readline
a, b = map(int, input().split())
target=a
GCD=1
LCM=b
i=2
while i*i<=target:
    if not a%i:
        if not b%i:
            GCD*=i
            b//=i
        else:
            LCM*=i
        a//=i
    else:
        i+=1
if a>1:
    if not b%a:
        GCD*=a
    else:
        LCM*=a

print(GCD)
print(LCM)