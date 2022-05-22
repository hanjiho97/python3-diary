import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def countfive(num):
    i=1
    five=0
    while num>=5**i:
        five+=num//(5**i)
        i+=1
    return five

def counttwo(num):
    i=1
    two=0
    while num>=2**i:
        two+=num//(2**i)
        i+=1
    return two

totalfive=countfive(n)-countfive(m)-countfive(n-m)
totaltwo=counttwo(n)-counttwo(m)-counttwo(n-m)
print(min(totaltwo, totalfive))