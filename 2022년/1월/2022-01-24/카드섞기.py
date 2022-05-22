import sys
input = sys.stdin.readline

N = int(input())
target=list(map(int, input().split()))
card = [i+1 for i in range(N)]

def shuffle(K, arr):
    dummy=arr[N-2**K:]
    M=2**K
    for i in range(2, K+2):
        temp=dummy[M-2**(K-i+1):M]+dummy[:M-2**(K-i+1)]
        M//=2
        for i in range(len(temp)):
            dummy[i]=temp[i]
    result=dummy+arr[:N-2**K]
    return result

k=0
while N>2**k:
    k+=1

#완전탐색
for i in range(k-1):
    for j in range(k-1):
        if shuffle(j+1, shuffle(i+1, card))==target:
            print(i+1, end=' ')
            print(j+1)
            break