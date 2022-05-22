from lib2to3.pgen2.pgen import DFAState
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.sort()
time=0
temp=0
for i in range(N):
    temp+=P[i]
    time+=temp
print(time)