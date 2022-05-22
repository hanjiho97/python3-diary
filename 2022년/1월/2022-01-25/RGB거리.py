import sys
input = sys.stdin.readline

RGB=[]
for _ in range(int(input())):
    RGB.append(list(map(int, input().split())))
for i in range(1, len(RGB)):
    RGB[i][0]=min(RGB[i-1][1],RGB[i-1][2])+RGB[i][0]
    RGB[i][1]=min(RGB[i-1][0],RGB[i-1][2])+RGB[i][1]
    RGB[i][2]=min(RGB[i-1][0],RGB[i-1][1])+RGB[i][2]

print(min(RGB[-1]))