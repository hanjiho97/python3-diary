import sys
input = sys.stdin.readline

#Ai는 Ai-1의 배수임으로 그리디 문제이다
N, K = map(int, input().split())
count=0
change = [int(input()) for _ in range(N)]

for i in change[::-1]:
    if K==0:
        break
    count+=K//i
    K=K%i
print(count)