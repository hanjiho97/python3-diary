import sys
input = sys.stdin.readline

for _ in range(int(input())):
    word=[]
    for i in input().rstrip():
        if i=='(':
            word.append(i)
        elif i==')' and '(' not in word:
            word.append(i)
            break
        elif i==')' and '(' in word:
            word.pop()
    if not word:
        print('YES')
    else:
        print('NO')