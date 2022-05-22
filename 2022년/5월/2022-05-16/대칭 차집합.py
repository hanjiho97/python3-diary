import sys
input = sys.stdin.readline

N,M=map(int, input().split())
A=set(input().split())
B=set(input().split())
ans=len(A)+len(B)-2*len(A&B)
print(ans)