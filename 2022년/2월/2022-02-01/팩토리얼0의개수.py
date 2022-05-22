import sys
input = sys.stdin.readline

N = int(input())

five=0
for i in range(2, N+1):
    while not i%5:
        five+=1
        i//=5

print(five)