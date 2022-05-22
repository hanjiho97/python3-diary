import sys
input = sys.stdin.readline

N = int(input())
total=0
people=[]
for r in range(N):
    people.append(list(map(int, input().split())))
    total+=sum(people[r])

def calculate(x, y, d1, d2):
    global total
    one,two,three,four= 0,0,0,0
    c1=y+1
    for r in range(x+d1):
        if r>=x: c1-=1
        one+=sum(people[r][:c1])
    c2=y+1
    for r in range(x+d2+1):
        if r>x: c2+=1
        two+=sum(people[r][c2:])
    c3=y-d1
    for r in range(x+d1, N):
        three+=sum(people[r][:c3])
        if r<x+d1+d2: c3+=1
    c4=y+d2
    for r in range(x+d2+1, N):
        four+=sum(people[r][c4:])
        if r<=x+d1+d2: c4-=1
    five=total-one-two-three-four
    return max(one, two, three, four, five)-min(one, two, three, four, five)

ans=100000
for x in range(0, N-2):
    for y in range(0, N-1):
        for d1 in range(1, y):
            for d2 in range(1, min(N-x-d1, N-y)):
                ans=min(ans, calculate(x,y,d1,d2))
print(ans)