import sys
input = sys.stdin.readline

abc = [[[0]*21 for _ in range(21)] for _ in range(21)]

#top-down 방식
def calculate(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return calculate(20, 20, 20)
    if abc[a][b][c]!=0:
        return abc[a][b][c]
    if a<b and b<c:
        abc[a][b][c] = calculate(a, b, c-1) + calculate(a, b-1, c-1) - calculate(a, b-1, c)
    else:
        abc[a][b][c] = calculate(a-1, b, c) + calculate(a-1, b-1, c) + calculate(a-1, b, c-1) - calculate(a-1, b-1, c-1)
    return abc[a][b][c]
    

while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w(%d, %d, %d) = %d"%(a, b, c, calculate(a, b, c)))