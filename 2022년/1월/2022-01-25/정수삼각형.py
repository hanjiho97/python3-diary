import sys
input = sys.stdin.readline

triangle=[]
n = int(input())
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j==0:
            triangle[i][j]+=triangle[i-1][j]
            continue
        if j==len(triangle[i])-1:
            triangle[i][j]+=triangle[i-1][j-1]
            continue
        triangle[i][j]+=max(triangle[i-1][j], triangle[i-1][j-1])


print(max(triangle[-1]))