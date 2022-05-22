import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def multiply(A, B):
    global C
    if B==1: return A%C
    m=multiply(A, B//2)
    if not B%2: return (m*m)%C
    else: return (m*m*A)%C

print(multiply(A, B))