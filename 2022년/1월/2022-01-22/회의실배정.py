import sys
input = sys.stdin.readline

#데이터 받기
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

#끝나는 시간순으로 정렬
data.sort(key=lambda x: x[0])
data.sort(key=lambda x: x[1])

ans=0
time=0
#그리디 알고리즘 끝나는 시간에 맞춰 최선의 선택
for start, finish in data:
    if start>=time:
        ans+=1
        time=finish
print(ans)