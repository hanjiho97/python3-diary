import sys
input = sys.stdin.readline

num = [list(map(int, input().split())) for _ in range(9)]
emptyspace = [(i, j) for i in range(9) for j in range(9) if num[i][j]==0]

#가지치기를 통해 확인 1. 가로 2. 세로 3. 정사각형
#가로,세로는 쉽게 확인 가능 문제는 정사각형  
#앞의 조건을 만족하는 숫자 리스트 중에 차례로 집어보기
#맞지 않으면 다시 뒤로 백

#후보군 찾기
def find(i, j):
    reference=set(list(i for i in range(10)))
    temp=set()
    #가로세로
    for k in range(9):
        temp.add(num[i][k])
        temp.add(num[k][j])
    #대각선
    a=i//3
    b=j//3
    for m in range(3):
        for n in range(3):
            temp.add(num[a*3+m][b*3+n])
    return list(reference-temp)

def fill(count):
    #종료조건 모든 빈칸이 채워졌을 때
    if count==len(emptyspace):
        for n in num:
            print(*n)
        exit(0)
    i, j =emptyspace[count]
    candidate=find(i, j)
    #백트래킹
    for candi in candidate:
        num[i][j]=candi
        fill(count+1)
        num[i][j]=0
fill(0)