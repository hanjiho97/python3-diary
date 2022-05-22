import sys
input = sys.stdin.readline

S = input().rstrip()

sum = 0
for s in S:
    if(s=='Z' or s=='Y' or s=='X' or s=='W'):
        sum+=10
        continue
    elif(s=='T' or s=='U' or s=='V'):
        sum+=9
        continue
    elif(s=='S'):
        sum+=8
        continue
    else:
        sum+=(3+(ord(s)-65)//3)
print(sum)