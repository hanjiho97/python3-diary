#그리디 문제
import sys
input = sys.stdin.readline

x, N = map(int, input().split())

#이진수 변환
x = format(x, 'b')

#변환횟수보다 1이 많은 경우
if N>x.count('1'): print(-1);
else:
    for i in range(N-1):
        x=x.replace('1','0',1)
        print(int(x,2), end=' ')
    print(0)