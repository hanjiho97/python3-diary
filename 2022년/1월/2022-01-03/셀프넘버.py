#유클리드 소거법으로 도전

#계산
def d(n):
    L = str(n)
    sum = 0
    for l in L:
        sum+=int(l)
    sum+=n
    return sum

#집합만들기
def mkset(n):
    result = set()
    while(n<=10000):
        result.add(n)
        n=d(n)
    return result

#기본 집합 생성
X = list(range(1, 10000))

while(True):
    try:
        if(X[0]<=10000):
            print(X[0])
            #순차적으로 제거
            X = sorted(set(X)-mkset(X[0]))
    except:
        break
