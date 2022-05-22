import sys
input = sys.stdin.readline

#한수 체크
def check(n):
    L = str(n)
    try:
       p = int(L[1])-int(L[0])
    except:
        return True
    for i in range(len(L)-1):
        if(p==(int(L[i+1])-int(L[i]))):
            continue
        else:
            return False
    return True

N = int(input())
num = 0

for i in range(N):
    if(check(i+1)):
        num+=1
print(num)