import sys
input = sys.stdin.readline

#소인수분해
def find_factor(m):
    i=2
    factors={}
    while i*i<=m:
        if m%i:
            i+=1
        else:
            factors[i]=0
            while not m%i:
                factors[i]+=1
                m//=i
    if m>1:
        factors[m]=1
    return factors

while True:
    try:
        n, m = map(int, input().split())
        if m==0:
            print('%d does not divide %d!'%(m, n))
            continue
    except:
        break
    flag=0
    for prime, num in find_factor(m).items():
        i=1
        sum=0
        while prime**i<=n:
            sum+=n//(prime**i)
            i+=1
        if sum<num:
            flag=1
            break
    if flag:
        print('%d does not divide %d!'%(m, n))
    else:
        print('%d divides %d!'%(m, n))