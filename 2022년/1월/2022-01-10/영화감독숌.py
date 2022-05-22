import sys
input = sys.stdin.readline

N = int(input())

check=set()

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                check.add(int(str(i)+str(j)+str(k)+str(l)+'666'))
                check.add(int(str(i)+str(j)+str(k)+'666'+str(l)))
                check.add(int(str(i)+str(j)+'666'+str(k)+str(l)))
                check.add(int(str(i)+'666'+str(j)+str(k)+str(l)))

data=sorted(list(check))
print(data[N-1])